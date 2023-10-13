from imageParser import *

ExceptionalArtAmount = 0
GrandArtAmount = 0
GreaterArtAmount = 0
LesserArtAmount = 0

def Pay(art: imgArtifacts, price: int):
    global ExceptionalArtAmount, GrandArtAmount, GreaterArtAmount, LesserArtAmount

    if art == imgArtifacts.tExceptional:
        if ExceptionalArtAmount - price >= 0:
            ExceptionalArtAmount = ExceptionalArtAmount - price
            return True
    elif art == imgArtifacts.tLesser:
        if LesserArtAmount - price >= 0:
            LesserArtAmount = LesserArtAmount - price
            return True
    elif art == imgArtifacts.tGrand:
        if GrandArtAmount - price >= 0:
            GrandArtAmount = GrandArtAmount - price
            return True
    elif art == imgArtifacts.tGreater:
        if GreaterArtAmount - price >= 0:
            GreaterArtAmount = GreaterArtAmount - price
            return True

    return False