
import csv
class data_generater():
    def __init__(self):
        time =["8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00"]
        number=["2","3","4","5","6"]
        profile=[]


        towrite=[]
        todict=[]
        with open('Workbook1.csv', 'r') as csv_file:
            
            all_lines = csv.reader(csv_file)
            ii=0
            for one_line in all_lines:
                if ii==0:
                    profile = one_line[1:]
                    #print(str(profile))
                    ii+=1
                else:
                    li=one_line[1:]
                    if one_line[0]!="sayAll":
                        for i in range(len(li)):
                            for k in range(len(time)):
                                for j in range(len(number)):
                                    towrite.append("1 " + number[j] + "," + time[k] + "," + profile[i]+"\n")

                                    for _ in range(4):
                                        towrite.append(
                                            str(_ + 2) + " "+one_line[0] + "\t" + li[i] + " " + time[k] + " " + number[j] + "\n")

                                    towrite.append("\n")

                                    todict.append("1 " + li[i] + " " + time[k] + " " + number[j] + "\n")
                    else:
                        for i in range(len(profile)):
                            for k in range(len(time)):
                                for j in range(len(number)):
                                    towrite.append("1 " + number[j] + "," + time[k] + "," + profile[i]+"\n")

                                    towrite.append("2 sayAll" + "\t" + li[i][:-1]+" " + number[
                                        j] + " people at " + time[k] + li[i][-1]+"\n")

                                    towrite.append("3 sayAll" + "\t" + li[i][:-1]+" " + number[
                                        j] + " people at " + time[k] + li[i][-1]+"\n")

                                    towrite.append("4 sayAll" + "\t" + li[i][:-1]+" " + number[
                                        j] + " people at " + time[k] + li[i][-1]+"\n")

                                    towrite.append("5 sayAll" + "\t" + li[i][:-1]+" " + number[
                                        j] + " people at " + time[k] + li[i][-1]+"\n")
                                    towrite.append("\n")
                                    #

                                    todict.append(
                                            "1 " + li[i][:-1]+" " + number[j] + " people at " + time[
                                                k] + li[i][-1]+"\n")


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