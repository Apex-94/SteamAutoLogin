import os
import pyautogui
import subprocess
import time
#Point(x=921, y=455)
#Point(x=880, y=488)
filename="F:\steaminst\Steam.exe"# ADD YOUR FILE PATH TO STEAM
#os.system(filename)
subprocess.Popen(filename)
time.sleep(5)
#print(pyautogui.position())
#pyautogui.click(921,455)
#pyautogui.typewrite("ADD UR USERNAME HERE")
steam=pyautogui.locateOnScreen(r'C:\Users\User\Desktop\res\steam.PNG')
#print("User ID is .....")
x=921
y=455
x1=880
y1=488
pyautogui.doubleClick(x,y,button='left')
pyautogui.typewrite("UR USER ID HERE")
time.sleep(5)
print("Password is.....4")
pyautogui.doubleClick(x1,y1,button='left')
pyautogui.typewrite("YOUR PASSWORD HERE")
