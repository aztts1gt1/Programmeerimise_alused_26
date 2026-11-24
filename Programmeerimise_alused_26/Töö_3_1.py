
#  Tsüklid (FOR, WHILE, WHILE True)
# Proovi lahendada kõik ülesanded kolme erineva tsükliga, kui see on võimalik.

# 1️⃣ Sisestatakse 15 arvu.
# Määrata, mitu neist on täisarvud.

täisarvud = 0
for i in range(15):
    arv = float(input("Sisesta arv: "))
    if arv % 1 == 0:
        täisarvud += 1
print("Täisarve oli kokku:", täisarvud)



# 2️⃣ Küsi kasutajalt arv A ja leia kõigi naturaalarvude summa vahemikus 1 kuni A.

a = int(input("Sisesta arv A: "))
summa = 0
i = 1
while i <= a:
    summa += i
    i += 1
print("Summa on:", summa)



# 3️⃣ Sisestatakse 8 arvu.
# Leida nende korrutis (ainult positiivsete arvude puhul).

korrutis = 1
loendur = 0
while True:
    arv = float(input("Sisesta arv: "))
    if arv > 0:
        korrutis *= arv
    loendur += 1
    if loendur == 8:
        break
print("Positiivsete arvude korrutis:", korrutis)



# 4️⃣ Koosta programm, mis väljastab ekraanile arvude ruudud vahemikus 10 kuni 20.

for arv in range(10, 21):
    print(arv, "ruut on", arv ** 2)



# 5️⃣ Koosta programm, mis arvutab ainult negatiivsete arvude summa N sisestatud arvu seast.
# N väärtus sisestatakse klaviatuurilt.

n = int(input("Mitu arvu sisestad? "))
summa = 0
kord = 0
while kord < n:
    arv = float(input("Sisesta arv: "))
    if arv < 0:
        summa += arv
    kord += 1
print("Negatiivsete arvude summa:", summa)



# 6️⃣ Klaviatuurilt sisestatakse N arvu.
# Koosta programm, mis määrab sisestatud arvude seast:
#     negatiivsete arvude arvu,
#     positiivsete arvude arvu,
#     nullide arvu.
#     (N väärtus sisestatakse klaviatuurilt.)

n = int(input("Mitu arvu sisestad? "))
pos = 0
neg = 0
nullid = 0

for i in range(n):
    arv = float(input("Sisesta arv: "))
    if arv > 0:
        pos += 1
    elif arv < 0:
        neg += 1
    else:
        nullid += 1

print("Positiivseid:", pos, "Negatiivseid:", neg, "Nulle:", nullid)



# 7️⃣ Väljastada ekraanile arvud, mis on K-ga jaguvad vahemikust [A, B].

a = int(input("Sisesta vahemiku algus A: "))
b = int(input("Sisesta vahemiku lõpp B: "))
k = int(input("Sisesta jagaja K: "))

praegune = a
while True:
    if praegune > b:
        break
    if praegune % k == 0:
        print(praegune)
    praegune += 1



# 8️⃣ Koosta programm, mis prindib tollide ja sentimeetrite teisendustabeli
# (1 toll = 2,5 cm) väärtuste jaoks 1 kuni 20 tolli.

toll = 1
while toll <= 20:
    cm = toll * 2.5
    print(toll, "tolli =", cm, "cm")
    toll += 1



# 9️⃣ Panka pandi S eurot 3% intressiga.
# Määrata, kui suureks summa muutub N aasta järel.

s = float(input("Sisesta algsumma S: "))
n = int(input("Mitu aastat? "))

for aasta in range(n):
    intress = s * 0.03
    s = s + intress

print("Summa pärast", n, "aastat on:", round(s, 2))



# 🔟 Klaviatuurilt sisestatakse 10 arvu paari.
# Võrdle igas paaris olevaid arve ja väljasta neist suurem arv.

loendur = 0
while loendur < 10:
    a = float(input("Sisesta esimene arv: "))
    b = float(input("Sisesta teine arv: "))
    if a > b:
        print("Suurem:", a)
    elif b > a:
        print("Suurem:", b)
    else:
        print("Arvud on võrdsed")
    loendur += 1



# 1️⃣1️⃣ Leia kahekohaliste paaritute arvude korrutis, mis on jaguvad juhuslikult genereeritud arvuga.

import random

juhuslik = random.randint(1, 20)
print("Juhuslik arv on:", juhuslik)

korrutis = 1
arv = 10
leitud = False

while True:
    if arv > 99:
        break
    if arv % 2 != 0 and arv % juhuslik == 0:
        korrutis = korrutis * arv
        leitud = True
    arv += 1

if leitud:
    print("Korrutis on:", korrutis)
else:
    print("Sobivaid arve pole")



# 1️⃣2️⃣ Heina niitmise brigaadis on N niidukit.
# Esimene niiduk töötas m tundi, iga järgmine 10 minutit rohkem kui eelmine.
# Leia, kui mitu tundi töötas kogu brigaad kokku.

n = int(input("Mitu niidukit? "))
m = float(input("Esimese niiduki aeg tundides: "))

koguaeg = 0
aeg = m

for i in range(n):
    koguaeg = koguaeg + aeg
    aeg = aeg + 10 / 60

print("Kogu brigaad töötas:", round(koguaeg, 2), "tundi")



# 1️⃣3️⃣ Leia kõik naturaalarvud 100-st kuni 1000-ni, mis on 7-ga jaguvad.
# Arvuta ka nende arv ja summa.

arv = 100
kogus = 0
summa = 0

while arv <= 1000:
    if arv % 7 == 0:
        print(arv)
        kogus += 1
        summa += arv
    arv += 1

print("Kogus:", kogus)
print("Summa:", summa)



# 1️⃣4️⃣ Koosta programm, mis arvutab korrutise arvudest 1 kuni N.
# N väärtus genereeritakse juhuslikult.

import random

n = random.randint(1, 15)
print("Juhuslik N on:", n)

korrutis = 1
i = 1
while i <= n:
    korrutis *= i
    i += 1

print("Korrutis on:", korrutis)



# 1️⃣5️⃣ Kirjuta programm, mis väljastab 10 rida, igal real arvud 0-st kuni 9-ni, näiteks:
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# ...................
# 0 1 2 3 4 5 6 7 8 9

for rida in range(10):
    for arv in range(10):
        print(arv, end=" ")
    print()



# 1️⃣6️⃣ Kirjutage programm, mis väljastab veeruna read järgmises vormis:
# 1 0 0 0 0 0 0 0 0
# 0 2 0 0 0 0 0 0 0
# 0 0 3 0 0 0 0 0 0
# 0 0 0 4 0 0 0 0 0
# 0 0 0 0 5 0 0 0 0
# 0 0 0 0 0 6 0 0 0
# 0 0 0 0 0 0 7 0 0
# 0 0 0 0 0 0 0 8 0
# 0 0 0 0 0 0 0 0 9

for rida in range(1, 10):
    for veerg in range(1, 10):
        if rida == veerg:
            print(rida, end=" ")
        else:
            print(0, end=" ")
    print()



# 1️⃣7️⃣Kirjutage programm, mis väljastab veeruna kasutaja määratud arvu korrutustabeli järgmises vormis:
# 2*1=2
# 2*2=4
# 2*3=6
# 2*4=8
# 2*5=10
# 2*6=12
# 2*7=14
# 2*8=16
# 2*9=18

arv = int(input("Sisesta arv: "))
i = 1
while i <= 9:
    print(f"{arv}*{i}={arv * i}")
    i += 1



# 1️⃣8️⃣ Antud on naturaalarvud 20-st kuni 50-ni. Väljasta need arvud, mis jaguvad 3-ga, kuid ei jaga 5-ga.

arv = 20
while True:
    if arv > 50:
        break
    if arv % 3 == 0 and arv % 5 != 0:
        print(arv)
    arv += 1



# 1️⃣9️⃣ Antud on naturaalarvud 35-st kuni 87-ni. Leia ja väljasta need arvud, mille jagamisel 7-ga jääk on 1, 2 või 5.

for arv in range(35, 88):
    jaak = arv % 7
    if jaak == 1 or jaak == 2 or jaak == 5:
        print(arv)



# 2️⃣0️⃣   Antud on naturaalarvud 1-st kuni 50-ni. Leia nende arvude summa, mis jaguvad 5 või 7-ga. 

arv = 1
summa = 0
while arv <= 50:
    if arv % 5 == 0 or arv % 7 == 0:
        summa += arv
    arv += 1
print("Summa on:", summa)



# 2️⃣1️⃣ Klaviatuurilt sisestatakse 10 arvu – nii positiivseid kui ka negatiivseid.
# Asenda kõik negatiivsed arvud nende absoluutväärtustega ja väljasta saadud 10 arvu.

loendur = 0
while True:
    arv = float(input("Sisesta arv: "))
    if arv < 0:
        arv = abs(arv)
    print("Tulemus:", arv)
    loendur += 1
    if loendur == 10:
        break



# 2️⃣2️⃣    Leia arvude 100 kuni 200 summa, mis on 17-ga jaguvad.
 
summa = 0
for arv in range(100, 201):
    if arv % 17 == 0:
        summa += arv
print("17-ga jaguvate arvude summa on:", summa)



# 2️⃣3️⃣   Arvutisse sisestatakse N punkti koordinaadid.
# Määrata, mitu neist punktidest jääb raadiusega R ringi sisse, mille keskpunkt on punktis (a, b).

n = int(input("Mitu punkti sisestad? "))
r = float(input("Sisesta ringi raadius R: "))
a = float(input("Sisesta keskpunkti koordinaat a: "))
b = float(input("Sisesta keskpunkti koordinaat b: "))

sees = 0
loendur = 0
while loendur < n:
    x = float(input("Sisesta punkti x: "))
    y = float(input("Sisesta punkti y: "))
    if (x - a) ** 2 + (y - b) ** 2 <= r ** 2:
        sees += 1
    loendur += 1

print("Ringi sisse jäi punkte:", sees)



# 2️⃣4️⃣  Arvutisse sisestatakse järjest N õpilase pikkused.
# Määrata klasside õpilaste keskmine pikkus.

n = int(input("Mitu õpilast on klassis? "))
summa = 0
loendur = 0

while True:
    if loendur >= n:
        break
    pikkus = float(input("Sisesta õpilase pikkus (cm): "))
    summa += pikkus
    loendur += 1

keskmine = summa / n
print("Õpilaste keskmine pikkus on:", round(keskmine, 1))



# 2️⃣5️⃣  Antud on naturaalarv N.
# Leia, mitu naturaalarvu, mis ei ületa N, ei jagu ühegagi arvudest 2, 3 või 5.

n = int(input("Sisesta naturaalarv N: "))
kogus = 0

for arv in range(1, n + 1):
    if arv % 2 != 0 and arv % 3 != 0 and arv % 5 != 0:
        kogus += 1

print("Selliseid arve on:", kogus)



# 2️⃣6️⃣ Kaks kahekohalist arvu, mis on kirjutatud üksteise järel, moodustavad neljakohalise arvu, mis jagub nende korrutisega.
# Leia need arvud.

for a in range(10, 100):
    for b in range(10, 100):
        neljakohaline = a * 100 + b
        if neljakohaline % (a * b) == 0:
            print("Leitud arvud:", a, "ja", b)


 
# 2️⃣7️⃣Antud on kaks kahekohalist arvu A ja B.
# Nendest moodustatakse kaks neljakohalist arvu:
#     esimene saadakse, kui kirjutatakse esmalt A, seejärel B;
#     teine saadakse, kui kirjutatakse esmalt B, seejärel A.
#     Leia arvud A ja B, kui on teada, et esimene neljakohaline arv jagub 99-ga,
#     ja teine 49-ga.

a = 10
while a <= 99:
    b = 10
    while b <= 99:
        esimene = a * 100 + b
        teine = b * 100 + a
        if esimene % 99 == 0 and teine % 49 == 0:
            print("A =", a, "ja B =", b)
        b += 1
    a += 1



# 2️⃣8️⃣   Loo „mini-loterii” programm.
# Arvuti „mõtleb välja” suvalise arvu, ja kasutaja peab selle ära arvama.
# Lõpuks tuleb kuvada, mitu katset kasutaja tegi.

import random

salajane = random.randint(1, 20)
katsed = 0

while True:
    pakutud = int(input("Arva ära arv vahemikus 1 kuni 20: "))
    katsed += 1
    if pakutud == salajane:
        print("Õige! Arvasid ära", katsed, "katsega.")
        break
    elif pakutud < salajane:
        print("Otsitav arv on suurem.")
    else:
        print("Otsitav arv on väiksem.")



# 2️⃣9️⃣Kirjuta programm, mis väljastab veeruna read järgmisel kujul:
# x 0 0 0 0 0 0 0 0
# x x 0 0 0 0 0 0 0
# x 0 x 0 0 0 0 0 0
# x 0 0 x 0 0 0 0 0
# x 0 0 0 x 0 0 0 0
# x 0 0 0 0 x 0 0 0
# x 0 0 0 0 0 x 0 0
# x 0 0 0 0 0 0 x 0
# x 0 0 0 0 0 0 0 x

for rida in range(1, 10):
    for veerg in range(1, 10):
        if veerg == 1 or rida == veerg:
            print("x", end=" ")
        else:
            print(0, end=" ")
    print()



# 3️⃣0️⃣Programmis luuakse kaks juhuslikku arvu M ja N.
# Ekraanile väljastatakse kahes reas arvujadad:
# üks N-st M-ni ja teine M-st N-ni.

import random

m = random.randint(1, 15)
n = random.randint(1, 15)
print("M =", m, "ja N =", n)

i = n
while True:
    print(i, end=" ")
    if i == m:
        break
    if n < m:
        i += 1
    else:
        i -= 1
print()

j = m
while True:
    print(j, end=" ")
    if j == n:
        break
    if m < n:
        j += 1
    else:
        j -= 1
print()



# 3️⃣1️⃣Spongi Bob praeb kotlette 🍔
# Tal on K kotletti, ja ühele pannile mahub M kotletti.
# Arvuta, mitu täis pannitäit tuleb praadida ja mitu kotletti jääb viimaseks panniks.

k = int(input("Mitu kotletti on kokku (K)? "))
m = int(input("Mitu kotletti mahub pannile (M)? "))

pannitaied = 0
while k >= m:
    k -= m
    pannitaied += 1

print("Täis pannitäisi:", pannitaied)
print("Viimasele pannile jääb kotlette:", k)














