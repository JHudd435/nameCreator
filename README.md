# nameCreator
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/JHudd435/nameCreator?style=for-the-badge)](https://github.com/JHudd435/nameCreator/releases/)
[![GitHub forks](https://img.shields.io/github/forks/JHudd435/nameCreator?style=for-the-badge)](https://github.com/JHudd435/nameCreator/network/members)
[![GitHub license](https://img.shields.io/github/license/JHudd435/nameCreator?style=for-the-badge)](https://github.com/JHudd435/nameCreator/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/JHudd435/nameCreator?style=for-the-badge)](https://github.com/JHudd435/nameCreator/issues)

A python name generator for Windows.

This is a python package for name generation. It can generate names from different countries, and can generate both male and female names.
Current namesets: "american", "russian", "spanish", "italian", "german", "french", "swedish", "finnish", "japaneser" (japanese romanized), and "japanese". Will be adding Chinese and Japanese by release 1.0.0. Also will split spanish into mexican, latino, and spanish.
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

Displays help message:

```shell
nameCreatorCLI generate --help
```

Generates 10 male finnish names:

```shell
nameCreatorCLI generate -a 10 -l finnish -g m
```

Generates 10 italian female names, sends to a text file and does not print the output to the terminal:

```shell
nameCreatorCLI generate -a 10 -l italian -g f -o italianNames.txt -n
```