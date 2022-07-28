# nameCreator
[![GitHub issues](https://img.shields.io/github/issues/JHudd435/nameCreator)](https://github.com/JHudd435/nameCreator/issues)
[![GitHub forks](https://img.shields.io/github/forks/JHudd435/nameCreator)](https://github.com/JHudd435/nameCreator/network)
[![GitHub stars](https://img.shields.io/github/stars/JHudd435/nameCreator)](https://github.com/JHudd435/nameCreator/stargazers)
[![GitHub license](https://img.shields.io/github/license/JHudd435/nameCreator)](https://github.com/JHudd435/nameCreator/blob/main/LICENSE)

A python name generator.

This is a python package for name generation. It can generate names from different countries, and can generate both male and female names.
Current languages: "american", "russian", "spanish", "italian", "german","french","swedish"

# Installation
<i>pip install nameCreator</i>

# Usage
firstNameMale = nameCreator.firstM.FirstNameMale('nationality')

print(firstNameMale)

lastName = nameCreator.last.LastName('nationality')

print(lastName)

firstNameFemale = nameCreator.firstF.FirstNameFemale('nationality')

print(firstNameFemale)

lastName = nameCreator.last.LastName('nationality')

print(lastName)

## OR
Go to folder you downloaded nameCreatorCLI.py to

Open powershell window in folder

Run <i>python nameCreatorCLI.py generate --help</i>
Or put the script in python Scripts folder.
