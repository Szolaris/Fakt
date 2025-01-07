n = int(input('tanulok szama: '))
k = int(input('k: '))
legalabb_k = []
db = 0

for i in range(n):
    jegy = int(input())
    if jegy >= K:
        db += 1
        legalabb_k.append(i +1)

print(db, end=' ')

for i in range(db-1):
    print(legalabb_k[i], end=' ')
print(legalabb_k[db-1])
