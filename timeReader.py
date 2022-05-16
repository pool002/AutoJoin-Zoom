#! python3
#Time Reader - To check the times in the csv file and join classes accordingly

import csv
from datetime import datetime as dt
from zoom import signin

#Opening and assigning variables to the time col
day=1          #Remember to update the timings Number everyday  #1-Monday #2-Tuesday....4-Thursday            
fileopen=open(f'timings{day}.csv')
fileread=csv.reader(fileopen)
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

#A function to show the current day selected in case of wrong timings file
def showDay():
    global day
    if(day==1):
        print(f'\nFollowing classes for Monday')
    if(day==2):
        print(f'\nFollowing classes for Tuesday')
    if(day==3):
        print(f'\nFollowing classes for Wednesday')
    if(day==4):
        print(f'\nFollowing classes for Thursday')


#Simple Function to print some info after joining class
def classNoInfo():
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
def callSignIn():
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
    showDay()
    while True:
        now = dt.now().strftime("%H:%M")
        #Only calls the function if time matches
        if(now in time_to_join):
            classNoInfo()
            callSignIn()
        else:
            continue
except KeyboardInterrupt:
    print(" Stopping...")
