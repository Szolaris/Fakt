N = int(input("Add meg a tejek árát:"))
min_ár = int(input("Add meg a tej minimum árát:"))
max_ár = int(input("Add meg a tej maximum árát:"))
árak = []
db = []

for i in range(N):
    ár = int(input("Add meg a tejek árát:"))
    árak.append(ár)

print(árak)

for i in range(N):
    if min_ár <= árak[i] <= max_ár:
        db += 1
print(db)
