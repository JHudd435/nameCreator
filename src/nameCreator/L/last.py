import random
import os
#from unidecode import unidecode

curDir = os.path.dirname(__file__)
#lists
LastAmerican = []
LastRussian = []
LastSpanish = []
LastItalian = []
LastGerman = []
LastFrench = []
LastSwedish = []
LastFinnish = []


def Line(obj):
    return (obj.rstrip().lstrip())


## read files
# american (USA)
with open(curDir + "\\names\\american.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        LastAmerican.append(Line(line))

# russian (Russian Federation)
with open(curDir + "\\names\\russian.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        LastRussian.append(Line(line))

# spanish (Spain,Mexico, other Spanish speaking nations) (To be divided)
with open(curDir + "\\names\\spanish.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        LastSpanish.append(Line(line))

#italian
with open(curDir + "\\names\\italian.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        LastItalian.append(Line(line))

#german
with open(curDir + "\\names\\german.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        LastGerman.append(Line(line))

#french
with open(curDir + "\\names\\french.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        LastFrench.append(Line(line))

#swedish
with open(curDir + "\\names\\swedish.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        LastSwedish.append(Line(line))

#finnish
with open(curDir + "\\names\\finnish.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        LastFinnish.append(Line(line))


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
    if (nationality.lower() == "finnish"):
        return random.choice(LastFinnish)