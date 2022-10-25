#! python3
# Zoom - Module for joining zoom

import os
import pyautogui as gui
import subprocess as sub
import time


#Function to log in zoom
def signin(id):
    print('DO NOT click anywhere while joining class.')
    #Checking os
    current_dir=os.getcwd()
    if(current_dir[0] == '/'):
        operating_system='l'
        print('Linux Detected:')
        sub.Popen(['/opt/zoom/ZoomLauncher'])       #Runs Zoom
    else:
        #Find and launch zoom on windows
        operating_system='w'
        print('Windows Detected:')
        machineName=''                             #Change this to the name of your computer
        sub.Popen([rf'C:\Users\{machineName}\AppData\Roaming\Zoom\bin\Zoom.exe'])

    #Time breaks to wait for app to run
    time.sleep(30)

    #Clicking the class join button
    gui.moveTo(1028,468,2)
    gui.click()

    time.sleep(1)

    #Clicking and writing meeting id
    gui.click()
    gui.write(id)

    #Join
    gui.moveTo(1019,669,2)
    gui.click()

    #Take some Time to join then minimize
    time.sleep(20)
    gui.moveTo(1470, 113,1)
    gui.click()

    #Passcode and join                                  #Commenting it out as pw is not required
    # pass_btn=gui.locateCenterOnScreen('passcode.png')
    # gui.moveTo(pass_btn)
    # gui.click()
    # gui.write(pw)
    # gui.press('enter')

    time.sleep(14)
    print('Joined',chr(64),chr(45),chr(64),'\n\n\n')

    
    #Closing once Class ends ------ Time : 40mins, Deducting due to previous time.sleeps
    time.sleep(2310)
    if(operating_system=='l'):
        sub.run(['killall','zoom'])        #Killing any previous instances of Zoom before reopening
    else:
        sub.run(['taskkill','/im','zoom.exe','/f'])     #Kills zoom in windows
