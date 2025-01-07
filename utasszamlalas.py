sor = input()
sor = sor.split()

n = int(sor[0])
m = int(sor[1])

zsufolt = m * 0.8
ures = m * 0.2

zsufolt_buszok = []
ures_buszok = []

for i in range(n):
    busz = int(input())
    if busz >= zsufolt:
        zsufolt_buszok.append(i + 1)
    if busz < ures:
        ures_buszok.append(i + 1)



print(len(zsufolt_buszok), end=' ')
for i in range(len(zsufolt_buszok)):
    print(zsufolt_buszok[i], end=' ')

print(len(ures_buszok), end=' ')
for i in range(len(ures_buszok)):
    print(ures_buszok[i], end=' ')
