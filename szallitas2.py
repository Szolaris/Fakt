targyak = []
n = 15

targyak = list(map(int, input().split(",")))
print(targyak)
print('2.feladat')


dobozok = []
tomeg = 0

for i in range(len(targyak)):
    if tomeg + targyak[i] > 20:
        '''pass'''
        dobozok.append(tomeg)
        tomeg = 0
    tomeg += tomeg[i]
dobozok.append(tomeg)

print('3. feladat')
print('A dobozok tartalmának tömege (kg): ', end='')
for i in range(len(dobozok)):
    print(dobozok[i], end='')
