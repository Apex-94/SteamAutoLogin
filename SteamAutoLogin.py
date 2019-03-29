import os
import pyautogui
import subprocess
import time
import sys
import json
import psutil
"""TODO
1st key is for non steam guard 2nd key is for steam guard
1.Exceptions for Steam_guard
1.1 Adding better time.sleep() optimization
1.2 Creating different functions for easy access 
2.Poping out Steam_guard code from .txt file after using the top most code as the once used it expires
3.Multi accounts currently running only 2 accounts using if and else statement
4.Storing Accounts in json format and reading data from it(Encryption if required)
5.Building an executable file
"""
for pid in psutil.pids():
    p = psutil.Process(pid)
    if p.name() == "Steam.exe":
        flag=False

if (flag==False):
    print("Steam is already running")
    time.sleep(3)
    sys.exit()
else:
    pyautogui.FAILSAFE = True
    #Point(x=921, y=455)
    #Point(x=880, y=488)
    accoutfile=open('Account_info.json')
    data=json.load(accoutfile)
    dic=data
    accoutfile.close
    print(dic)
    print(type(dic))
    filename="F:\steaminst\Steam.exe"
    #os.system(filename)
    print('Launching Steam.exe')
    #print(pyautogui.position())
    #pyautogui.click(921,455)
    #pyautogui.typewrite("apex_94")
    time.sleep(1)
    print("Choose '1' for Account :Apex_94")
    print("Choose '2' for Account :Apex__94")
    try:
        input_id=int(input())
    except ValueError:
        print("Enter valid option:")
    else:
        if(input_id==1):
            steam = subprocess.Popen(filename)
            steam1 = pyautogui.locateOnScreen(r'C:\Users\User\Desktop\res\steam.PNG')
            print("Loading info")
            time.sleep(2)
            x=921
            y=455
            x1=880
            y1=488
            Loggin_id=dic.get("1")[0]
            Loggin_pass=dic.get("1")[1]
            time.sleep(2)
            print("entering username")
            pyautogui.doubleClick(x,y,button='left')
            pyautogui.typewrite(Loggin_id)
            time.sleep(1)
            print("entering password")
            pyautogui.doubleClick(x1,y1,button='left')
            pyautogui.typewrite(Loggin_pass)
            print("Sucessfully logged in .....")
            pyautogui.press('enter')
        else:
            steam = subprocess.Popen(filename)
            steam1 = pyautogui.locateOnScreen(r'C:\Users\User\Desktop\res\steam.PNG')
            print("Loading info")
            time.sleep(2)
            x = 921
            y = 455
            x1 = 880
            y1 = 488
            Loggin_id = dic.get("2")[0]
            Loggin_pass = dic.get("2")[1]
            time.sleep(2)
            print("entering username")
            pyautogui.doubleClick(x, y, button='left')
            pyautogui.typewrite(Loggin_id)
            time.sleep(1)
            print("entering password")
            pyautogui.doubleClick(x1, y1, button='left')
            pyautogui.typewrite(Loggin_pass)
            print("Sucessfully logged in .....")
            pyautogui.press('enter')
            steam_guardflag = pyautogui.locateOnScreen(r'C:\Users\User\Desktop\steamguard.PNG')
            print("Entering Steam Guard info")
            time.sleep(2)
            print('Searching for any available backup codes in PC..')
            time.sleep(2)
            try:

                x2, y2 = 1063, 576
                steamguardcodes =r'C:\Users\User\\Desktop\steamcodes.txt'
                with open(steamguardcodes, 'r') as f:
                    list = []
                    print("Opening steamguard codes......")
                    time.sleep(2)
                    for line in f:
                        code = line.split('\n')
                        list.append(code[0])
                    use_code = list[0]
                    pyautogui.click(x2, y2, clicks=2, button='left')
                    pyautogui.typewrite(use_code)
                    pyautogui.press('enter')
                    list.pop()
                    print("Logging using steam guard code is compleated")
            except FileNotFoundError:
                print("File not Found")
