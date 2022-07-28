import nameCreator
import click


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
@nameCreatorCLI.command()
def generate(gender: str, language: str, amount=str):
    """Generates names."""
    if (gender.lower() == "male" or gender.lower() == "m"):
        for i in range(int(amount)):
            firstname = nameCreator.firstM.FirstNameMale(language)
            lastname = nameCreator.last.LastName(language)
            print(firstname + " " + lastname)
    elif (gender.lower() == "female" or gender.lower() == "f"):
        for i in range(int(amount)):
            firstname = nameCreator.firstF.FirstNameFemale(language)
            lastname = nameCreator.last.LastName(language)
            print(firstname + " " + lastname)
    else:
        print(gender.lower)
        print("Please enter male or female as gender.")


if __name__ == '__main__':
    nameCreatorCLI(prog_name='nameCreatorCLI')