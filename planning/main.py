# coding=utf-8

import out
from WorldModel import WorldModel
from planner1 import problem1
import json
import urllib.request
import variables


def plan(message, input_info):
    size, time, sex, age, name, restaurants = input_info

    model = WorldModel()

    model.robotSlot.size = size
    model.robotSlot.time = time

    # ---------------------
    number = size

    for num in variables.numbers:
        if num in message and "pm" not in message and ":" not in message and num != size:
            number = variables.numbers_dict[num]
            break

    # ---------------------
    if "?" in message:
        message_list = message.split('.')
        message = message_list[len(message_list)-1]

    if message == "Start" or message == "start":
        initializeVar()
        variables.counter = 0
        variables.restaurant = restaurants[variables.counter]
        variables.counter = variables.counter + 1
    elif variables.position == "Close (Goal)":
        initializeVar()
        variables.counter = 0
        variables.response = "You have reached the end of the last conversation. Please start a new one."
        return
    elif variables.situation == []:
        res = out.sent(message)
        variables.intent_list = out.return_intent(res, range(0, 2))
        print(variables.intent_list)
        model.analyzer(res, number)
    else:
        initializeVar()
        variables.restaurant = restaurants[variables.counter]
        variables.counter = variables.counter + 1
    # else:
    #     variables.response = "This is the end of the conversation."
    #     variables.position = "Close (Goal)"
    #     variables.flowchart_history.append(variables.position)
    #     variables.counter = 0
    #     initializeVar()
    #     return

    plan, variables.init = problem1(model)

    if plan is None:
        variables.action_list = []
        print("No Plan!")
        return
    else:
        variables.action_list = []
        for i in range(len(plan)):
            variables.action_list.append(plan[i].__str__())
        print(variables.action_list)

    if plan[0].__str__() == "start()":  # done
        variables.response = "Ringing " + variables.restaurant
        variables.position = variables.flow_dict["start"]
        variables.flowchart_history.append(variables.position)

    elif plan[0].__str__() == "opening()":
        requestResponse(model, "sayAll", sex, age)
        model.humanSlot.time = model.robotSlot.time
        model.humanSlot.size = model.robotSlot.size

    elif plan[0].__str__() == "tableFor2()":
        requestResponse(model, "tableFor2", sex, age)

    elif plan[0].__str__() == "combineTables()":
        requestResponse(model, "combineTables", sex, age)
        variables.combineTables = True

    elif plan[0].__str__() == "tentativelyReserve()":
        requestResponse(model, "tentativelyReserve", sex, age)
        variables.newTime = variables.newTime + " " + message

    elif plan[0].__str__() == "changeTime()":
        requestResponse(model, "changeTime", sex, age)
        variables.changeTime = True
        variables.newTime = message

    elif plan[0].__str__() == "askForReason()":
        requestResponse(model, "askForReason", sex, age)

    elif plan[0].__str__() == "askForBiggerTable()":
        requestResponse(model, "askForBiggerTable", sex, age)
        variables.biggerTable = True

    elif plan[0].__str__() == "sitAtBar()":
        requestResponse(model, "sitAtBar", sex, age)
        variables.bar = True

    elif plan[0].__str__() == "askForAlternatives()":
        requestResponse(model, "askForAlternatives", sex, age)

    elif plan[0].__str__() == "wait()":
        variables.response = "Hmm"
        variables.position = variables.flowchart_history[len(variables.flowchart_history) - 1]
        variables.flowchart_history.append(variables.position)

    elif plan[0].__str__() == "sayName()":
        variables.response = "My name is " + name
        variables.position = variables.flow_dict["sayName"]
        variables.flowchart_history.append(variables.position)

    elif plan[0].__str__() == "sayThanks()":
        requestResponse(model, "sayThanks", sex, age)
        variables.success = True

    elif plan[0].__str__() == "callBackLater()":
        requestResponse(model, "callBackLater", sex, age)

    elif plan[0].__str__() == "changeRestaurant()":
        requestResponse(model, "changeRestaurant", sex, age)
        variables.changeRestaurant = True

    elif plan[0].__str__() == "doubleConfirm()":  # done
        variables.response = "Is it all set?"
        variables.position = variables.flow_dict["doubleConfirm"]
        variables.flowchart_history.append(variables.position)

    elif plan[0].__str__() == "close()":
        situation(size)
        if variables.situation == []:
            variables.response = "Bye. "
        else:
            variables.response = "Bye. " + variables.situation[0]


def requestResponse(model, action, sex, age):
    req = urllib.request.Request('http://127.0.0.1:9000')
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    body = {"slot": [str(model.robotSlot.size), model.robotSlot.time], "Action": action, "profile": [sex, age]}
    print(body)
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)
    data = json.loads(response.read().decode('utf-8'))
    variables.response = data['response']
    if variables.flow_dict[action] == "":
        variables.position = variables.flowchart_history[len(variables.flowchart_history) - 1]
    else:
        variables.position = variables.flow_dict[action]
    variables.flowchart_history.append(variables.position)


def initializeVar():
    variables.failure1 = False
    variables.combineTables = False
    variables.changeTime = False
    variables.biggerTable = False
    variables.bar = False
    variables.changeRestaurant = False
    variables.newTime = ""
    variables.flowchart_history = []
    variables.situation = []
    if variables.counter == 0:
        variables.flow_dict["sayName"] = "Divergence Resolution"
    else:
        variables.flow_dict["sayName"] = "Alternative Solution"


def situation(size):
    if not variables.success:
        if variables.changeTime:
            variables.situation.append(
                "The person at the restaurant said: \"" + variables.newTime + "\" I have reserved a "
                "table for " + str(size) + " when they are open. [User Confirmation]")
            variables.position = "User Confirmation"
            variables.flowchart_history.append(variables.position)
        elif variables.changeRestaurant or variables.failure1:
            variables.situation.append("First attempt has failed. The restaurant will call you "
                                       "if there is a table available, but I could call another restaurant now. "
                                       "Shall I proceed?")
            variables.position = "Attempt"
            variables.flowchart_history.append(variables.position)
        elif variables.combineTables:
            variables.situation.append("I have successfully booked a combined table for you.")
            variables.position = variables.flow_dict["close"]
            variables.flowchart_history.append(variables.position)
        elif variables.biggerTable:
            variables.situation.append("I have successfully booked a bigger table for you.")
            variables.position = variables.flow_dict["close"]
            variables.flowchart_history.append(variables.position)
        elif variables.bar:
            variables.situation.append("I have successfully booked " + str(size) +
                                       " seats at the bar for you.")
            variables.position = variables.flow_dict["close"]
            variables.flowchart_history.append(variables.position)
    else:
        variables.position = variables.flow_dict["close"]
        variables.flowchart_history.append(variables.position)