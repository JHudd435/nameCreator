import random
import os
from unidecode import unidecode

curDir = os.path.dirname(__file__)
#lists
FirstAmericanMale = []
FirstRussianMale = []
FirstSpanishMale = []


def uniLine(obj):
    return (unidecode(obj.rstrip().lstrip(), "preserve"))


## read files
# american (USA)
with open(curDir + "\\names\\american.txt") as mytxt:
    for line in mytxt:
        FirstAmericanMale.append(uniLine(line))

# russian (Russian Federation)
with open(curDir + "\\names\\russian.txt") as mytxt:
    for line in mytxt:
        FirstRussianMale.append(uniLine(line))

# spanish (Spain,Mexico, other Spanish speaking nations) (To be divided)
with open(curDir + "\\names\\spanish.txt") as mytxt:
    for line in mytxt:
        FirstSpanishMale.append(uniLine(line))


#defs
def FirstNameMale(nationality):
    if (nationality.lower() == "american"):
        return random.choice(FirstAmericanMale)
    if (nationality.lower() == "spanish"):
        return random.choice(FirstSpanishMale)
    if (nationality.lower() == "russian"):
        return random.choice(FirstRussianMale)