from itemParser import parseItem
from classes import itemClass
from Settings import load, fa
import pyperclip
import movement
import pyautogui
import keyboard
import os
isOnPause = False

def startRoot():
    global isOnPause
    print('WAITING FOR BUTTON V')

    while True:
        keyboard.wait('v')
        for j in range(0, 34): #<- max coin use
            for i in range(0, 16):
                if isOnPause:
                    print('PAUSE: WAITING FOR BUTTON V')
                    keyboard.wait('v')
                movement.doMove(movement.map[i])
                movement.doBuy()
            movement.doMove(movement.reroll)
            movement.doClick()

def switchPause(e):
    global isOnPause
    isOnPause = not isOnPause

if __name__ == '__main__':
    keyboard.on_press_key('/', lambda x: os._exit(1))
    keyboard.on_press_key('\\', switchPause)
    pyautogui.PAUSE = 0.08
    load()
    #map = []
    """
    keyboard.wait('+')
    movement.set1Item(pyautogui.position())

    keyboard.wait('+')
    movement.set2Item(pyautogui.position())

    keyboard.wait('+')
    movement.set3Item(pyautogui.position())

    keyboard.wait('+')
    movement.set4Item(pyautogui.position())

    movement.allReg()
    movement.generateItemMap()
    movement.printMap()
    """
    print('HOVER OVER 16 items in 2 rows and press "-" on each')

    for i in range(0, 16):
        keyboard.wait('-')
        movement.map.append(pyautogui.position())
        #mpos = movement.map[i]
        #pyautogui.moveTo(mpos[0], mpos[1], 1)
    print('HOVER OVER reroll button and press "+"')
    print('+')
    keyboard.wait('+')
    movement.reroll = pyautogui.position()
    print('HOVER OVER buy price textbox and press "*"')
    print('*')
    keyboard.wait('*')
    movement.buyPrice = pyautogui.position()
    print('*')
    print('HOVER OVER buy button and press "*"')
    keyboard.wait('*')
    movement.buyButton = pyautogui.position()

    startRoot()

