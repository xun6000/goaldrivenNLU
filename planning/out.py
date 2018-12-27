# coding=utf-8
import json
import watson_developer_cloud

conversation = watson_developer_cloud.ConversationV1(
    iam_api_key="Wu5glUEuIEvEQnyDk_66YODTZDz9TDeGzm1C2rZng_5I",
    version='2018-07-10'
)
conversation.set_url(
    "https://gateway-syd.watsonplatform.net/assistant/api")
conversation_id = ''


def logg(response):
    print(json.dumps(response, indent=2))


def print_intent(response, list):
    if len(list) > len(response['intents']):
        list = range(0, len(response['intents']))
    for i in list:
        print(response['intents'][i]['intent'] + " " + str(response['intents'][i]['confidence']))


def return_intent(response, list):
    intent_list = []
    if len(list) > len(response['intents']):
        list = range(0, len(response['intents']))
    for i in list:
        intent_list.append(response['intents'][i]['intent'] + " " + str(response['intents'][i]['confidence']))
    return intent_list


def print_entity(response):
    if len(response['entities']) > 0:
        for entity in response['entities']:
            print(entity['entity'] + " " + entity['value'] + " " + str(entity['confidence']))
    else:
        print ('No entity!')


def print_response(response):
    #if response['output']['text'][0] != "":
    print ('[ROBOT]: ' + response['output']['text'][0])


def sent(msg):
    global conversation
    global conversation_id
    if conversation is None:
        conversation = watson_developer_cloud.ConversationV1(
            iam_api_key= "Wu5glUEuIEvEQnyDk_66YODTZDz9TDeGzm1C2rZng_5I",
            version='2018-07-10'
        )
    conversation.set_url("https://gateway-syd.watsonplatform.net/assistant/api")
    response = conversation.message(
        workspace_id='09b80ae8-ae6e-422c-ada5-fdb44e300f44',
        input={
            'text': msg
        },
        alternate_intents=True
    )
    conversation_id = response['context']['conversation_id']
    return response