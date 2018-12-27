import variables


class Slot:
    size = 0
    time = ""

    def __init__(self):
        self.size = 0
        self.time = ""


class Dialog:
    status = 0.0

    def __init__(self):
        self.status = 0


class WorldModel:

    robotSlot = Slot()
    humanSlot = Slot()
    dialog = Dialog()

    def __init__(self):
        self.robotSlot = Slot()
        self.humanSlot = Slot()
        self.dialog = Dialog()

    def reset(self):
        self.robotSlot.__init__()
        self.humanSlot.__init__()
        self.dialog.__init__()

    def analyzer(self, response, number):
        THRESHOLD = 0.28
        print(response['intents'])
        if response['intents'][0]['intent'] == 'greeting':
            self.dialog.status = 1
        elif response['intents'][0]['intent'] == 'askSize' and response['intents'][0]['confidence'] > THRESHOLD:
            self.humanSlot.size = 0
            self.humanSlot.time = self.robotSlot.time
            self.dialog.status = 2
        elif response['intents'][0]['intent'] == 'askTime' and response['intents'][0]['confidence'] > THRESHOLD:
            self.humanSlot.time = ''
            self.humanSlot.size = self.robotSlot.size
            self.dialog.status = 2
        elif response['intents'][0]['intent'] == 'search' and response['intents'][0]['confidence'] > THRESHOLD:
            self.humanSlot.size = self.robotSlot.size
            self.humanSlot.time = self.robotSlot.time
            self.dialog.status = 3
        elif response['intents'][0]['intent'] == 'timeIssue' and response['intents'][0]['confidence'] > THRESHOLD:
            self.dialog.status = 4
            self.humanSlot.size = self.robotSlot.size
            self.humanSlot.time = ''
        elif response['intents'][0]['intent'] == 'success' and response['intents'][0]['confidence'] > THRESHOLD:
            if variables.changeTime:
                self.dialog.status = 7
            else: #variables.confirm == True or variables.failure1 == True:
                self.dialog.status = 5
            # else:
            #     variables.confirm = True
            #     self.dialog.status = 5.2
            self.humanSlot.size = self.robotSlot.size
            self.humanSlot.time = self.robotSlot.time
        elif response['intents'][0]['intent'] == 'needConfirmation' and response['intents'][0]['confidence'] > THRESHOLD:
            # if variables.confirm == False:
            #     self.dialog.status = 5.2
            #     variables.confirm = True
            # else:
            self.dialog.status = 5
            self.humanSlot.size = self.robotSlot.size
            self.humanSlot.time = self.robotSlot.time
        elif response['intents'][0]['intent'] == 'askName' and response['intents'][0]['confidence'] > THRESHOLD:
            self.dialog.status = 4.9
            self.humanSlot.size = self.robotSlot.size
            self.humanSlot.time = self.robotSlot.time
        elif response['intents'][0]['intent'] == 'failure' and response['intents'][0]['confidence'] > THRESHOLD and variables.failure1 == False:
            variables.failure1 = True
            self.dialog.status = 6.1
            self.humanSlot.size = self.robotSlot.size
            self.humanSlot.time = self.robotSlot.time
        elif response['intents'][0]['intent'] == 'failure' and response['intents'][0]['confidence'] > THRESHOLD and variables.failure1 == True:
            self.dialog.status = 6
            self.humanSlot.size = self.robotSlot.size
            self.humanSlot.time = self.robotSlot.time
        elif response['intents'][0]['intent'] == 'timeResponse' and response['intents'][0]['confidence'] > THRESHOLD:
            self.dialog.status = 5.1
            self.humanSlot.size = self.robotSlot.size
            self.humanSlot.time = self.robotSlot.time
        elif response['intents'][0]['intent'] == 'confusing' and response['intents'][0]['confidence'] > THRESHOLD:
            if self.robotSlot.size == 2:
                self.dialog.status = 4.12  # change!!!
                self.humanSlot.time = self.robotSlot.time
                self.humanSlot.size = 0
            elif number > self.robotSlot.size:
                self.dialog.status = 4.1
                self.humanSlot.time = self.robotSlot.time
                self.humanSlot.size = 0
            elif number == 4:
                self.dialog.status = 4.2
                self.humanSlot.time = self.robotSlot.time
                self.humanSlot.size = 0
            elif number < self.robotSlot.size:
                self.dialog.status = 4
                self.humanSlot.time = self.robotSlot.time
                self.humanSlot.size = 0
            else:
                self.dialog.status = 1.1
                self.humanSlot.size = 0
                self.humanSlot.time = ''
        elif response['intents'][0]['intent'] == 'delivery' and response['intents'][0]['confidence'] > THRESHOLD:
            self.dialog.status = 6
            self.humanSlot.size = self.robotSlot.size
            self.humanSlot.time = self.robotSlot.time
        elif response['intents'][0]['intent'] == 'noNeedForReservation' and response['intents'][0]['confidence'] > THRESHOLD: #ask we need at least how many people for a reservation
            self.dialog.status = 5
            self.humanSlot.time = self.robotSlot.time
            self.humanSlot.size = self.robotSlot.size
        elif response['intents'][0]['intent'] == 'barSeats' and response['intents'][0]['confidence'] > THRESHOLD: #done #after bigger table
            self.dialog.status = 4.12
            self.humanSlot.time = self.robotSlot.time
            self.humanSlot.size = 0
        elif response['intents'][0]['intent'] == 'notOpen' and response['intents'][0]['confidence'] > THRESHOLD:
            self.dialog.status = 4
            self.humanSlot.size = self.robotSlot.size
            self.humanSlot.time = ''
        elif response['intents'][0]['intent'] == 'fullyBooked' and response['intents'][0]['confidence'] > THRESHOLD: #how to solve multiple times? #answer
            self.dialog.status = 9
            self.humanSlot.time = self.robotSlot.time
            self.humanSlot.size = self.robotSlot.size
        elif response['intents'][0]['intent'] == 'bye' and response['intents'][0]['confidence'] > THRESHOLD:
            self.dialog.status = 8
            self.humanSlot.time = self.robotSlot.time
            self.humanSlot.size = self.robotSlot.size
        elif number > self.robotSlot.size:
            self.dialog.status = 4.1
            self.humanSlot.time = self.robotSlot.time
            self.humanSlot.size = 0
        elif number < self.robotSlot.size:
            self.dialog.status = 4
            self.humanSlot.time = self.robotSlot.time
            self.humanSlot.size = 0
        elif response['intents'][0]['intent'] == 'haveBiggerTable' and response['intents'][0]['confidence'] > THRESHOLD:
            self.dialog.status = 4.1
            self.humanSlot.time = self.robotSlot.time
            self.humanSlot.size = 0
        elif response['intents'][0]['intent'] == 'haveSmallerTable' and response['intents'][0]['confidence'] > THRESHOLD:
            self.dialog.status = 4
            self.humanSlot.time = self.robotSlot.time
            self.humanSlot.size = 0