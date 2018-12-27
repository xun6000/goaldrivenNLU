from __future__ import absolute_import

import os
import re
import numpy as np
import tensorflow as tf

stop_words = set(["a","an","the"])


def load_candidates(data_dir, task_id):
    """Load bot response candidates."""
    assert task_id > 0 and task_id < 6

    candidates=[]
    candidates_f=None
    candid_dic={}
    candidates_f='../personalized-dialog-candidates.txt'
    with open(os.path.join(data_dir,candidates_f)) as f:
        for i,line in enumerate(f):
            candid_dic[line.strip().split(' ',1)[1]] = i
            line=tokenize(line.strip())[1:]
            candidates.append(line)
    return candidates,candid_dic


def load_dialog_task(data_dir, task_id, candid_dic, isOOV):
    """Load the nth task. There are 5 tasks in total.

    Returns a tuple containing the training and testing data for the task.
    """
    assert task_id > 0 and task_id < 6

    files = os.listdir(data_dir)
    files = [os.path.join(data_dir, f) for f in files]
    s = 'personalized-dialog-task{}-'.format(task_id)
    train_file = [f for f in files if s in f and 'trn' in f][0]
    if isOOV:
        test_file = [f for f in files if s in f and 'tst-OOV' in f][0]
    else: 
        test_file = [f for f in files if s in f and 'tst.' in f][0]
    val_file = [f for f in files if s in f and 'dev' in f][0]
    train_data = get_dialogs(train_file,candid_dic)
    test_data = get_dialogs(test_file,candid_dic)
    val_data = get_dialogs(val_file,candid_dic)
    return train_data, test_data, val_data
def myload_dialog_task(candid_dic, isOOV,data_dir="../data/personalized-dialog-dataset/full/"):
    """Load the nth task. There are 5 tasks in total.

    Returns a tuple containing the training and testing data for the task.
    """
    task_id=1
    assert task_id > 0 and task_id < 6

    files = os.listdir(data_dir)
    files = [os.path.join(data_dir, f) for f in files]
    s = 'personalized-dialog-task{}-'.format(task_id)
    # train_file = [f for f in files if s in f and 'trn' in f][0]
    if isOOV:
        test_file = [f for f in files if s in f and 'tst-OOV' in f][0]
    else:
        test_file = [f for f in files if s in f and 'tst.' in f][0]

    # val_file = [f for f in files if s in f and 'dev' in f][0]
    # train_data = get_dialogs(train_file,candid_dic)
    #print("the loaded test file road is ", test_file)
    test_data = get_dialogs(test_file,candid_dic)
    #print("the loaded test file is ", test_data,test_file)
    #val_data = get_dialogs(val_file,candid_dic)
    print("loaded test data")
    return test_data


def tokenize(sent):
    """Return the tokens of a sentence including punctuation.
    
    >>> tokenize('Bob dropped the apple. Where is the apple?')
    ['Bob', 'dropped', 'the', 'apple', '.', 'Where', 'is', 'the', 'apple']
    """
    sent=sent.lower()
    if sent=='<silence>':
        return [sent]
    result=[x.strip() for x in re.split('(\W+)?', sent) if x.strip() and x.strip() not in stop_words]
    if not result:
        result=['<silence>']
    if result[-1]=='.' or result[-1]=='?' or result[-1]=='!':
        result=result[:-1]
    return result

def parse_dialogs_per_response(lines,candid_dic):
    """Parse dialogs provided in the personalized dialog tasks format."""
    data = []
    context = []
    context_profile = []
    u = None
    r = None
    for line in lines:
        line=line.strip()
        if line:
            nid, line = line.split(' ', 1)
            nid = int(nid)
            if nid == 1:
                # Process profile attributes
                attribs = line.split(' ')
                for attrib in attribs:
                    r=tokenize(attrib)
                    # Add temporal encoding, and utterance/response encoding
                    r.append('$r')
                    r.append('#'+str(nid))
                    context_profile.append(r)

            else:
                # Process conversation turns
                if '\t' in line:
                    # Process turn containing bot response
                    u, r = line.split('\t')
                    a = candid_dic[r]
                    u = tokenize(u)
                    r = tokenize(r)
                    data.append((context_profile[:],context[:],u[:],a))
                    u.append('$u')
                    u.append('#'+str(nid))
                    r.append('$r')
                    r.append('#'+str(nid))
                    context.append(u)
                    context.append(r)
                else:
                    # Process turn without bot response
                    r=tokenize(line)
                    r.append('$r')
                    r.append('#'+str(nid))
                    context.append(r)
        else:
            # Clear contexts
            context=[]
            context_profile=[]
    return data



def get_dialogs(f,candid_dic):
    """Given a file name, read the file, retrieve the dialogs, and then convert 
    the sentences into a single dialog.
    
    If max_length is supplied, any stories longer than max_length tokens will 
    be discarded.
    """
    with open(f) as f:
        return parse_dialogs_per_response(f.readlines(),candid_dic)


def vectorize_candidates_sparse(candidates,word_idx):
    shape=(len(candidates),len(word_idx)+1)
    indices=[]
    values=[]
    for i,candidate in enumerate(candidates):
        for w in candidate:
            indices.append([i,word_idx[w]])
            values.append(1.0)
    return tf.SparseTensor(indices,values,shape)


def vectorize_candidates(candidates,word_idx,sentence_size):
    shape=(len(candidates),sentence_size)
    C=[]
    for i,candidate in enumerate(candidates):
        lc=max(0,sentence_size-len(candidate))
        C.append([word_idx[w] if w in word_idx else 0 for w in candidate] + [0] * lc)
    return tf.constant(C,shape=shape)


def vectorize_data(data, word_idx, sentence_size, 
                   batch_size, candidates_size, max_memory_size):
    """Vectorize profile, stories and queries.

    If a sentence length < sentence_size, the sentence will be padded with 0's.

    If a story length < memory_size, the story will be padded with empty memories.
    Empty memories are 1-D arrays of length sentence_size filled with 0's.

    The answer array is returned as a one-hot encoding.
    """
    P = []
    S = []
    Q = []
    A = []
    data.sort(key=lambda x:len(x[0]),reverse=True)
    for i, (profile, story, query, answer) in enumerate(data):
        if i%batch_size==0:
            memory_size=max(1,min(max_memory_size,len(story)))
        pp = []
        for i, sentence in enumerate(profile, 1):
            lp = max(0, sentence_size - len(sentence))
            pp.append([word_idx[w] if w in word_idx else 0 for w in sentence] + [0] * lp)

        ss = []
        for i, sentence in enumerate(story, 1):
            ls = max(0, sentence_size - len(sentence))
            ss.append([word_idx[w] if w in word_idx else 0 for w in sentence] + [0] * ls)

        # Take only the most recent sentences that fit in memory
        ss = ss[::-1][:memory_size][::-1]

        # Pad to memory_size
        lm = max(0, memory_size - len(ss))
        for _ in range(lm):
            ss.append([0] * sentence_size)

        lq = max(0, sentence_size - len(query))
        q = [word_idx[w] if w in word_idx else 0 for w in query] + [0] * lq

        P.append(np.array(pp))
        S.append(np.array(ss))
        Q.append(np.array(q))
        A.append(np.array(answer))
    return P, S, Q, A
