"""
A name generator that can generate names by country.
"""
import random

#lists(male)
FirstAmericanMale = []
FirstRussianMale = []
FirstSpanishMale = []
#lists(female)
FirstAmericanFemale = []
FirstRussianFemale = []
FirstSpanishFemale = []
#lists(last)
LastAmerican = []
LastRussian = []
LastSpanish = []

## read files
# american (USA)
with open("./First Names/Male/american.txt") as mytxt:
    for line in mytxt:
        FirstAmericanMale.append(line.rstrip().lstrip())

with open("./First Names/Female/american.txt") as mytxt:
    for line in mytxt:
        FirstAmericanFemale.append(line.rstrip().lstrip())

with open("./Last Names/american.txt") as mytxt:
    for line in mytxt:
        LastAmerican.append(line.rstrip().lstrip())

# russian (Russian Federation)
with open("./First Names/Male/russian.txt") as mytxt:
    for line in mytxt:
        FirstRussianMale.append(line.rstrip().lstrip())

with open("./First Names/Female/russian.txt") as mytxt:
    for line in mytxt:
        FirstRussianFemale.append(line.rstrip().lstrip())

with open("./Last Names/russian.txt") as mytxt:
    for line in mytxt:
        LastRussian.append(line.rstrip().lstrip())

# spanish (Spain,Mexico, other Spanish speaking nations) (To be divided)
with open("./First Names/Male/spanish.txt") as mytxt:
    for line in mytxt:
        FirstSpanishMale.append(line.rstrip().lstrip())

with open("./First Names/Female/spanish.txt") as mytxt:
    for line in mytxt:
        FirstSpanishFemale.append(line.rstrip().lstrip())

with open("./Last Names/spanish.txt") as mytxt:
    for line in mytxt:
        LastSpanish.append(line.rstrip().lstrip())


#defs
def FirstNameMale(nationality):
    if (nationality.lower() == "american"):
        return random.choice(FirstAmericanMale)
    if (nationality.lower() == "spanish"):
        return random.choice(FirstSpanishMale)
    if (nationality.lower() == "russian"):
        return random.choice(FirstRussianMale)


def FirstNameFemale(nationality):
    if (nationality.lower() == "american"):
        return random.choice(FirstAmericanFemale)
    if (nationality.lower() == "spanish"):
        return random.choice(FirstSpanishFemale)
    if (nationality.lower() == "russian"):
        return random.choice(FirstRussianFemale)


def LastName(nationality):
    if (nationality.lower() == "american"):
        return random.choice(LastAmerican)
    if (nationality.lower() == "spanish"):
        return random.choice(LastSpanish)
    if (nationality.lower() == "russian"):
        return random.choice(LastRussian)
