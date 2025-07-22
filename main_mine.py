import subprocess
import time
import os
import numpy as np
try:
    import pyautogui
except ImportError:
    subprocess.call(['pip install pyautogui'], stdout=subprocess.PIPE, universal_newlines=True)
try:
    from random import randint
except ImportError:
    subprocess.call(['pip install random'], stdout=subprocess.PIPE, universal_newlines=True)
#for setup you will need a folder named Pictures, inside of this you will need 4 png files named as followed
# sandstone.png
# sandstone1.png
# grind.png
# mine.png
# see readme on how to create your own

#lets allow the time for the program to sleep so we can minimise pycharm this will be usefull for testing
time.sleep(3)
#This tutorial we will make a bot for Runescape and avoid some  heuristic detection by adding randomness

# okay so for some prep work you need to get the exact camera angle because we are working with pixle detection in a 3d enviorment we need to basically take the "3d" out of the enviroment so all the pixels and colors will match our files
# this can be done by left clicking on the compass near the minimap and restricting the zoom in the settings, this will ensure the exact camera angle each time

# for this example we will create and autominer that mines sanstone and processess it into sand
def mine():
    iron_chk = None
    max_iter = 20
    cnt = 0
    while iron_chk is None & cnt < max_iter:
        iron_chk1 = pyautogui.locateOnScreen('Pictures/iron_mine_1.png',minSearchTime=2,confidence=.95)        
        iron_chk2 = pyautogui.locateOnScreen('Pictures/iron_mine_2.png',minSearchTime=2,confidence=.95) 
        iron_chk3 = pyautogui.locateOnScreen('Pictures/iron_mine_3.png',minSearchTime=2,confidence=.95)
        sqrt((iron_chk1 - iron_chk2)**2)
        cnt += 1
    pyautogui.moveTo(iron_chk, duration=1.2, tween=pyautogui.easeOutQuad)
    
    
    # declaring a variable sandstone and set the value to none than search on screen 20 itterations for the file in Pictures/sandstone.png
    for i in range(1,20):
        iron_chk = pyautogui.locateOnScreen('Pictures/iron_mine_1.png',minSearchTime=2,confidence=.95)
        print(iron_chk)
        iron_chk = pyautogui.locateOnScreen('Pictures/iron_mine_2.png',minSearchTime=2,confidence=.95) 
        iron_chk = pyautogui.locateOnScreen('Pictures/iron_mine_3.png',minSearchTime=2,confidence=.95) 
        # this will result in the output of bbox with grid coordinates that we can work with
    pyautogui.moveTo(sandstone, duration=1.2, tween=pyautogui.easeOutQuad)
    # okay so lets break this down pyautogui.moveTo this moves the mouse the tween allows different options this one starts the movement fast and slows down to be as humanly accurate as possible
    pyautogui.rightClick()
    mine = None
    for i in range(1,3):
        mine = pyautogui.locateOnScreen('Pictures/mine.png') 
        # searches 3 itterations for mine.png or the bitmap we pointed it to
    pyautogui.moveTo(mine, duration=1.2)
    pyautogui.click()
    time.sleep(randint(10,12))
    # set the sleep time so the stamina bar only gets about half way down
    
def moveAft():
    global invIx, invIy
    invIx = invIx*-1
    invIy = invIy*-1
    mse = pyautogui.mouseinfo
    initPos = mse.position()
    print(initPos)
    print(f"({invIx}, {invIy})")
    pyautogui.moveTo(initPos+(invIx,invIy), duration=1.2, tween=pyautogui.easeOutQuad)
    pyautogui.rightClick()
    for i in range(0,20):
        pyautogui.click()
        time.sleep(randint(1, 3))
    pyautogui.click()
    time.sleep(randint(20, 50))
    return
#enddef

def moveFore():
    global invIx, invIy
    invIx = invIx*-1
    invIy = invIy*-1
    mse = pyautogui.mouseinfo
    initPos = mse.position()
    print(initPos)
    print(f"({invIx}, {invIy})")
    pyautogui.moveTo(initPos+(invIx,invIy), duration=1.2, tween=pyautogui.easeOutQuad)
    pyautogui.rightClick()
    for i in range(0,20):
        pyautogui.click()
        time.sleep(randint(1, 3))
    pyautogui.click()
    time.sleep(randint(20, 50))
    return
#enddef

def grind():
    global invIx, invIy
    invIx = randint(-100,100)*-1
    invIy = randint(-100,100)*-1
    mse = pyautogui.mouseinfo
    initPos = mse.position()
    print(initPos)
    print(f"({invIx}, {invIy})")
    pyautogui.moveTo(initPos+(invIx,invIy), duration=1.2, tween=pyautogui.easeOutQuad)
    pyautogui.rightClick()
    pyautogui.moveTo(initPos+(invIy,invIx), duration=1.2, tween=pyautogui.easeOutQuad)
    time.sleep(randint(1, 3))
    grind = None
    while grind is None:
        grind = pyautogui.locateOnScreen(os.path.abspath('./Pictures/blurrAmmonite.png'),minSearchTime=2, confidence=0.6, step = 100)
        print(grind)
        time.sleep(randint(1, 3))
    #endfor
    pyautogui.moveTo(grind, duration=1, tween=pyautogui.easeOutQuad)
    pyautogui.click()
    time.sleep(randint(20, 50))
    return
#enddef

# Okay so lets explain the logic below we create a never ending loop, each loop we search the last inventory slot to see if its filled or not 20 times
# if the last inventory slot has something in it it will execute the grind function if it does not it will execute the mine function several times until the last slot is filled usually 3-4 times
# in the grind function the sleep is not random as Runescape gives you the time it takes to craft all 26-27 pieces into sand
if __name__ == '__main__':
    while True:
        invIx = randint(-100,100)*-1
        invIy = randint(-100,100)*-1
        grind()
    #end while
    # for i in range(1,20):
    #     empytbag = pyautogui.locateOnScreen('Pictures/emptybag.png',confidence=.65,region=(1722,748, 200,450)) # the region argument states where on screen you want to look for the matching pixles. If coloration is an issue try using the grayscale=True argument
    # if empytbag is not None:
    #     print("mining")
    #     mine()
    #     empytbag == None
    #     pass
    # for i in range(1, 20):
    #     empytbag = pyautogui.locateOnScreen('Pictures/emptybag.png', confidence=.65,region=(1722, 748, 200, 450))
    # emptybag = None
    # if emptybag is None:
    #     print("grinding")
    #     grind()
    #     emptybag == 1
    #     pass
    # so the first attempt at writing this I tried a while statement for each function and it didnt work as smoothly
    # if you want to make this code look a little better you could create classes but this was intended for fast setup
