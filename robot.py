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
