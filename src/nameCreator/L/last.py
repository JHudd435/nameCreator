import random
import os
from unidecode import unidecode

curDir = os.path.dirname(__file__)
#lists
LastAmerican = []
LastRussian = []
LastSpanish = []
LastItalian = []
LastGerman = []
LastFrench = []
LastSwedish = []


def uniLine(obj):
    return (unidecode(obj.rstrip().lstrip(), "preserve"))


## read files
# american (USA)
with open(curDir + "\\names\\american.txt") as mytxt:
    for line in mytxt:
        LastAmerican.append(uniLine(line))

# russian (Russian Federation)
with open(curDir + "\\names\\russian.txt") as mytxt:
    for line in mytxt:
        LastRussian.append(uniLine(line))

# spanish (Spain,Mexico, other Spanish speaking nations) (To be divided)
with open(curDir + "\\names\\spanish.txt") as mytxt:
    for line in mytxt:
        LastSpanish.append(uniLine(line))

#italian
with open(curDir + "\\names\\italian.txt") as mytxt:
    for line in mytxt:
        LastItalian.append(uniLine(line))

#german
with open(curDir + "\\names\\german.txt") as mytxt:
    for line in mytxt:
        LastGerman.append(uniLine(line))

#french
with open(curDir + "\\names\\french.txt") as mytxt:
    for line in mytxt:
        LastFrench.append(uniLine(line))

#swedish
with open(curDir + "\\names\\swedish.txt") as mytxt:
    for line in mytxt:
        LastSwedish.append(uniLine(line))


#defs
def LastName(nationality):
    if (nationality.lower() == "american"):
        return random.choice(LastAmerican)
    if (nationality.lower() == "spanish"):
        return random.choice(LastSpanish)
    if (nationality.lower() == "russian"):
        return random.choice(LastRussian)
    if (nationality.lower() == "italian"):
        return random.choice(LastItalian)
    if (nationality.lower() == "german"):
        return random.choice(LastGerman)
    if (nationality.lower() == "french"):
        return random.choice(LastFrench)
    if (nationality.lower() == "swedish"):
        return random.choice(LastSwedish)