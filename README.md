# nameCreator
![GitHub release (latest by date)](https://img.shields.io/github/v/release/JHudd435/nameCreator?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/JHudd435/nameCreator?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/JHudd435/nameCreator?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/JHudd435/nameCreator?style=for-the-badge)

A python name generator for Windows.

This is a python package for name generation. It can generate names from different countries, and can generate both male and female names.
Current namesets: "american", "russian", "spanish", "italian", "german", "french", "swedish", "finnish". Will be adding Chinese and Japanese in next release. Also will split spanish into mexican, latino, and spanish.
Many of the name sets come from https://github.com/ironarachne/namegen.

## Installation
Install from pypi with `pip`:
```shell
pip install nameCreator
```
## Usage

### In python file
```python
firstNameMale = nameCreator.firstM.FirstNameMale('nationality')

print(firstNameMale)

lastName = nameCreator.last.LastName('nationality')

print(lastName)

firstNameFemale = nameCreator.firstF.FirstNameFemale('nationality')

print(firstNameFemale)

lastName = nameCreator.last.LastName('nationality')

print(lastName)
```

### In command line
```shell
nameCreatorCLI generate --help
```
