# coding: utf-8

import random
import os

curDir = os.path.dirname(__file__)
# lists
LastAmerican = []
LastRussian = []
LastSpanish = []
LastItalian = []
LastGerman = []
LastFrench = []
LastSwedish = []
LastFinnish = []
LastJapaneseR = []
LastJapanese = []
LastChineseR = []
LastChinese = []


def Line(obj):
    return (obj.rstrip().lstrip())


# Read Files
# american (USA)
with open(os.path.join(curDir, os.path.join('names', 'american.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        LastAmerican.append(Line(line))

# russian (Russian Federation)
with open(os.path.join(curDir, os.path.join('names', 'russian.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        LastRussian.append(Line(line))

# spanish (Spain,Mexico, other Spanish speaking nations) (To be divided)
with open(os.path.join(curDir, os.path.join('names', 'spanish.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        LastSpanish.append(Line(line))

# italian
with open(os.path.join(curDir, os.path.join('names', 'italian.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        LastItalian.append(Line(line))

# german
with open(os.path.join(curDir, os.path.join('names', 'german.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        LastGerman.append(Line(line))

# french
with open(os.path.join(curDir, os.path.join('names', 'french.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        LastFrench.append(Line(line))

# swedish
with open(os.path.join(curDir, os.path.join('names', 'swedish.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        LastSwedish.append(Line(line))

# finnish
with open(os.path.join(curDir, os.path.join('names', 'finnish.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        LastFinnish.append(Line(line))

# japaneseR (romanized Japanese)
with open(os.path.join(curDir, os.path.join('names', 'japaneseR.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        LastJapaneseR.append(Line(line))

# japanese
with open(os.path.join(curDir, os.path.join('names', 'japanese.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        LastJapanese.append(Line(line))

# chineseR (romanized Chinese)
with open(os.path.join(curDir, os.path.join('names', 'chineseR.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        LastChineseR.append(Line(line))

# chinese
with open(os.path.join(curDir, os.path.join('names', 'chinese.txt')), encoding="utf-8") as mytxt:
    for line in mytxt:
        LastChinese.append(Line(line))


# defs
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
    if (nationality.lower() == "japaneser"):
        return random.choice(LastJapaneseR)
    if (nationality.lower() == "japanese"):
        return random.choice(LastJapanese)
    if (nationality.lower() == "chineser"):
        return random.choice(LastChineseR)
    if (nationality.lower() == "chinese"):
        return random.choice(LastChinese)
