sor = input()
sor = sor.split()
N = int(sor[0])
K = int(sor[1])

teruletek = []
arak = []

for i in range(N):
    sor = input()
    sor  = sor.split()
    teruletek.append(int(sor[0]))
    arak.append(int(sor[1]))

db = 0
dragak = []

for i in range(N):
    if arak[i] > K:
        db += 1
        dragak.append(i+1)

print()

print(db, end=' ')
for i in range(len(dragak)):
    print(dragak[i], end=' ')
