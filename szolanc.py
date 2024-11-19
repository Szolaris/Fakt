elso_szo = input('1. szó: ')
játék = False
pontok = 0


if len(elso_szo) == 6:
    játék = True
    pontok +=1
else:
    print('A karakterek száma téves')


while játék:
    masodik_szo = input('Kövi szó: ')
    if len(masodik_szo) != 6:
        print('A karakterek száma téves')
        játék = False
        break

    if masodik_szo[0] != elso_szo[5]:
        print('Nem illeszkedik!')
        játék = False
    pontok += 1
    elso_szo = masodik_szo

if pontok <= 2:
    print('kezdő')
elif pontok <= 5:
    print('közepes')
else:
    print('haladó')

print(pontok)
