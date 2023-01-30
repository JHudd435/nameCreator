# nameCreator
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/JHudd435/nameCreator?style=for-the-badge)](https://github.com/JHudd435/nameCreator/releases/)
[![GitHub forks](https://img.shields.io/github/forks/JHudd435/nameCreator?style=for-the-badge)](https://github.com/JHudd435/nameCreator/network/members)
[![GitHub license](https://img.shields.io/github/license/JHudd435/nameCreator?style=for-the-badge)](https://github.com/JHudd435/nameCreator/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/JHudd435/nameCreator?style=for-the-badge)](https://github.com/JHudd435/nameCreator/issues)

A python name generator for Windows.

This is a python package for name generation. It can generate names from different countries, and can generate both male and female names.
Nationalities: "american", "russian", "spanish", "italian", "german", "french", "swedish", "finnish", "japaneser" (japanese romanized), and "japanese". Will be adding Chinese and Japanese by release 1.0.0. Also will split spanish into mexican, latino, and spanish.

## Installation

### From pypi
Install from pypi with `pip`:
```shell
pip install nameCreator
```

### Build from source
Clone the repository and cd into the nameCreator directory, then:

```shell
pip install build
python -m build
cd dist
pip install nameCreator-0.9.0-py3-none-any.whl
```

## Usage

### In python file (latest release)
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

### In python file (built from source)
```python
firstNameMale = nameCreator.FirstNameMale('nationality')

print(firstNameMale)

lastName = nameCreator.LastName('nationality')

print(lastName)

firstNameFemale = nameCreator.FirstNameFemale('nationality')

print(firstNameFemale)

lastName = nameCreator.LastName('nationality')

print(lastName)
```

### In command line

Displays help message:

```shell
nameCreatorCLI generate --help
```

Generates 10 male finnish names:

```shell
nameCreatorCLI generate -a 10 -e finnish -g m
```

Generates 10 italian female names, sends to a text file and does not print the output to the terminal:

```shell
nameCreatorCLI generate -a 10 -e italian -g f -o italianNames.txt -n
```

Arguments:

Specifies the amount of names to generate:

```shell
-a --amount
```

Specifies the ethnicity:

```shell
-e --ethnicity
```

Specifies the gender of the generated names:

```shell
-g --gender
```

Specifies the output path (like `C:/Users/You/test.txt` or `test.txt` to put in the current path):

```shell
-o --output
```

Specifies whether or not to print the output to the terminal (useless if there is no output path specified):

```shell
-n --noprint
```

## SOURCES:
https://github.com/ironarachne/namegen