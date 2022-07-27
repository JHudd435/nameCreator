# nameCreator
A python name generator.

This is a python package for name generation. It can generate names from different countries, and can generate both male and female names.
Current languages: "american", "russian", "spanish", "italian", "german","french","swedish"

# Installation
<i>pip install nameCreator</i>

# Usage
firstNameMale = nameCreator.firstM.FirstNameMale('nationality') # nationality can be any of the above options

print(firstNameMale)

lastName = nameCreator.last.LastName('nationality')

print(lastName)

firstNameFemale = nameCreator.firstF.FirstNameFemale('nationality')

print(firstNameFemale)

lastName = nameCreator.last.LastName('nationality')

print(lastName)
