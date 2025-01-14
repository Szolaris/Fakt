N = 8
terulretek = [42,110,125,166,42,110,120,35,48,58]
arak = [15,20,160,180,10 ,39,100,41,51,59] 

db = 0

for i in range(N):
    if arak[i] > 50:
        db +=1

if db == 0:
    print("Nincs ilyen lakás")
else:
    print(db)

van = False
for i in terulretek:
    if i < 50:
        van = True

if van == True:
    print("IGEN")
else:
    print("NEM")

sorszam = 0

for i in range(N):
    if arak[i] <= 60 and terulretek[i] > 50:
        sorszam = i +1
        break
if sorszam == 0:
    print("Nincs a keresésnek megfelelő lakás")
else:
    print(sorszam)

nar = []
for i in range(N):
    nar.append(arak[i]/terulretek[i])
minimum = nar[0]
sorszam = 0
for i in range(len(nar)):
    if nar[i] < minimum:
        minimum = i
        sorszam = i + 1
print(minimum)


print(len(set(terulretek)))
