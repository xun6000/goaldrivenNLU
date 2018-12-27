li=["greetings sir","hello sir. How are you today","hey dude what is up","hi ma am. what's up?","hello,how are you doing today?","hey girl how is it going"]


#
time =["8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00"]
number=["2","3","4","5","6"]
profile=["male,elderly","male,middle-aged","male,young","female,elderly","female,middle-aged","female,young"]



towrite=[]
todict=[]
for i in range(len(li)):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[i])
            towrite.append("\n")
            for _ in range(4):
                towrite.append(str(_+2)+" start" + "\t"+li[i]+" "+time[k]+" "+number[j]+"\n")

            towrite.append("\n")


            todict.append("1 "+li[i]+" "+time[k]+" "+number[j]+"\n")
#P[0]
for i in range(1):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[0])
            towrite.append("\n")
            towrite.append("2 sayAll" + "\t"+ "i'd like to book a table. We will be " + number[j] + " people at " + time[k] + "\n")

            towrite.append("3 sayAll" + "\t" + "i'd like to book a table. We will be " + number[j] + " people at " + time[k] + "\n")

            towrite.append("4 sayAll" + "\t" + "i'd like to book a table. We will be " + number[j] + " people at " + time[k] + "\n")

            towrite.append("5 sayAll" + "\t" + "i'd like to book a table. We will be " + number[j] + " people at " + time[k] + "\n")
            towrite.append("\n")
#
            if i==0:
                todict.append("1 "+"i'd like to book a table. We will be " + number[j] + " people at " + time[k] + "\n")
#p[1]
for i in range(1):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[1])
            towrite.append("\n")
            towrite.append(
                "2 sayAll" + "\t" + "Hi sir, may I book a table at "+ time[k]+" tomorrow for "+number[j] + " people?" + "\n")

            towrite.append(
                "3 sayAll" + "\t" +  "Hi sir, may I book a table at "+ time[k]+" tomorrow for "+number[j] + " people?" + "\n")

            towrite.append(
                "4 sayAll" + "\t" + "Hi sir, may I book a table at "+ time[k]+" tomorrow for "+number[j] + " people?" + "\n")

            towrite.append(
                "5 sayAll" + "\t" + "Hi sir, may I book a table at "+ time[k]+" tomorrow for "+number[j] + " people?" + "\n")
            towrite.append("\n")

            if i==0:
                todict.append("1 "+"Hi sir, may I book a table at "+ time[k]+" tomorrow for "+number[j] + " people?" + "\n")
for i in range(1):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[2])
            towrite.append("\n")
            towrite.append("2 sayAll" + "\t"+"may i have a table for " + number[j] + " people at " + time[k]+"\n")

            towrite.append("3 sayAll" + "\t" +"may i have a table for " + number[j] + " people at " + time[k] + "\n")

            towrite.append("4 sayAll" + "\t" + "may i have a table for " + number[j] + " people at " + time[k] + "\n")

            towrite.append("5 sayAll" + "\t" + "may i have a table for " + number[j] + " people at " + time[k] + "\n")
            towrite.append("\n")

            if i==0:
                todict.append("1 "+"may i have a table for " + number[j] + " people at " + time[k] + "\n")
#p[3]
for i in range(1):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[3])
            towrite.append("\n")
            towrite.append("2 sayAll" + "\t"+"Hi madam, may I reserve a table at "+ time[k]+" tomorrow for " + number[j] + " people" +"\n")

            towrite.append("3 sayAll" + "\t" +"Hi madam, may I reserve a table at "+ time[k]+" tomorrow for " + number[j] + " people" +"\n")

            towrite.append("4 sayAll" + "\t" + "Hi madam, may I reserve a table at "+ time[k]+" tomorrow for " + number[j] + " people" + "\n")

            towrite.append("5 sayAll" + "\t" + "Hi madam, may I reserve a table at "+ time[k]+" tomorrow for " + number[j] + " people" +"\n")
            towrite.append("\n")

            if i==0:
                todict.append("1 "+"Hi madam, may I reserve a table at "+ time[k]+" tomorrow for " + number[j] + " people" +"\n")
#p[4
for i in range(1):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[4])
            towrite.append("\n")
            towrite.append("2 sayAll" + "\t"+"can you book a table for " + number[j] + " people at " + time[k]+"\n")

            towrite.append("3 sayAll" + "\t" +"can you book a table for " + number[j] + " people at " + time[k] + "\n")

            towrite.append("4 sayAll" + "\t" + "can you book a table for " + number[j] + " people at " + time[k] + "\n")

            towrite.append("5 sayAll" + "\t" + "can you book a table for " + number[j] + " people at " + time[k] + "\n")
            towrite.append("\n")

            if i==0:
                todict.append("1 "+"can you book a table for " + number[j] + " people at " + time[k]+"\n")
#p[5
for i in range(1):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[5])
            towrite.append("\n")
            towrite.append("2 sayAll" + "\t"+"can I book a table for " + number[j] + " people at " + time[k]+"\n")

            towrite.append("3 sayAll" + "\t" +"can I book a table for " + number[j] + " people at " + time[k] + "\n")

            towrite.append("4 sayAll" + "\t" + "can I book a table for " + number[j] + " people at " + time[k] + "\n")

            towrite.append("5 sayAll" + "\t" + "can I book a table for " + number[j] + " people at " + time[k] + "\n")
            towrite.append("\n")

            if i==0:
                todict.append("1 "+"can I book a table for " + number[j] + " people at " + time[k]+"\n")

li=["Okay, that's fine","<silence>","em, okay, I will be here.","Okay, I can wait.","Mhm, it doesn't matter","Mhm, see you in a few minute"]

for i in range(len(li)):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[i])
            towrite.append("\n")
            for _ in range(4):
                towrite.append(str(_+2)+" wait" + "\t"+li[i]+" "+time[k]+" "+number[j]+"\n")

                #towrite.append(str(_ + 2) + " <SILENCE>" + "\t" + li[4] + " fefjiejfie\n")

            # towrite.append("4 <SILENCE>" + "\t" + li[i]+ "\n")
            #
            # towrite.append("5 <SILENCE>" + "\t" + li[i] + "\n")
            towrite.append("\n")


            todict.append("1 "+li[i]+" "+time[k]+" "+number[j]+"\n")
            #todict.append("1 "+li[4]+" fefjiejfie\n")


li=["We don't mind if we can get two seats at the bar","Do you have a bar in your restaurant? We don’t mind if we can get two seats at the bar.","Can we sit at the bar then?","Can I reserve the seats at the bar instead?","Can we get the seats at the bar instead?","Can we sit at the bar?"]




for i in range(len(li)):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[i])
            towrite.append("\n")
            for _ in range(4):
                towrite.append(str(_+2)+" sitAtBar" + "\t"+li[i]+" "+time[k]+" "+number[j]+"\n")

                #towrite.append(str(_ + 2) + " <SILENCE>" + "\t" + li[4] + " fefjiejfie\n")

            # towrite.append("4 <SILENCE>" + "\t" + li[i]+ "\n")
            #
            # towrite.append("5 <SILENCE>" + "\t" + li[i] + "\n")
            towrite.append("\n")


            todict.append("1 "+li[i]+" "+time[k]+" "+number[j]+"\n")
            #todict.append("1 "+li[4]+" fefjiejfie\n")

li=["May we have two smaller tables together?","Can we have two smaller tables together?","What if we have two smaller tables combined?","I’m wondering if it is possible to combine two tables for us.","Can we have two smaller tables combined?","can we put two tables together"]


for i in range(len(li)):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[i])
            towrite.append("\n")
            for _ in range(4):
                towrite.append(str(_+2)+" combineTables" + "\t"+li[i]+" "+time[k]+" "+number[j]+"\n")

                #towrite.append(str(_ + 2) + " <SILENCE>" + "\t" + li[4] + " fefjiejfie\n")

            # towrite.append("4 <SILENCE>" + "\t" + li[i]+ "\n")
            #
            # towrite.append("5 <SILENCE>" + "\t" + li[i] + "\n")
            towrite.append("\n")


            todict.append("1 "+li[i]+" "+time[k]+" "+number[j]+"\n")
li=["Thank you. Would you mind calling me back if there are suitable tables?","Okay. Could you call me back if you have suitable tables later?","Okay, thanks. Can you call me back once there is an available table?","Okay, thank you all the same. Would you mind calling me back if suitable tables come up later?","Okay, thank you. Let me know","Thanks, I will wait for your good news"]

for i in range(len(li)):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[i])
            towrite.append("\n")
            for _ in range(4):
                towrite.append(str(_+2)+" changeRestaurant" + "\t"+li[i]+" "+time[k]+" "+number[j]+"\n")

                #towrite.append(str(_ + 2) + " <SILENCE>" + "\t" + li[4] + " fefjiejfie\n")

            # towrite.append("4 <SILENCE>" + "\t" + li[i]+ "\n")
            #
            # towrite.append("5 <SILENCE>" + "\t" + li[i] + "\n")
            towrite.append("\n")


            todict.append("1 "+li[i]+" "+time[k]+" "+number[j]+"\n")
            #todict.append("1 "+li[4]+" fefjiejfie\n")

li=["Would you mind telling me other times that are available?","I see, what's your opening hour?","What are the available times now?","What is the best time?","do you know when is the good time? ","Can you tell me what the available times are?"]
#li=["Thank you. Would you mind calling me back if there are suitable tables?","Okay. Could you call me back if you have suitable tables later?","Okay, thanks. Can you call me back once there is an available table?","Thank you. Would you mind calling me back if suitable tables come up later?","Okay, thank you. Let me know","Thanks, I will wait for your good news"]

for i in range(len(li)):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[i])
            towrite.append("\n")
            for _ in range(4):
                towrite.append(str(_+2)+" changeTime" + "\t"+li[i]+" "+time[k]+" "+number[j]+"\n")

                #towrite.append(str(_ + 2) + " <SILENCE>" + "\t" + li[4] + " fefjiejfie\n")

            # towrite.append("4 <SILENCE>" + "\t" + li[i]+ "\n")
            #
            # towrite.append("5 <SILENCE>" + "\t" + li[i] + "\n")
            towrite.append("\n")


            todict.append("1 "+li[i]+" "+time[k]+" "+number[j]+"\n")
            #todict.append("1 "+li[4]+" fefjiejfie\n")

li=["Understood. I'll call back later. Goodbye","Thanks. If anything changes, I will call you back.","Gotcha. I'll call back later. Bye","Okay, thank you","Thank you, have a good one","Have a nice day"]
#li=["Would you mind telling me other times that are available?","Could you tell me available times?","What are the available times now?","What is the best time?","do you know when is the good time? ","Can you tell me what the available times are?"]
#li=["Thank you. Would you mind calling me back if there are suitable tables?","Okay. Could you call me back if you have suitable tables later?","Okay, thanks. Can you call me back once there is an available table?","Thank you. Would you mind calling me back if suitable tables come up later?","Okay, thank you. Let me know","Thanks, I will wait for your good news"]

for i in range(len(li)):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[i])
            towrite.append("\n")
            for _ in range(4):
                towrite.append(str(_+2)+" callBackLater" + "\t"+li[i]+" "+time[k]+" "+number[j]+"\n")

                #towrite.append(str(_ + 2) + " <SILENCE>" + "\t" + li[4] + " fefjiejfie\n")

            # towrite.append("4 <SILENCE>" + "\t" + li[i]+ "\n")
            #
            # towrite.append("5 <SILENCE>" + "\t" + li[i] + "\n")
            towrite.append("\n")


            todict.append("1 "+li[i]+" "+time[k]+" "+number[j]+"\n")
            #todict.append("1 "+li[4]+" fefjiejfie\n")
li=["That's great, thank you very much.","OK, thank you very much.","Awesome, thanks man.","Okay, thank you for your time.","That's great, thank you","That's great, thank you very much"]
#li=["Would you mind telling me other times that are available?","Could you tell me available times?","What are the available times now?","What is the best time?","do you know when is the good time? ","Can you tell me what the available times are?"]
#li=["Thank you. Would you mind calling me back if there are suitable tables?","Okay. Could you call me back if you have suitable tables later?","Okay, thanks. Can you call me back once there is an available table?","Thank you. Would you mind calling me back if suitable tables come up later?","Okay, thank you. Let me know","Thanks, I will wait for your good news"]


for i in range(len(li)):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[i])
            towrite.append("\n")
            for _ in range(4):
                towrite.append(str(_+2)+" sayThanks" + "\t"+li[i]+" "+time[k]+" "+number[j]+"\n")

                #towrite.append(str(_ + 2) + " <SILENCE>" + "\t" + li[4] + " fefjiejfie\n")

            # towrite.append("4 <SILENCE>" + "\t" + li[i]+ "\n")
            #
            # towrite.append("5 <SILENCE>" + "\t" + li[i] + "\n")
            towrite.append("\n")


            todict.append("1 "+li[i]+" "+time[k]+" "+number[j]+"\n")
            #todict.append("1 "+li[4]+" fefjiejfie\n")

li=["Could you tell me the reason?","May I know the reason?","Can you tell me the reason?","I'm wondering if you could tell me the reason","May I know what the reason is?","Could you tell me why"]
#li=["Would you mind telling me other times that are available?","Could you tell me available times?","What are the available times now?","What is the best time?","do you know when is the good time? ","Can you tell me what the available times are?"]
#li=["Thank you. Would you mind calling me back if there are suitable tables?","Okay. Could you call me back if you have suitable tables later?","Okay, thanks. Can you call me back once there is an available table?","Thank you. Would you mind calling me back if suitable tables come up later?","Okay, thank you. Let me know","Thanks, I will wait for your good news"]

for i in range(len(li)):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[i])
            towrite.append("\n")
            for _ in range(4):
                towrite.append(str(_+2)+" askForReason" + "\t"+li[i]+" "+time[k]+" "+number[j]+"\n")

                #towrite.append(str(_ + 2) + " <SILENCE>" + "\t" + li[4] + " fefjiejfie\n")

            # towrite.append("4 <SILENCE>" + "\t" + li[i]+ "\n")
            #
            # towrite.append("5 <SILENCE>" + "\t" + li[i] + "\n")
            towrite.append("\n")


            todict.append("1 "+li[i]+" "+time[k]+" "+number[j]+"\n")

li=["I'm wondering if we can have a bigger table.","In this case, can I reserve a bigger table?","Can we have a bigger table then?","Could you give us a big table?","May I take a bigger table?","May I reserve the bigger table?"]
#li=["Would you mind telling me other times that are available?","Could you tell me available times?","What are the available times now?","What is the best time?","do you know when is the good time? ","Can you tell me what the available times are?"]
#li=["Thank you. Would you mind calling me back if there are suitable tables?","Okay. Could you call me back if you have suitable tables later?","Okay, thanks. Can you call me back once there is an available table?","Thank you. Would you mind calling me back if suitable tables come up later?","Okay, thank you. Let me know","Thanks, I will wait for your good news"]

for i in range(len(li)):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[i])
            towrite.append("\n")
            for _ in range(4):
                towrite.append(str(_+2)+" askForBiggerTable" + "\t"+li[i]+" "+time[k]+" "+number[j]+"\n")

                #towrite.append(str(_ + 2) + " <SILENCE>" + "\t" + li[4] + " fefjiejfie\n")

            # towrite.append("4 <SILENCE>" + "\t" + li[i]+ "\n")
            #
            # towrite.append("5 <SILENCE>" + "\t" + li[i] + "\n")
            towrite.append("\n")


            todict.append("1 "+li[i]+" "+time[k]+" "+number[j]+"\n")
            #todict.append("1 "+li[4]+" fefjiejfie\n")

li=["I'm wondering if there are any alternatives. Your restaurant is fantastic and we really want to go.","Are there alternatives? Your restaurant is the best in the region and we really want to go.","Are there any alternatives? We really would like to go to your restaurant.","Do you have tables outside? Maybe we can sit in the open air. ","Do you know how to solve this problem","Could you help us to solve this problem"]

for i in range(len(li)):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[i])
            towrite.append("\n")
            for _ in range(4):
                towrite.append(str(_+2)+" askForAlternatives" + "\t"+li[i]+" "+time[k]+" "+number[j]+"\n")


            towrite.append("\n")


            todict.append("1 "+li[i]+" "+time[k]+" "+number[j]+"\n")

li=["How about tables for 2 people?","May I know if there are tables for 2?","Are tables for 2 available?","How about tables for 2?","Are there tables for 2 people?","Are there tables for two available?"]

for i in range(len(li)):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[i])
            towrite.append("\n")
            for _ in range(4):
                towrite.append(str(_+2)+" tableFor2" + "\t"+li[i]+" "+time[k]+" "+number[j]+"\n")


            towrite.append("\n")


            todict.append("1 "+li[i]+" "+time[k]+" "+number[j]+"\n")



li=["Can I make a reservation for that time for now? I will call back if anything changes.","Can we tentatively reserve a table at that time for now?  We just need to double check with the time."," Is it okay if I book a table at that time for now? I need to double-check.","May I reserve a table at that time? I will check that with others."," I want to reserve a table for that time. I will check that with others.","Can I tentatively book a table for now? I need to double-check on time."]
for i in range(len(li)):
    for k in range(len(time)):
        for j in range(len(number)):
            towrite.append("1 "+number[j]+","+time[k]+","+ profile[i])
            towrite.append("\n")
            for _ in range(4):
                towrite.append(str(_+2)+" tentativelyReserve" + "\t"+li[i]+" "+time[k]+" "+number[j]+"\n")


            towrite.append("\n")


            todict.append("1 "+li[i]+" "+time[k]+" "+number[j]+"\n")










f=open("../data/personalized-dialog-dataset/full/personalized-dialog-task1-API-calls-dev.txt","w")
f.writelines(towrite)
f.close()
f=open("../data/personalized-dialog-dataset/full/personalized-dialog-task1-API-calls-trn.txt","w")
f.writelines(towrite)
f.close()
f=open("../data/personalized-dialog-dataset/full/personalized-dialog-task1-API-calls-tst.txt","w")
f.writelines(towrite)
f.close()
f=open("../data/personalized-dialog-dataset/full/personalized-dialog-task1-API-calls-tst-OOV.txt","w")
f.writelines(towrite)
f.close()
f=open("../data/personalized-dialog-dataset/personalized-dialog-candidates.txt","w")
f.writelines(todict)
f.close()