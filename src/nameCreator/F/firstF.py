#!/usr/bin/env python
# encoding=utf-8

import random
import os
#from unidecode import unidecode

curDir = os.path.dirname(__file__)
#lists
FirstAmericanFemale = []
FirstRussianFemale = []
FirstSpanishFemale = []
FirstItalianFemale = []
FirstGermanFemale = []
FirstFrenchFemale = []
FirstSwedishFemale = []
FirstFinnishFemale = []


def Line(obj):
    return (obj.rstrip().lstrip())


## read files
# american (USA)
with open(curDir + "\\names\\american.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstAmericanFemale.append(Line(line))

# russian (Russian Federation)
with open(curDir + "\\names\\russian.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstRussianFemale.append(Line(line))

# spanish (Spain,Mexico, other Spanish speaking nations) (To be divided)
with open(curDir + "\\names\\spanish.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstSpanishFemale.append(Line(line))

#italian
with open(curDir + "\\names\\italian.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstItalianFemale.append(Line(line))

#german
with open(curDir + "\\names\\german.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstGermanFemale.append(Line(line))

#french
with open(curDir + "\\names\\french.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstFrenchFemale.append(Line(line))

#swedish
with open(curDir + "\\names\\swedish.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstSwedishFemale.append(Line(line))

#finnish
with open(curDir + "\\names\\finnish.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstFinnishFemale.append(Line(line))


#defs
def FirstNameFemale(nationality):
    if (nationality.lower() == "american"):
        return random.choice(FirstAmericanFemale)
    if (nationality.lower() == "spanish"):
        return random.choice(FirstSpanishFemale)
    if (nationality.lower() == "russian"):
        return random.choice(FirstRussianFemale)
    if (nationality.lower() == "italian"):
        return random.choice(FirstItalianFemale)
    if (nationality.lower() == "german"):
        return random.choice(FirstGermanFemale)
    if (nationality.lower() == "french"):
        return random.choice(FirstFrenchFemale)
    if (nationality.lower() == "swedish"):
        return random.choice(FirstSwedishFemale)
    if (nationality.lower() == "finnish"):
        return random.choice(FirstFinnishFemale)