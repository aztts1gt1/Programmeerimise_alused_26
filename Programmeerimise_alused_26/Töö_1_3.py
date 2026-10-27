
# Ülesanne 1.
# Kirjuta programm, mis sind tervitab ja kuvab ekraanile tänane kuupäev moduli datetime kasutades ja date.today() funktsiooni abil.
# from datetime import *
# tana=date.today()
# print(f"Täna on {tana}")
# Kasuta erinevate formaatide kuvamiseks ekraanile järgmised funktsioonid:
# # 27/12/2022
# tana = tana.strftime("%d/%m/%Y")
# # December 27, 2022
# tana = tana.strftime("%B %d, %Y")
# # 12/27/22
# tana = tana.strftime("%m/%d/%y")
# # Dec-27-2022
# tana = tana.strftime("%b-%d-%Y")
# Omadused day, month, year kasutatakse päeva, kuu ja aasta parameetri leidmiseks date klassist.
# Arvuta mitu päeva on jäänud kuu lõpuni, aasta lõpuni.
# Arvuta oma vanus aastates, kuudes ja päevades.
from calendar import *
from datetime import *
tana = date.today()
print(f"Täna on {tana}")

tana1 = tana.strftime("%d/%m/%Y")
print(f"Tere! \nTäna on {tana1}")

tana2 = tana.strftime("%B %d, %Y")
print(f"Tere! \nTäna on {tana2}")

tana3 = tana.strftime("%m/%d/%y")
print(f"Tere! \nTäna on {tana3}")

tana4 = tana.strftime("%b-%d-%Y")
print(f"Tere! \nTäna on {tana4}")


kuulõpuni = monthrange(tana.year, tana.month)[1] - tana.day
print("Kuu lõpuni on jäänud", kuulõpuni, "päeva.")
aastalõpuni = (date(tana.year, 12, 31) - tana).days
# date()-> 31.12.2026
# tana -> 27.10.2026
# days -> 65 päeva jäänud
print("Aasta lõpuni on jäänud", aastalõpuni, "päeva.")
sünnipäev = date(2010, 9, 2)
vanus = aastalõpuni//365
print("Oled", vanus, "aastat, ")
print((aastalõpuni%365)//30, "kuud ja")
print((aastalõpuni%365)%30, "päeva vana.")



# Ülesanne 2.
# Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?
# +Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
# +Katseta erinevaid kombinatsioone paralleelselt ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.

tulemus_1 = 3 + 8 / (4 - 2) * 4
tulemus_2 = 3 + 8 / 4 - 2 * 4
tulemus_3 = (3 + 8) / (4 - 2) * 4
tulemus_4 = 3 + 8 / ((4 - 2) * 4)
print(f"Algne tehe 3 + 8 / (4 - 2) * 4 vastus: {tulemus_1}")
print(f"Ilma sulgudeta tehe 3 + 8 / 4 - 2 * 4 vastus: {tulemus_2}")
print(f"Liitmine esimesena (3 + 8) / (4 - 2) * 4 vastus: {tulemus_3}")
print(f"Kogu jagaja sulgudes 3 + 8 / ((4 - 2) * 4) vastus: {tulemus_4}")



# Ülesanne 3.
# Ruudu sees asub ring. Ringi raadius on R.
# Leia ja väljasta ekraanile ruudu pindala, ruudu ümbermõõt, ringi pindala, ringi ümbermõõt.

import math
while True:
    try:
        R = float(input("Sisesta ringi raadius R: "))
        if R <= 0:
            print("Raadius peab olema suurem kui null!")
            continue
        break
    except ValueError:
        print("Viga! Palun sisesta korrektne arv (murdarv või täisarv).")
a = 2 * R
ruudu_pindala = a ** 2
ruudu_ümbermoot = 4 * a
ringi_pindala = math.pi * (R ** 2)
ringi_ümbermoot = 2 * math.pi * R
print(f"\nTulemused raadiusega R = {R}")
print(f"Ruudu pindala: {round(ruudu_pindala, 2)}")
print(f"Ruudu ümbermõõt: {round(ruudu_ümbermoot, 2)}")
print(f"Ringi pindala: {round(ringi_pindala, 2)}")
print(f"Ringi ümbermõõt: {round(ringi_ümbermoot, 2)}")




# Ülesanne 4.
# Koosta programm, mis arvutab välja Maa ümbermõõdu ekvaatori kohal 2-eurostes müntides ehk teisisõnu: 
# kui palju 2-euroseid münte tuleb panna üksteise kõrvale, 
# et rida ulatuks ümber Maa. Kasuta teadmist, 
# et Maa raadius ekvaatori kohal on 6378 km. 
# Algandmed (Maa raadius, mündi läbimõõt jne) omista programmi alguses sisukate nimedega muutujatele. Kuna ümbermõõdu arvutamiseks tuleb kasutada  PI-d (3,14...), siis võid selle (umbkaudse) väärtuse otse programmi kirjutada.  
# Püüdke välja mõelda viise, kuidas juhuslikest vigadest valemis hoiduda (teisendamised, ümardamise täpsus jne). Võimalusel võrrelge tulemusi teistega. Kui on erinevusi, leidke ühiselt põhjused.
# Kas programm on piisavalt hästi kirjutatud, et algandmete muutumise korral (näiteks juhul, kui on vaja arvutada Marsi ümbermõõtu 1-eurostes müntides) on parandusi selge ja lihtne teha?

maa_ümbermoot_km = 40075.017
mündi_diameeter_mm = 25.75
maa_ümbermoot_mm = maa_ümbermoot_km * 1000 * 1000
müntide_arv = maa_ümbermoot_mm / mündi_diameeter_mm
print(f"Maa ekvaatori kohal ümbermõõdu katmiseks läheb vaja umbes {round(müntide_arv):,} münti.")



# Ülesanne 5.
# Eelnevaid teadmisi kasutades kirjuta programm, mis väljastaks:
# kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll kill-koll
# kill-koll

osa1 = "kill-koll"
osa2 = "killadi-koll"
lause = f"{osa1} {osa1} {osa2} {osa1} {osa1} {osa2} {osa1}"
print(lause)
# VÕI
tekst = "kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll"
print(tekst.title())



# Ülesanne 6.
# Koosta programm, mis väljastaks järgmised laulusõnad suurte tähtedega:
#
# Rong see sõitis tsuhh tsuhh tsuhh,
# piilupart oli rongijuht.
# Rattad tegid rat tat taa,
# rat tat taa ja tat tat taa.
# Aga seal rongi peal,
# kas sa tead, kes olid seal?
#
# Rong see sõitis tuut tuut tuut,
# piilupart oli rongijuht.
# Rattad tegid kill koll koll,
# kill koll koll ja kill koll kill.
#
#
# ....Sisend, väljund, tingimus....

tekst = (
'''    
    Rong see sõitis tsuhh tsuhh tsuhh,
    piilupart oli rongijuht.
    Rattad tegid rat tat taa,
    rat tat taa ja tat tat taa.
    Aga seal rongi peal,
    kas sa tead, kes olid seal?

    Rong see sõitis tuut tuut tuut,
    piilupart oli rongijuht.
    Rattad tegid kill koll koll,
    kill koll koll ja kill koll kill.
'''
)
print(tekst.upper())



# Ülesanne 7.
# Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile ristküliku ümbermõõdu ja pindala.

while True:
    try:
        a = float(input("Sisesta esimese külje pikkus: "))
        b = float(input("Sisesta teise külje pikkus: "))
        if a <= 0 or b <= 0:
            print("Küljad ei saa olla null!")
            continue
        break
    except ValueError:
        print("Viga! Palun sisesta korrektne arv (murdarv või täisarv).")
ümbermoot = 2 * (a + b)
pindala = a * b
print(f"Ristküliku ümbermõõt on: {ümbermoot}")
print(f"Ristküliku pindala on: {pindala}")



# Ülesanne 8.
# Kütusekulu arvutamine
#
#     Kasutaja sisestab tangitud kütuse liitrid
#     Kasutaja sisestab läbitud kilomeetrid
#     Programm leiab kütusekulu 100km kohta keskmiselt

while True:
    try:
        tangitud_liitrid = float(input("Sisesta tangitud kütuse liitrid: "))
        labitud_kilomeetrid = float(input("Sisesta läbitud kilomeetrid: "))
        if labitud_kilomeetrid <= 0:
            print("Läbitud kilomeetrid peavad olema suuremad kui null!")
            continue
        break
    except ValueError:
        print("Viga! Palun sisesta korrektne arv (murdarv või täisarv).")
kutusekulu_100km = (tangitud_liitrid / labitud_kilomeetrid) * 100
print(f"\nSinu auto keskmine kütusekulu on {kutusekulu_100km:.2f} liitrit 100 km kohta.")



# Ülesanne 9.
# Rulluisutajad
#
#     Rulluisutaja keskmine kiirus on 29,9km/h
#     Kui kaugele jõuab M minutiga

kiirus_km_h = 29.9
while True:
    try:
        M = float(input("Sisesta aeg minutites (M): "))
        if M <= 0:
            print("Aeg ei saa olla negatiivne!")
            continue
        break
    except ValueError:
        print("Viga! Palun sisesta korrektne arv (murdarv või täisarv).")
aeg_tundides = M / 60
vahemaa_km = kiirus_km_h * aeg_tundides
print(f"Rulluisutaja jõuab {M} minutiga umbes {vahemaa_km:.2f} km kaugusele.")



# Ülesanne 10.
# Ajateisendus

#     Kasutaja sisestab aja minutites
#     Sinu valem leiab ja väljastab tunnid ja minutid
#     Näiteks: sisestus 72, vastus 1:12

while True:
    try:
        minutid_kokku = int(input("Sisesta aeg minutites: "))
        if minutid_kokku < 0:
            print("Aeg ei saa olla negatiivne!")
            continue
        break
    except ValueError:
        print("Viga! Palun sisesta korrektne arv (murdarv või täisarv).")
tunnid = minutid_kokku // 60
minutid = minutid_kokku % 60
print(f"Vastus {tunnid}:{minutid:02d}")





