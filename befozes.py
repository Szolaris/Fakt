uvegek = [5, 2, 2, 4, 3, 2, 4, 10, 5, 5, 3, 5, 4, 3, 3]

print("2. feladat")

lekvar = int(input('Mari néni lekvárja (dl): '))

print("3.feladat")
maxertek = uvegek[0]
for i in range(len(uvegek)):
    if uvegek[i] > maxertek:
        maxertek = uvegek[i]
        sor = i

print(f'A legnagyobb üveg: {maxertek} dl és {sor}. a sorban.')

print("4.feladat")

osszeg = 0

for i in range(len(uvegek)):
    osszeg += uvegek[i]
if osszeg > lekvar:
    print("Elegendő üveg volt.")
else:
    print("Nem volt elegendő üveg.")
