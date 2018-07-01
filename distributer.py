import json
import os
import threading
#from watson_developer_cloud import ConversationV1
from flask import request
from flask import Flask, jsonify
from flask import abort
import urllib.request

def farward(port,body):

    from flask import jsonify

    #body = {"slot": ["4", "12:00"]}

    myurl = "http://0.0.0.0:"+str(port)
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    print(jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes)
    print("here")
    data = json.loads(response.read().decode('utf-8'))
    return (data)



app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def create_task():
    if not request.json or not 'Action' in request.json:
        return jsonify({'error': "no text"}), 201
    way=request.json['Action']
    if way=="start":
        data=farward(9001,request.json)
    elif way=="sayAll":
        data=farward(9002,request.json)
    elif way=="wait":
        data=farward(9003,request.json)
    elif way=="sitAtBar":
        data=farward(9004,request.json)
    elif way=="combineTables":
        data=farward(9005,request.json)
    elif way=="changeRestaurant":
        data=farward(9006,request.json)
    elif way=="changeTime":
        data=farward(9007,request.json)
    elif way=="callBackLater":
        data=farward(9008,request.json)
    elif way=="sayThanks":
        data=farward(9009,request.json)
    elif way=="close":
        data=farward(9010,request.json)
    elif way=="askForReason":
        data=farward(9011,request.json)
    elif way=="askForBiggerTable":
        data=farward(9012,request.json)
    elif way=="askForAlternatives":
        data=farward(9013,request.json)
    else:
        return jsonify({'error': "Action error"}), 201




    return jsonify(data), 201

if __name__ == '__main__':
    print("Multiple Workspace Ready.")
    app.run(host='0.0.0.0', debug=True, port=int(os.getenv('PORT', 9000)), use_reloader=False, threaded=True)