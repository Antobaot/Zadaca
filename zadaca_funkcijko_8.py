
def pozdrav1(ime):
    return "Pozdrav " + ime + "!"


pozdrav2 = lambda ime: "Dobrodošao " + ime + "!"


def izvrsi_pozdrav(funkcija):
    ime = input("Unesi svoje ime: ")
    print(funkcija(ime))


izvrsi_pozdrav(pozdrav1)

