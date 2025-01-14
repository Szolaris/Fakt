N = int(input("Add meg"))

eszik = []
etel = []

for i in range(N):
    sor = input()
    eszik.append(sor.split()[0])
    etel.append(sor.split()[1])

ragadozok = set()


for i in range(N):
    if etel[i] in eszik:
        ragadozok.add(eszik[i])

ragadozok = list(ragadozok)

print(len(ragadozok))

for i in range(len(ragadozok)):
    print(ragadozok[i])
