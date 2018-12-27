input_text = ""
input_info = []
response = ""
flowchart_history = []
position = ""
action_list = []
intent_list = []
init = []
situation = []
restaurant = ""
counter = 0

# confirm = False
failure1 = False
combineTables = False
changeTime = False
biggerTable = False
bar = False
changeRestaurant = False
success = False
newTime = ""
numbers = ["2", "4", "6", "8", "two", "four", "six", "eight"]
numbers_dict = {"2": 2, "two": 2, "4": 4, "four": 4, "6": 6, "six": 6, "8": 8, "eight": 8}

flow_dict = {"start": "Attempt", "sayAll": "Attempt", "combineTables": "Negotiation", "changeTime": "Negotiation",
             "askForReason": "Divergence Classification", "askForBiggerTable": "Negotiation", "sitAtBar": "Negotiation",
             "askForAlternatives": "Negotiation", "wait": "", "sayThanks":
             "", "callBackLater": "", "changeRestaurant": "Failure", "close": "Close (Goal)",
             "tableFor2": "Negotiation", "tentativelyReserve": "Alternative Solution", "doubleConfirm": "Divergence Resolution"}

