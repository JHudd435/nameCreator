import random
import os
from unidecode import unidecode

curDir = os.path.dirname(__file__)
#lists
FirstAmericanFemale = []
FirstRussianFemale = []
FirstSpanishFemale = []
FirstItalianFemale = []
FirstGermanFemale = []
FirstFrenchFemale = []
FirstSwedishFemale = []


def uniLine(obj):
    return (unidecode(obj.rstrip().lstrip(), "preserve"))


## read files
# american (USA)
with open(curDir + "\\names\\american.txt") as mytxt:
    for line in mytxt:
        FirstAmericanFemale.append(uniLine(line))

# russian (Russian Federation)
with open(curDir + "\\names\\russian.txt") as mytxt:
    for line in mytxt:
        FirstRussianFemale.append(uniLine(line))

# spanish (Spain,Mexico, other Spanish speaking nations) (To be divided)
with open(curDir + "\\names\\spanish.txt") as mytxt:
    for line in mytxt:
        FirstSpanishFemale.append(uniLine(line))

#italian
with open(curDir + "\\names\\italian.txt") as mytxt:
    for line in mytxt:
        FirstItalianFemale.append(uniLine(line))

#german
with open(curDir + "\\names\\german.txt") as mytxt:
    for line in mytxt:
        FirstGermanFemale.append(uniLine(line))

#french
with open(curDir + "\\names\\french.txt") as mytxt:
    for line in mytxt:
        FirstFrenchFemale.append(uniLine(line))

#swedish
with open(curDir + "\\names\\swedish.txt") as mytxt:
    for line in mytxt:
        FirstSwedishFemale.append(uniLine(line))


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