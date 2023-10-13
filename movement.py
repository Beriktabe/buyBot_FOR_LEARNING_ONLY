import pyautogui
import classes
import itemParser
import pyperclip
import time

item1 = (0, 0)
item2 = (0, 0)
item3 = (0, 0)
reroll = (0, 0)
buyPrice = (0, 0)
buyButton = (0, 0)
x = 0
y = 0
speed = 0.2
map = []

def set1Item(mPos):
    global item1
    print('1 item set to: ', mPos)
    item1 = mPos
    pass
def set2Item(mPos):
    global item2
    print('2 item set to: ', mPos)
    item2 = mPos
    #x = mPos[0]
    #print('offset x: ', x)
    pass
def set3Item(mPos):
    global item3
    print('2 row 1 item set to: ', mPos)
    item3 = mPos
    #y = mPos[1] - firstItem[1]
    #print('offset x: ', y)
    pass
def set4Item(mPos):
    global reroll
    print('Reroll set to: ', mPos)
    reroll = mPos
    pass

def allReg():
    global x,y
    y = item2[1] - item1[1]
    x = item3[0] - item1[0]
    print(x, '   ', y)
    pass

def generateItemMap():
    map.append((item1[0], item1[1]))
    #max 16: 11 first row

    for i in range(1, 11):
        map.append((item1[0], item1[1] + y * i))

    for i in range(0, 4):
        map.append((item1[0]+x, item1[1] + y * i))

def doMove(coord):
    pyautogui.moveTo(coord[0], coord[1], speed)

def doClick():
    pyautogui.leftClick()

def doDoubleClick():
    pyautogui.doubleClick()

def doBuy():

    pyautogui.hotkey('ctrl', 'c')
    item = pyperclip.paste()
    print('Item: ', item.split('--------')[0])
    if itemParser.parseItem(item):
        print('----Buy')

        origPrice = 0
        price = 0

        doClick()
        doMove(buyPrice)
        doDoubleClick()
        pyautogui.hotkey('ctrl', 'c')
        origPrice = int(pyperclip.paste())
        price = round(origPrice * 0.53)
        print('Original: ', origPrice)
        print('Changed: ', price)
        pyautogui.typewrite(str(price), interval=0.2)
        print('Written: ', str(price))
        doMove(buyButton)

        doClick()

        doMove(buyPrice)
        doDoubleClick()
        pyautogui.hotkey('ctrl', 'c')
        if origPrice != int(pyperclip.paste()):
            pyautogui.typewrite(str(round(origPrice*0.63)), interval=0.2)
            doMove(buyButton)
            doClick()
            doClick()

        print('----Bought')
        return True
    else:
        print('----Not buy')
        return False

def printMap():
    print(map)