#Author Shushant Ghosh
#This program is for taking quiz
#Data is provided from json file
import json
data = json.load(open('quiz_data.json'))           #Loading file from json file
print("Choose one among the following options")
for name in data['quiz']:                          #Distunguishing different groups in quiz
    print(name)
ch=input("")
flag=0
res=[]                                             #To store User returned values
try:                                               #So that the program doesnot close abruptly
    for q in data['quiz'][ch]:
        print(q, ":")
        print(data['quiz'][ch][q]['question'])
        for o in data['quiz'][ch][q]['options']:
            print(o)
        sp = input("Your Answer : ")
        res.append(sp)                                      #user replies is/are appended in the list
        for o in data['quiz'][ch][q]['options']:
            if sp==o:
                  flag=1
        if flag==0:
            try:
                raise ValueError("Incorrect option")
            except:
                print("Enter correct option")
    print("*************************QUIZ RESULT***********************\nUser Answered\n",res)                            #
    for answers in data['quiz'][ch]:
        print(answers, " Correct Answer is ", data['quiz'][ch][answers]['answer'])
except:                                                                    # print if exception is present
    print("Enter values among the above options only in string form")