import random


szavak = ["fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", 
"farkas", "almafa", "babona", "gerinc", "dervis", "bagoly", 
"ecetes", "angyal", "boglya"]

kivalasztott_szo = random.choice(szavak)
print(kivalasztott_szo)

talalt_betuk = []

for i in range(6):
    talalt_betuk.append(".")


db = 0
jatek = True
while jatek:
    tipp = input("Kérem a tipppet: ")
    if tipp == 'stop':
        jatek = False
        break

    db += 1
    
    for i in range(6):
        if kivalasztott_szo[i] in tipp:
            talalt_betuk[i] = kivalasztott_szo[i]

    eredmeny= ''.join(talalt_betuk)
    print(f'Az eredmény : {eredmeny}')

    if "." not in talalt_betuk:
        print(f'{db} darab tippeléssel találtad el')
        jatek = False
