dCurrency = {}
dMapsName = []
dMapsMods = []
dMapFragments = []
dGems = {}
dItemPause = []
dDelveSocketable = []

def load():
    with open('BUY/Stackable Currency.txt', 'r') as f:
        lines = f.read()
        for line in lines.split('@'):
            itemSet = line.replace('\n', '').split('#')
            name = itemSet[0]
            amount = int(itemSet[1])
            dCurrency[name] = amount

    with open('BUY/Map Fragments.txt', 'r') as f:
        lines = f.read()
        for line in lines.split('@'):
            item = line.replace('\n', '')
            dMapFragments.append(item)

    #with open('BUY/Pause.txt', 'r') as f:
    #    lines = f.read()
    #    for line in lines.split('@'):
    #        item = line.replace('\n', '')
    #        dItemPause.append(item)

    with open('BUY/Support Skill Gems.txt', 'r') as f:
        lines = f.read()
        for line in lines.split('@'):
            itemSet = line.replace('\n', '').split('#')
            name = itemSet[0]
            level = int(itemSet[1])
            dGems[name] = level

    with open('BUY/Maps.txt', 'r') as f:
        lines = f.read()
        for line in lines.split('@'):
            itemSet = line.replace('\n', '').split(':')
            mode = itemSet[0]
            data = itemSet[1]
            if mode == 'name':
                dMapsName.append(data)
            elif mode == 'mode':
                dMapsMods.append(data)

    with open('BUY/Delve Stackable Socketable Currency.txt', 'r') as f:
        lines = f.read()
        a = lines.split('@')
        for line in lines.split('@'):
            item = line.replace('\n', '')
            dDelveSocketable.append(item)
def fa():
    print(dCurrency)
