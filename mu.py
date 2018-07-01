# import json
# import urllib.request
# from flask import jsonify
#
#
# body = {"slot": ["4","12:00"]}
#
# myurl = "http://9.186.52.186:9002"
# req = urllib.request.Request(myurl)
# req.add_header('Content-Type', 'application/json; charset=utf-8')
# jsondata = json.dumps(body)
# jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
# req.add_header('Content-Length', len(jsondataasbytes))
# print (jsondataasbytes)
# response = urllib.request.urlopen(req, jsondataasbytes)
# data = json.loads(response.read().decode('utf-8'))
# print(data['response'])
# a="fejifjeijksdl fiejflsdjkl fejifjids {fefef} fefjeiofj{fefsjdif}"
# b=a.replace("{", "X");
# print(b)
import os
pre = os.popen('source activate root')
#pretst = os.popen('./runwithpre.sh')
output1 = os.popen('cd /Users/gy12/Desktop/notebooks/multi/1/MemN2N-split-memory; python 1.py --train False --task_id 1 &')
output2 = os.popen('cd /Users/gy12/Desktop/notebooks/multi/2/MemN2N-split-memory; python 1.py --train False --task_id 1 &')
output3 = os.popen('cd /Users/gy12/Desktop/notebooks/multi/3/MemN2N-split-memory; python 1.py --train False --task_id 1 &')
output4 = os.popen('cd /Users/gy12/Desktop/notebooks/multi/4/MemN2N-split-memory; python 1.py --train False --task_id 1 &')
output5 = os.popen('cd /Users/gy12/Desktop/notebooks/multi/5/MemN2N-split-memory; python 1.py --train False --task_id 1 &')
output6 = os.popen('cd /Users/gy12/Desktop/notebooks/multi/6/MemN2N-split-memory; python 1.py --train False --task_id 1 &')
output7 = os.popen('cd /Users/gy12/Desktop/notebooks/multi/7/MemN2N-split-memory; python 1.py --train False --task_id 1 &')
output8 = os.popen('cd /Users/gy12/Desktop/notebooks/multi/8/MemN2N-split-memory; python 1.py --train False --task_id 1 &')
output9 = os.popen('cd /Users/gy12/Desktop/notebooks/multi/9/MemN2N-split-memory; python 1.py --train False --task_id 1 &')
# #output10 = os.popen('cd /Users/gy12/Desktop/notebooks/multi/2/MemN2N-split-memory; python 1.py --train False --task_id 1 &')
output11 = os.popen('cd /Users/gy12/Desktop/notebooks/multi/11/MemN2N-split-memory; python 1.py --train False --task_id 1 &')
output12 = os.popen('cd /Users/gy12/Desktop/notebooks/multi/12/MemN2N-split-memory; python 1.py --train False --task_id 1 &')
output13 = os.popen('cd /Users/gy12/Desktop/notebooks/multi/13/MemN2N-split-memory; python 1.py --train False --task_id 1 &')
all = os.popen('cd /Users/gy12/Desktop/notebooks/multi; /Users/gy12/anaconda/envs/py35/bin/python distributer.py &')




#print(output1.read())
