#! python3
#Time Reader - To check the times in the csv file and join classes accordingly

import csv
from datetime import datetime as dt
from zoom import signin

#Opening and assigning variables to the time col
fileopen=open('timings4.csv')        #Remember to update the timings Number everyday    #1-Monday
fileread=csv.reader(fileopen)                                                           #2-Tuesday....4-Thursday            
filedata=list(fileread)

#A list to hold all the timings
time_to_join=[]

#Loop to get timings list
for i in range(1,len(filedata)):
    extime=filedata[i][0]
    time=extime[0:5]
    time_to_join.append(time)


#A List to hold the number of classes
classNo=[]      
for i in range(1,len(filedata)):
    classNo.append(filedata[i][2])

maxClasses=len(classNo)

#Gets the Week Day for a brief info
weekDay = dt.today().strftime('%A')

#A counter variable to change as per class
classCounter=0

#Simple Function to print some info after joining class
def info():
    global classCounter
    global maxClasses
    if(classCounter>=maxClasses):
        return 'All Classes Done'
    if(classCounter):
        print(f'Joining Class {classNo[classCounter]} of {weekDay}')
        classCounter+=1
    else:
        print(f'Joining Class {classNo[classCounter]} of {weekDay}')
        classCounter=1
    return
    

#A function to define id and password also calls the signin function from zoom.py   
def func():
    for i in range(0,6):    
        if(now==time_to_join[i]):
            row=i+1
            meet_id=filedata[row][1]
            # meet_pw=filedata[row][2]
            break
    signin(meet_id)

#Closing the file as it's no longer needed
fileopen.close()

#Main execution block
try:
    while True:
        now = dt.now().strftime("%H:%M")
        #Only calls the function if time matches
        if(now in time_to_join):
            info()
            func()
        else:
            continue
except KeyboardInterrupt:
    print(" Stopping...")