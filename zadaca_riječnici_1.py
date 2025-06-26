import random

# Lista imena
imena = ['Ivan', 'Antonio', 'Antonija', 'Anto', 'Marijan', 'Zvjezdan', 'Ivan', 'Mihaela', 'Ružica', 'Dorijan', 'Petra',
         'Matej', 'Filip', 'Magdalena', 'Mate', 'Iva', 'Danis', 'Josip', 'Nebojša', 'Ante', 'Luka', 'Ante', 'Lorena',
         'Ivan', 'Nikola', 'Ivan', 'Helena', 'Ivan', 'Gabrijela', 'Andrija', 'Regina', 'Petar', 'Dino', 'Marija',
         'Semir', 'Gabriela', 'Borna', 'Filip', 'Krešimir', 'Ivana', 'Gabrijel', 'Vinko', 'Vinko', 'Romana',
         'Viktorija', 'Mija', 'Matej', 'Vinko', 'Luka', 'Antea', 'Ivan', 'Ivan', 'Luka', 'Daniel', 'Nikola', 'Marko']

ocjene = {}
for ime in imena:
    ocjena = random.randint(1, 5)
    ocjene[ime] = ocjena


brojac_ocjena = {}
for ocjena in ocjene.values():
    if ocjena in brojac_ocjena:
        brojac_ocjena[ocjena] += 1
    else:
        brojac_ocjena[ocjena] = 1


print("Broj ocjena po vrijednosti:")
for ocjena in sorted(brojac_ocjena.keys()):
    print("Ocjena", ocjena, ":", brojac_ocjena[ocjena])


ukupno = len(ocjene)
polozili = 0
for ocjena in ocjene.values():
    if ocjena > 1:
        polozili += 1

postotak = polozili / ukupno * 100
print("Postotak prolaznosti:", round(postotak, 2), "%")
