# coding: utf-8

import random
import os

curDir = os.path.dirname(__file__)
# lists
FirstAmericanMale = []
FirstRussianMale = []
FirstSpanishMale = []
FirstItalianMale = []
FirstGermanMale = []
FirstFrenchMale = []
FirstSwedishMale = []
FirstFinnishMale = []
FirstJapaneseRMale = []
FirstJapaneseMale = []
FirstChineseRMale = []
FirstChineseMale = []


def Line(obj):
    return (obj.rstrip().lstrip())


# Read Files
# american (USA)
with open(os.path.join(curDir, os.path.join('names', 'american.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstAmericanMale.append(Line(line))

# russian (Russian Federation)
with open(os.path.join(curDir, os.path.join('names', 'russian.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstRussianMale.append(Line(line))

# spanish (Spain,Mexico, other Spanish speaking nations) (To be divided)
with open(os.path.join(curDir, os.path.join('names', 'spanish.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstSpanishMale.append(Line(line))

# italian
with open(os.path.join(curDir, os.path.join('names', 'italian.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstItalianMale.append(Line(line))

# german
with open(os.path.join(curDir, os.path.join('names', 'german.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstGermanMale.append(Line(line))

# french
with open(os.path.join(curDir, os.path.join('names', 'french.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstFrenchMale.append(Line(line))

# swedish
with open(os.path.join(curDir, os.path.join('names', 'swedish.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstSwedishMale.append(Line(line))

# finnish
with open(os.path.join(curDir, os.path.join('names', 'finnish.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstFinnishMale.append(Line(line))

# japaneseR (romanized Japanese)
with open(os.path.join(curDir, os.path.join('names', 'japaneseR.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstJapaneseRMale.append(Line(line))

# japanese
with open(os.path.join(curDir, os.path.join('names', 'japanese.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstJapaneseMale.append(Line(line))

# chineseR (romanized Chinese)
with open(os.path.join(curDir, os.path.join('names', 'chineseR.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstChineseRMale.append(Line(line))

# chinese
with open(os.path.join(curDir, os.path.join('names', 'chinese.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        FirstChineseMale.append(Line(line))


# defs
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
    if (nationality.lower() == "japaneser"):
        return random.choice(FirstJapaneseRMale)
    if (nationality.lower() == "japanese"):
        return random.choice(FirstJapaneseMale)
    if (nationality.lower() == "chineser"):
        return random.choice(FirstChineseRMale)
    if (nationality.lower() == "chinese"):
        return random.choice(FirstChineseMale)
