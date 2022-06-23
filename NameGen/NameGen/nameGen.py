"""
A name generator that can generate names by country.
"""
import random
import os
from unidecode import unidecode

curDir = os.path.dirname(__file__)

#lists(male)
FirstAmericanMale = []
FirstRussianMale = []
FirstSpanishMale = []
FirstFrenchMale = []
#lists(female)
FirstAmericanFemale = []
FirstRussianFemale = []
FirstSpanishFemale = []
FirstFrenchFemale = []
#lists(last)
LastAmerican = []
LastRussian = []
LastSpanish = []
LastFrench = []


def uniLine(obj):
    return (unidecode(obj.rstrip().lstrip(), "preserve"))


## read files
# american (USA)
with open(curDir + "/FirstNames/Male/american.txt") as mytxt:
    for line in mytxt:
        FirstAmericanMale.append(uniLine(line))

with open(curDir + "/FirstNames/Female/american.txt") as mytxt:
    for line in mytxt:
        FirstAmericanFemale.append(uniLine(line))

with open(curDir + "/LastNames/american.txt") as mytxt:
    for line in mytxt:
        LastAmerican.append(uniLine(line))

# russian (Russian Federation)
with open(curDir + "/FirstNames/Male/russian.txt") as mytxt:
    for line in mytxt:
        FirstRussianMale.append(uniLine(line))

with open(curDir + "/FirstNames/Female/russian.txt") as mytxt:
    for line in mytxt:
        FirstRussianFemale.append(uniLine(line))

with open(curDir + "/LastNames/russian.txt") as mytxt:
    for line in mytxt:
        LastRussian.append(uniLine(line))

# spanish (Spain,Mexico, other Spanish speaking nations) (To be divided)
with open(curDir + "/FirstNames/Male/spanish.txt") as mytxt:
    for line in mytxt:
        FirstSpanishMale.append(uniLine(line))

with open(curDir + "/FirstNames/Female/spanish.txt") as mytxt:
    for line in mytxt:
        FirstSpanishFemale.append(uniLine(line))

with open(curDir + "/LastNames/spanish.txt") as mytxt:
    for line in mytxt:
        LastSpanish.append(uniLine(line))

# french
with open(curDir + "/FirstNames/Male/french.txt") as mytxt:
    for line in mytxt:
        FirstFrenchMale.append(uniLine(line))

with open(curDir + "/FirstNames/Female/french.txt") as mytxt:
    for line in mytxt:
        FirstFrenchFemale.append(uniLine(line))

with open(curDir + "/LastNames/french.txt") as mytxt:
    for line in mytxt:
        LastFrench.append(uniLine(line))


#defs
def FirstNameMale(nationality):
    if (nationality.lower() == "american"):
        return random.choice(FirstAmericanMale)
    if (nationality.lower() == "spanish"):
        return random.choice(FirstSpanishMale)
    if (nationality.lower() == "russian"):
        return random.choice(FirstRussianMale)
    if (nationality.lower() == "french"):
        return random.choice(FirstFrenchMale)


def FirstNameFemale(nationality):
    if (nationality.lower() == "american"):
        return random.choice(FirstAmericanFemale)
    if (nationality.lower() == "spanish"):
        return random.choice(FirstSpanishFemale)
    if (nationality.lower() == "russian"):
        return random.choice(FirstRussianFemale)
    if (nationality.lower() == "french"):
        return random.choice(FirstFrenchFemale)


def LastName(nationality):
    if (nationality.lower() == "american"):
        return random.choice(LastAmerican)
    if (nationality.lower() == "spanish"):
        return random.choice(LastSpanish)
    if (nationality.lower() == "russian"):
        return random.choice(LastRussian)
    if (nationality.lower() == "french"):
        return random.choice(LastFrench)
