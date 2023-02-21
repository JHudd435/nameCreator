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

# italian
with open(curDir + "\\names\\italian.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        LastItalian.append(Line(line))

# german
with open(curDir + "\\names\\german.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        LastGerman.append(Line(line))

# french
with open(curDir + "\\names\\french.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        LastFrench.append(Line(line))

# swedish
with open(curDir + "\\names\\swedish.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        LastSwedish.append(Line(line))

# finnish
with open(curDir + "\\names\\finnish.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        LastFinnish.append(Line(line))

# japaneseR (romanized Japanese)
with open(curDir + "\\names\\japaneseR.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        LastJapaneseR.append(Line(line))

# japanese
with open(curDir + "\\names\\japanese.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        LastJapanese.append(Line(line))

# chineseR (romanized Chinese)
with open(curDir + "\\names\\chineseR.txt", encoding="utf-8") as mytxt:
    for line in mytxt:
        LastChineseR.append(Line(line))

# chinese
with open(curDir + "\\names\\chinese.txt", encoding="utf-8") as mytxt:
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