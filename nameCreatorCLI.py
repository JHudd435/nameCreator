# coding: utf-8

import nameCreator
import click
import io


@click.group()
def nameCreatorCLI():
    """A CLI for the nameCreator python package."""


@click.option('-g',
              '--gender',
              help='Gender of the generated name(s) (M)ale or (F)emale.')
@click.option('-e', '--ethnicity', help='Ethnicity of the generated name(s).')
@click.option('-a', '--amount', help='How many names are generated.')
@click.option(
    '-o',
    '--output',
    help="Where to save the generation. If left empty, does not save.")
@click.option(
    '-n',
    '--noprint',
    help="Does not print the names. Useless if you are not using output.")
@nameCreatorCLI.command()
def generate(gender: str, ethnicity: str, amount=str, output=str, noprint=str):
    """Generates names. Supported ethnicities are American, Russian, Spanish, Italian, German, French, Finnish, Swedish, Romanized Japanese, and Japanese."""
    if (gender.lower() == "male" or gender.lower() == "m"):
        for i in range(int(amount)):
            if (ethnicity == "japanese" or ethnicity == "japaneseR"):
                firstname = nameCreator.LastName(ethnicity)
                lastname = nameCreator.FirstNameMale(ethnicity)
            else:
                firstname = nameCreator.FirstNameMale(ethnicity)
                lastname = nameCreator.LastName(ethnicity)
            try:
                if (noprint.lower() == "t"):
                    pass
            except:
                print(firstname + " " + lastname)
            if (output != None):
                with io.open(output, 'a', encoding='utf-8') as f:
                    f.write(firstname + " " + lastname + "\n")
    elif (gender.lower() == "female" or gender.lower() == "f"):
        for i in range(int(amount)):
            if (ethnicity == "japanese" or ethnicity == "japaneseR"):
                lastname = nameCreator.FirstNameFemale(ethnicity)
                firstname = nameCreator.LastName(ethnicity)
            else:
                firstname = nameCreator.FirstNameFemale(ethnicity)
                lastname = nameCreator.LastName(ethnicity)
            try:
                if (noprint.lower() == "t"):
                    pass
            except:
                print(firstname + " " + lastname)
            if (output != None):
                with io.open(output, 'a', encoding='utf-8') as f:
                    f.write(firstname + " " + lastname + "\n")
    else:
        print(gender.lower)
        print("Please enter male or female as gender.")


if __name__ == '__main__':
    nameCreatorCLI(prog_name='nameCreatorCLI')
