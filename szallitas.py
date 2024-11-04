targyak = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]

ossztomeg = sum(targyak)

print("2. feladat")
print(f"A tárgyak tömegének összege: {ossztomeg} kg")

dobozok = []
doboz = 0

for i in targyak:
    if doboz + i <= 20:
        doboz += i
    else:
        dobozok.append(doboz)
        doboz = i

if doboz > 0:
    dobozok.append(doboz)

print("3. feladat")
print(f"A dobozok tartalmának tömege (kg): {dobozok} ")
print(f"A szükséges dobozok száma: {len(dobozok)}")