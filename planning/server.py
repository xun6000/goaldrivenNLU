import os
from flask import request
from flask import Flask, jsonify
import variables


app = Flask(__name__)


def clean(initial):
    init = []
    for i in initial:
        if i[1] == 'start' or i[1] == 'close' or i[1] == 'sizeIssue' or i[1] == 'timeIssue':
            continue
        else:
            init.append(i)
    return init


def paren(action_list):
    new_list = []
    for action in action_list:
        new_list.append(action.strip('()'))
    return new_list


@app.route('/', methods=['GET', 'POST'])
def create_task():
    if not request.json or 'text' not in request.json:
        return jsonify({'error': "no text"}), 201
    print(request.json)
    variables.input_text = request.json['text']
    variables.input_info = request.json['information']

    # -------------------------------------------------

    import main
    main.plan(variables.input_text, variables.input_info)

    # -------------------------------------------------

    data = {}

    data["response"] = variables.response
    data["history"] = variables.flowchart_history
    data["current position"] = variables.position
    data["plan"] = paren(variables.action_list)
    data["intent"] = variables.intent_list
    data["dialogue state"] = clean(variables.init)
    data["pushMessage"] = variables.situation
    data["restaurant"] = variables.restaurant
    print(data)

    return jsonify(data), 200


if __name__ == '__main__':
    # print("Multiple Workspace Ready.")
    app.run(host='0.0.0.0', debug=True, port=int(os.getenv('PORT', 9099)), use_reloader=False, threaded=True)
