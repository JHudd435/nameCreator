import nameCreator
import click
import io


@click.group()
def nameCreatorCLI():
    """A CLI for the nameCreator python package."""


@click.option('-g',
              '--gender',
              help='Gender of the generated name(s) (M)ale or (F)emale.')
@click.option('-l',
              '--language',
              help='Language/Nationality of the generated name(s).')
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
def generate(gender: str, language: str, amount=str, output=str, noprint=str):
    """Generates names. Supported languages are American, Russian, Spanish, Italian, German, French, Finnish, Swedish, and Romanized Japanese."""
    if (gender.lower() == "male" or gender.lower() == "m"):
        for i in range(int(amount)):
            firstname = nameCreator.firstM.FirstNameMale(language)
            lastname = nameCreator.last.LastName(language)
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
            firstname = nameCreator.firstF.FirstNameFemale(language)
            lastname = nameCreator.last.LastName(language)
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