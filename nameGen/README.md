# NameGen
A python name generator.

This is a python package for name generation. It can generate names from different countries, and can generate both male and female names.
Current languages: "american", "russian", "spanish"

# Installation
<i>pip install nameGen</i>

# Usage
firstNameMale = nameGen.firstM.FirstNameMale('nationality')
print(firstNameMale)
lastName = nameGen.last.LastName('nationality')
print(lastName)

firstNameFemale = nameGen.firstF.FirstNameFemale('nationality')
print(firstNameFemale)
lastName = nameGen.last.LastName('nationality')
print(lastName)