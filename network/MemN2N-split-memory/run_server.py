from __future__ import absolute_import
from __future__ import print_function

from data_utils import load_dialog_task, myload_dialog_task,vectorize_data, load_candidates, vectorize_candidates, \
    vectorize_candidates_sparse, tokenize
from sklearn import metrics
from memn2n import MemN2NDialog
from itertools import chain
from six.moves import range, reduce
import sys
import tensorflow as tf
import numpy as np
import os
import pickle
import os
import threading
import json
import os
import threading
#from watson_developer_cloud import ConversationV1
from flask import request
from flask import Flask, jsonify
from flask import abort


tf.flags.DEFINE_float("learning_rate", 0.001, "Learning rate for Adam Optimizer.")
tf.flags.DEFINE_float("epsilon", 1e-8, "Epsilon value for Adam Optimizer.")
tf.flags.DEFINE_float("max_grad_norm", 40.0, "Clip gradients to this norm.")
tf.flags.DEFINE_integer("evaluation_interval", 10, "Evaluate and print results every x epochs")
tf.flags.DEFINE_integer("batch_size", 32, "Batch size for training.")
tf.flags.DEFINE_integer("hops", 3, "Number of hops in the Memory Network.")
tf.flags.DEFINE_integer("epochs", 50, "Number of epochs to train for.")
tf.flags.DEFINE_integer("embedding_size", 20, "Embedding size for embedding matrices.")
tf.flags.DEFINE_integer("memory_size", 250, "Maximum size of memory.")
tf.flags.DEFINE_integer("task_id", 1, "task id, 1 <= id <= 5")
tf.flags.DEFINE_integer("random_state", None, "Random state.")
tf.flags.DEFINE_string("data_dir", "../data/personalized-dialog-dataset/full",
                       "Directory containing personalized dialog tasks")
tf.flags.DEFINE_string("model_dir", "model/", "Directory containing memn2n model checkpoints")
tf.flags.DEFINE_boolean('train', False, 'if True, begin to train')
tf.flags.DEFINE_boolean('OOV', False, 'if True, use OOV test set')
tf.flags.DEFINE_boolean('save_vocab', False, 'if True, saves vocabulary')
tf.flags.DEFINE_boolean('load_vocab', False, 'if True, loads vocabulary instead of building it')
FLAGS = tf.flags.FLAGS
print("Started Task:", FLAGS.task_id)


class chatBot(object):
    def __init__(self, data_dir, model_dir, task_id,
                 OOV=False,
                 memory_size=250,
                 random_state=None,
                 batch_size=32,
                 learning_rate=0.001,
                 epsilon=1e-8,
                 max_grad_norm=40.0,
                 evaluation_interval=10,
                 hops=3,
                 epochs=10,
                 embedding_size=20,
                 save_vocab=False,
                 load_vocab=False):
        """Creates wrapper for training and testing a chatbot model.

        Args:
            data_dir: Directory containing personalized dialog tasks.

            model_dir: Directory containing memn2n model checkpoints.

            task_id: Personalized dialog task id, 1 <= id <= 5. Defaults to `1`.

            OOV: If `True`, use OOV test set. Defaults to `False`

            memory_size: The max size of the memory. Defaults to `250`.

            random_state: Random state to set graph-level random seed. Defaults to `None`.

            batch_size: Size of the batch for training. Defaults to `32`.

            learning_rate: Learning rate for Adam Optimizer. Defaults to `0.001`.

            epsilon: Epsilon value for Adam Optimizer. Defaults to `1e-8`.

            max_gradient_norm: Maximum L2 norm clipping value. Defaults to `40.0`.

            evaluation_interval: Evaluate and print results every x epochs.
            Defaults to `10`.

            hops: The number of hops over memory for responding. A hop consists
            of reading and addressing a memory slot. Defaults to `3`.

            epochs: Number of training epochs. Defualts to `200`.

            embedding_size: The size of the word embedding. Defaults to `20`.

            save_vocab: If `True`, save vocabulary file. Defaults to `False`.

            load_vocab: If `True`, load vocabulary from file. Defaults to `False`.
        """

        self.data_dir = data_dir
        self.task_id = task_id
        self.model_dir = model_dir
        self.OOV = OOV
        self.memory_size = memory_size
        self.random_state = random_state
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.epsilon = epsilon
        self.max_grad_norm = max_grad_norm
        self.evaluation_interval = evaluation_interval
        self.hops = hops
        self.epochs = epochs
        self.embedding_size = embedding_size
        self.save_vocab = save_vocab
        self.load_vocab = load_vocab

        candidates, self.candid2indx = load_candidates(self.data_dir, self.task_id)
        self.n_cand = len(candidates)
        # print("Candidate Size", self.n_cand)
        self.indx2candid = dict((self.candid2indx[key], key)
                                for key in self.candid2indx)

        # Task data
        self.trainData, self.testData, self.valData = load_dialog_task(
            self.data_dir, self.task_id, self.candid2indx, self.OOV)

        # print(self.testData)
        data = self.trainData + self.testData + self.valData

        self.build_vocab(data, candidates, self.save_vocab, self.load_vocab)
        print("build_vocab", self.build_vocab)
        self.candidates_vec = vectorize_candidates(
            candidates, self.word_idx, self.candidate_sentence_size)
        print("build_vocab", self.candidates_vec)
        optimizer = tf.train.AdamOptimizer(
            learning_rate=self.learning_rate, epsilon=self.epsilon)

        self.sess = tf.Session()

        self.model = MemN2NDialog(self.batch_size, self.vocab_size, self.n_cand,
                                  self.sentence_size, self.embedding_size,
                                  self.candidates_vec, session=self.sess,
                                  hops=self.hops, max_grad_norm=self.max_grad_norm,
                                  optimizer=optimizer, task_id=task_id)

        self.saver = tf.train.Saver(max_to_keep=50)

        # self.summary_writer = tf.summary.FileWriter(
        #     self.model.root_dir, self.model.graph_output.graph)

    def build_vocab(self, data, candidates, save=False, load=False):
        """Build vocabulary of words from all dialog data and candidates."""
        if load:
            print("I am here!!")
            # Load from vocabulary file
            vocab_file = open('vocab' + str(self.task_id) + '.obj', 'rb')
            vocab = pickle.load(vocab_file)
        else:
            vocab = reduce(lambda x, y: x | y,
                           (set(list(chain.from_iterable(s)) + q)
                            for p, s, q, a in data))
            vocab |= reduce(lambda x, y: x | y,
                            (set(list(chain.from_iterable(p)) + q)
                             for p, s, q, a in data))
            vocab |= reduce(lambda x, y: x | y,
                            (set(candidate) for candidate in candidates))
            vocab = sorted(vocab)

        self.word_idx = dict((c, i + 1) for i, c in enumerate(vocab))
        max_story_size = max(map(len, (s for _, s, _, _ in data)))
        mean_story_size = int(np.mean([len(s) for _, s, _, _ in data]))
        print("mean_story_size is ", mean_story_size)
        self.sentence_size = max(map(len, chain.from_iterable(s for _, s, _, _ in data)))
        #print("the size is ", candidates)
        self.candidate_sentence_size = max(map(len, candidates))

        query_size = max(map(len, (q for _, _, q, _ in data)))
        self.memory_size = min(self.memory_size, max_story_size)
        self.vocab_size = len(self.word_idx) + 1  # +1 for nil word
        self.sentence_size = max(query_size, self.sentence_size)  # for the position

        # Print parameters
        print("vocab size:", self.vocab_size)
        print("Longest sentence length", self.sentence_size)
        print("Longest candidate sentence length", self.candidate_sentence_size)
        print("Longest story length", max_story_size)
        print("Average story length", mean_story_size)

        # Save to vocabulary file
        if save:
            vocab_file = open('vocab' + str(self.task_id) + '.obj', 'wb')
            pickle.dump(vocab, vocab_file)

    def train(self):
        """Runs the training algorithm over training set data.

        Performs validation at given evaluation intervals.
        """
        trainP, trainS, trainQ, trainA = vectorize_data(
            self.trainData, self.word_idx, self.sentence_size,
            self.batch_size, self.n_cand, self.memory_size)
        valP, valS, valQ, valA = vectorize_data(
            self.valData, self.word_idx, self.sentence_size,
            self.batch_size, self.n_cand, self.memory_size)
        n_train = len(trainS)
        n_val = len(valS)
        print("Training Size", n_train)
        print("Validation Size", n_val)
        tf.set_random_seed(self.random_state)
        batches = zip(range(0, n_train - self.batch_size, self.batch_size),
                      range(self.batch_size, n_train, self.batch_size))
        batches = [(start, end) for start, end in batches]
        best_validation_accuracy = 0

        # Training loop
        # for each in self.indx2candid:
        #     print(self.indx2candid[each]+"\n")
        for t in range(1, self.epochs + 1):
            print('Epoch', t)
            np.random.shuffle(batches)
            total_cost = 0.0
            for start, end in batches:
                p = trainP[start:end]
                s = trainS[start:end]
                q = trainQ[start:end]
                a = trainA[start:end]
                cost_t = self.model.batch_fit(p, s, q, a)
                total_cost += cost_t
            if t % self.evaluation_interval == 0:
                # Perform validation
                train_preds = self.batch_predict(trainP, trainS, trainQ, n_train)
                #print("train_preds is ", train_preds)
                # for  a in train_preds:
                # print("key",self.indx2candid[a])

                print("___________________")
                val_preds = self.batch_predict(valP, valS, valQ, n_val)

                #print("val_preds is ", val_preds)

                # print(dict(self.candid2indx[key] for key in val_preds))
                # print("___________________")
                train_acc = metrics.accuracy_score(np.array(train_preds), trainA)
                val_acc = metrics.accuracy_score(val_preds, valA)
                print('-----------------------')
                print('Epoch', t)
                print('Total Cost:', total_cost)
                print('Training Accuracy:', train_acc)
                print('Validation Accuracy:', val_acc)
                print('-----------------------')

                # Write summary
                train_acc_summary = tf.summary.scalar(
                    'task_' + str(self.task_id) + '/' + 'train_acc',
                    tf.constant((train_acc), dtype=tf.float32))
                val_acc_summary = tf.summary.scalar(
                    'task_' + str(self.task_id) + '/' + 'val_acc',
                    tf.constant((val_acc), dtype=tf.float32))
                merged_summary = tf.summary.merge([train_acc_summary, val_acc_summary])
                summary_str = self.sess.run(merged_summary)
                self.summary_writer.add_summary(summary_str, t)
                self.summary_writer.flush()

                if val_acc > best_validation_accuracy:
                    best_validation_accuracy = val_acc
                    self.saver.save(self.sess, self.model_dir + 'model.ckpt',
                                    global_step=t)

    def test(self):
        """Runs testing on testing set data.

        Loads best performing model weights based on validation accuracy.
        """
        ckpt = tf.train.get_checkpoint_state(self.model_dir)
        if ckpt and ckpt.model_checkpoint_path:
            self.saver.restore(self.sess, ckpt.model_checkpoint_path)
        else:
            print("...no checkpoint found...")

        testP, testS, testQ, testA = vectorize_data(
            self.testData, self.word_idx, self.sentence_size,
            self.batch_size, self.n_cand, self.memory_size)
        n_test = len(testS)
        # for i in range(len(testP)):
        #     print("A",testP[i])
        print("Testing Size", n_test)

        test_preds = self.batch_predict(testP, testS, testQ, n_test)
        test_acc = metrics.accuracy_score(test_preds, testA)
        print("Testing Accuracy:", test_acc)

        # # Un-comment below to view correct responses and predictions
        # print(testA)
        # for pred in test_preds:
        #     print(pred, self.indx2candid[pred])

    # def loadmodel(self):
    #     ckpt = tf.train.get_checkpoint_state(self.model_dir)
    #     if ckpt and ckpt.model_checkpoint_path:
    #         self.saver.restore(self.sess, ckpt.model_checkpoint_path)
    #     else:
    #         print("...no checkpoint found...")
    # def test2(self):
    #     self.testData= myload_dialog_task(self.candid2indx, self.OOV)
    #     print(len(self.testData))
    #
    #     testP, testS, testQ, testA = vectorize_data(
    #         self.testData, self.word_idx, self.sentence_size,
    #         self.batch_size, self.n_cand, self.memory_size)
    #     n_test = len(testS)
    #     # for i in range(len(testP)):
    #     #     print("A",testP[i]) # length and A are correct
    #
    #     test_preds = self.batch_predict(testP, testS, testQ, n_test)
    #     test_acc = metrics.accuracy_score(test_preds, testA)
    #     #print("Testing Accuracy:", test_acc)
    #     current = []
    #     for i in range(len(test_preds)):
    #         current.append(self.indx2candid[test_preds[i]])
    #     print("Testing Accuracy:", test_acc)
    #     return current
    def loadmodel(self):
        ckpt = tf.train.get_checkpoint_state(self.model_dir)
        if ckpt and ckpt.model_checkpoint_path:
            self.saver.restore(self.sess, ckpt.model_checkpoint_path)
        else:
            print("...no checkpoint found...")
    def test2(self):

        self.testData= myload_dialog_task(self.candid2indx, self.OOV)
        # print(len(self.testData))
        # print(self.testData)
        testP, testS, testQ, testA = vectorize_data(
            self.testData, self.word_idx, self.sentence_size,
            self.batch_size, self.n_cand, self.memory_size)
        n_test = len(testS)
        # for i in range(len(testP)):
        #     print("P",testP[i]) # length and A are correct

        test_preds = self.batch_predict(testP, testS, testQ, n_test)
        test_acc = metrics.accuracy_score(test_preds, testA)
        # if test_acc<1:
        #     print(testA,len(testA),len(n_test))
        #print("Testing Accuracy:", test_acc)
        current = []
        for i in range(len(test_preds)):
            current.append(self.indx2candid[test_preds[i]])
        print("Testing Accuracy:", test_acc)
        return current
    def batch_predict(self, P, S, Q, n):
        """Predict answers over the passed data in batches.

        Args:
            P: Tensor (None, sentence_size)
            S: Tensor (None, memory_size, sentence_size)
            Q: Tensor (None, sentence_size)
            n: int

        Returns:
            preds: Tensor (None, vocab_size)
        """
        preds = []
        for start in range(0, n, self.batch_size):
            end = start + self.batch_size
            p = P[start:end]
            s = S[start:end]
            q = Q[start:end]
            pred = self.model.predict(p, s, q)
            preds += list(pred)
        return preds

    def close_session(self):
        self.sess.close()
model_dir = "task" + str(FLAGS.task_id) + "_" + FLAGS.model_dir
chatbot = chatBot(FLAGS.data_dir, model_dir, FLAGS.task_id, OOV=FLAGS.OOV,
                      batch_size=FLAGS.batch_size, memory_size=FLAGS.memory_size,
                      epochs=FLAGS.epochs, hops=FLAGS.hops, save_vocab=FLAGS.save_vocab,
                      load_vocab=FLAGS.load_vocab, learning_rate=FLAGS.learning_rate,
                      embedding_size=FLAGS.embedding_size)

app = Flask(__name__)
global k
k=0

@app.route('/', methods=['GET','POST'])
def create_task():
    if not request.json or not 'slot' in request.json:
        return jsonify({'error': "no slot"}), 201
    if not request.json or not 'Action' in request.json:
        return jsonify({'error': "no Action"}), 201
    if not request.json or not 'profile' in request.json:
        return jsonify({'error': "no profile"}), 201



    input_question = request.json['slot']
    if len(input_question)!=2 or input_question[0] not in ["2","3","4","5","6"] or input_question[1] not in ["8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00"]:
        return jsonify({'error': 'slot format error, it should be like ["6","13:00"]'}), 201

    to=str(input_question[0])+","+str(input_question[1])

    data={}
    global k
    pro=request.json['profile']
    if len(pro)!=2:
        return jsonify({'error': 'profile format error, it should be like ["male,elderly"]'}), 201
    pro = str(pro[0]) + "," + str(pro[1])
    if pro not in ["male,elderly","male,middle-aged","male,young","female,elderly","female,middle-aged","female,young"]:
        return jsonify({'error': 'profile value error,it should be like ["male,elderly"]'}), 201

    print(pro)
    act=request.json['Action']
    # ans=ans[k]

    if act not in ["start","sayAll","wait","sitAtBar","combineTables","changeRestaurant","changeTime","callBackLater","sayThanks","close","askForReason","askForBiggerTable","askForAlternatives","tableFor2","tentativelyReserve"]:
        return jsonify({'error': "action value error"}), 201


    # print("ans= ", ans)
    #
    f = open(
        "../data/personalized-dialog-dataset/full/personalized-dialog-task1-API-calls-tst.txt", "w")
    txt = ["1 "+to+","+pro,
           "2 "+str(act)+"	Greetings sir. 8:00 3",
           "3 "+str(act)+"	Greetings sir. 8:00 3",
           "4 "+str(act)+"	Greetings sir. 8:00 3",
           "5 "+str(act)+"	Greetings sir. 8:00 3"]
    for i in range(len(txt)):
        f.write(txt[i])
        f.write("\n")
    f.close()
    ans = chatbot.test2()

    if act !="sayAll":
        fi = ans[0].split(" ")[0:-2]
        data["response"] = " ".join(fi)
        print(data["response"])
    else:
        data["response"]=ans[0]



    print(jsonify(data))
    return jsonify(data), 201










if __name__ == '__main__':
    #model_dir = "task" + str(FLAGS.task_id) + "_" + FLAGS.model_dir
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    chatbot.loadmodel()

    app.run(host='0.0.0.0', debug=True, port=int(os.getenv('PORT', 9000)), use_reloader=False, threaded=True)

    chatbot.close_session()
