parancsok = input("Kérem a robot parancsait: ")
print(parancsok)
parancsok = list(parancsok)
print(parancsok)

Edb = 0
Ddb = 0
Kdb = 0
Ndb = 0



for i in range(len(parancsok)):
    if parancsok[i] == 'E':
        Edb += 1
    
    if parancsok[i] == 'D':
        Ddb += 1

    if parancsok[i] == 'K':
        Kdb += 1

    if parancsok[i] == 'N':
        Ndb += 1


print(f'E:{Edb}, D:{Ddb}, K:{Kdb}, N:{Ndb}')

if Ndb > Kdb:
    Ndb -= Kdb
    for i in range(Ndb):
        print('N', end='')
else:
    Kdb -= Ndb
    for i in range(Ddb):
        print('K', end='')

if Edb > Ddb:
    Edb -= Ddb
    for i in range(Edb):
        print('E', end='')
else:
    Ddb -= Edb
    for i in range(Kdb):
        print('K', end='')

