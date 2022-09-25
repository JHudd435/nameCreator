import random
import os
#from unidecode import unidecode

curDir = os.path.dirname(__file__)
#lists
FirstAmericanMale = []
FirstRussianMale = []
FirstSpanishMale = []
FirstItalianMale = []
FirstGermanMale = []
FirstFrenchMale = []
FirstSwedishMale = []
FirstFinnishMale = []


def Line(obj):
    return (obj.rstrip().lstrip())


## read files
# american (USA)
with open(curDir + "\\names\\american.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstAmericanMale.append(Line(line))

# russian (Russian Federation)
with open(curDir + "\\names\\russian.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstRussianMale.append(Line(line))

# spanish (Spain,Mexico, other Spanish speaking nations) (To be divided)
with open(curDir + "\\names\\spanish.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstSpanishMale.append(Line(line))

#italian
with open(curDir + "\\names\\italian.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstItalianMale.append(Line(line))

#german
with open(curDir + "\\names\\german.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstGermanMale.append(Line(line))

#french
with open(curDir + "\\names\\french.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstFrenchMale.append(Line(line))

#swedish
with open(curDir + "\\names\\swedish.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstSwedishMale.append(Line(line))

#finnish
with open(curDir + "\\names\\finnish.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstFinnishMale.append(Line(line))


#defs
def FirstNameMale(nationality):
    if (nationality.lower() == "american"):
        return random.choice(FirstAmericanMale)
    if (nationality.lower() == "spanish"):
        return random.choice(FirstSpanishMale)
    if (nationality.lower() == "russian"):
        return random.choice(FirstRussianMale)
    if (nationality.lower() == "italian"):
        return random.choice(FirstItalianMale)
    if (nationality.lower() == "german"):
        return random.choice(FirstGermanMale)
    if (nationality.lower() == "french"):
        return random.choice(FirstFrenchMale)
    if (nationality.lower() == "swedish"):
        return random.choice(FirstSwedishMale)
    if (nationality.lower() == "finnish"):
        return random.choice(FirstFinnishMale)