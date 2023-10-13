import pyautogui
from enum import Enum
import keyboard
import time

class imgArtifacts(str, Enum):
    __order__ = " tGreater tGrand tExceptional tLesser "
    tGreater = 'artifacts/greater.png'
    tGrand = 'artifacts/grand.png'
    tExceptional = 'artifacts/exceptional.png'
    tLesser = 'artifacts/lesser.png'

tHaggle = 'artifacts/haggle.png'

def findHaggle():
    if 0 == isOnScreen(tHaggle):
        return False
    return True

def findArt():
    for i in imgArtifacts:
        coord = isOnScreen(i)
        if coord != 0:
            return i

def isOnScreen(art):

    try:
        coordIfFound = pyautogui.locateOnScreen(art, grayscale=True)
        print(coordIfFound)
        return coordIfFound
    except:
        print('ERROR')
        return 0


keyboard.wait('*')
#time.sleep(5)
#print(findHaggle())
#print(findArt())
coord = pyautogui.locateCenterOnScreen('artifacts/box3.png')
pyautogui.moveTo(coord)
print(coord)