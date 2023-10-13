from classes import itemClass, currency, maps, mapFragments, gems, delveSocketable
import os

def parseItem(data:str):
    dataType = data.splitlines()[0][12:]

    if dataType == itemClass.tCurrency:
        return currency.parse(data)
    elif dataType == itemClass.tMaps:
        return maps.parse(data)
    elif dataType == itemClass.tMapFragments:
        return mapFragments.parse(data)
    elif dataType == itemClass.tGems:
        return gems.parse(data)
    elif dataType == itemClass.tDelve:
        return delveSocketable.parse(data)
    elif dataType == itemClass.tItemPause:
        print('ITEMS PAUSE: ', dataType)
        os._exit(1)
        return False #todo pause item + missing item