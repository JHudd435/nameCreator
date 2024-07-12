# coding: utf-8

import random
import os

curDir = os.path.dirname(__file__)
# lists
FirstAmericanFemale = []
FirstRussianFemale = []
FirstSpanishFemale = []
FirstItalianFemale = []
FirstGermanFemale = []
FirstFrenchFemale = []
FirstSwedishFemale = []
FirstFinnishFemale = []
FirstJapaneseRFemale = []
FirstJapaneseFemale = []
FirstChineseRFemale = []
FirstChineseFemale = []


def Line(obj):
    return (obj.rstrip().lstrip())


# Read Files
# american (USA)
with open(os.path.join(curDir, os.path.join('names', 'american.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstAmericanFemale.append(Line(line))

# russian (Russian Federation)
with open(os.path.join(curDir, os.path.join('names', 'russian.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstRussianFemale.append(Line(line))

# spanish (Spain,Mexico, other Spanish speaking nations) (To be divided)
with open(os.path.join(curDir, os.path.join('names', 'spanish.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstSpanishFemale.append(Line(line))

# italian
with open(os.path.join(curDir, os.path.join('names', 'italian.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstItalianFemale.append(Line(line))

# german
with open(os.path.join(curDir, os.path.join('names', 'german.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstGermanFemale.append(Line(line))

# french
with open(os.path.join(curDir, os.path.join('names', 'french.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstFrenchFemale.append(Line(line))

# swedish
with open(os.path.join(curDir, os.path.join('names', 'swedish.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstSwedishFemale.append(Line(line))

# finnish
with open(os.path.join(curDir, os.path.join('names', 'finnish.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstFinnishFemale.append(Line(line))

# japaneseR (romanized Japanese)
with open(os.path.join(curDir, os.path.join('names', 'japaneseR.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstJapaneseRFemale.append(Line(line))

# japanese
with open(os.path.join(curDir, os.path.join('names', 'japanese.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstJapaneseFemale.append(Line(line))

# chineseR (romanized Chinese)
with open(os.path.join(curDir, os.path.join('names', 'chineseR.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstChineseRFemale.append(Line(line))

# chinese
with open(os.path.join(curDir, os.path.join('names', 'chinese.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstChineseFemale.append(Line(line))


# defs
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
    if (nationality.lower() == "japaneser"):
        return random.choice(FirstJapaneseRFemale)
    if (nationality.lower() == "japanese"):
        return random.choice(FirstJapaneseFemale)
    if (nationality.lower() == "chineser"):
        return random.choice(FirstChineseRFemale)
    if (nationality.lower() == "chinese"):
        return random.choice(FirstChineseFemale)
