import nameGen

for i in range(10):
    hola = nameGen.FirstNameFemale("spanish") + " " + nameGen.LastName(
        "spanish")
    print(hola)
    hello = nameGen.FirstNameFemale("american") + " " + nameGen.LastName(
        "american")
    print(hello)
    boom = nameGen.FirstNameFemale("russian") + " " + nameGen.LastName(
        "russian")
    print(boom)
