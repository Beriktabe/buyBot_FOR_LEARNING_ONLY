from enum import Enum
import Settings

class itemClass(str,Enum):
    tMaps = 'Maps'
    tGems = 'Support Skill Gems'
    tCurrency = 'Stackable Currency'
    tMapFragments = 'Map Fragments'
    tDelve = 'Delve Stackable Socketable Currency'
    tItemPause = 'Jewels' #TODO: pause item

class base(object):
    #isBuy = False
    @staticmethod
    def parse(data: str):
        pass

class maps(base):

    def __init__(self):
        """Constructor"""

    @staticmethod
    def parse(data: str):
        implicit1 = 'nullData'
        implicit2 = 'nullData'
        splittedData = data.split('--------')
        name = splittedData[0].splitlines()[2]
        if len(splittedData[3].splitlines()) > 1:
            implicit1 = splittedData[3].splitlines()[1]
        if len(splittedData[3].splitlines()) > 2:
            implicit2 = splittedData[3].splitlines()[2]
        if name in Settings.dMapsName:
            return True
        elif implicit1 in Settings.dMapsMods or implicit2 in Settings.dMapsMods:
            return True

        return False

class currency(base):

    def __init__(self):
        """Constructor"""

    @staticmethod
    def parse(data: str):
        splittedData = data.split('--------')
        #print(splittedData)
        name = splittedData[0].splitlines()[2]
        #print(splittedData[1][12:].split('/')[0])
        stackSize = int(splittedData[1][14:].replace(' ', '').split('/')[0])
        if name in Settings.dCurrency:
            if stackSize >= Settings.dCurrency[name]:
                # self.isBuy = True
                return True

        return False

class mapFragments(base):

    def __init__(self):
        """Constructor"""

    @staticmethod
    def parse(data: str):
        splittedData = data.split('--------')
        name = splittedData[0].splitlines()[2]
        if name in Settings.dMapFragments:
            return True

        return False

class delveSocketable(base):

    def __init__(self):
        """Constructor"""

    @staticmethod
    def parse(data: str):
        splittedData = data.split('--------')
        name = splittedData[0].splitlines()[2]
        if name in Settings.dDelveSocketable:
            return True

        return False

class gems(base):

    def __init__(self):
        """Constructor"""

    @staticmethod
    def parse(data: str):
        splittedData = data.split('--------')
        name = splittedData[0].splitlines()[2]
        level = 0#int(splittedData[1].splitlines()[2][7:])
        #qual = int(splittedData[1].splitlines()[4][10:].split('%')[0])
        if name in Settings.dGems:
            if level >= Settings.dGems[name]:
                return True

        return False

class itemPause(base):

    def __init__(self):
        """Constructor"""