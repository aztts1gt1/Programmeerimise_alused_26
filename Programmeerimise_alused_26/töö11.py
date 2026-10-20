
import random
import math

def küsi_arv(tekst, tüüp=float):
    while True:
        try:
            return tüüp(input(tekst))
        except ValueError:
            print(f"Viga! Palun sisesta korrektne arv ({'täisarv' if tüüp == int else 'murdarv'}).")




print("\n\n\n1. ülesanne: \n\n") # 1.
# Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
# “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”

print("Tere, maailm!")
nimi = input("Mis on sinu nimi? ")
print(f"Tere, maailm! Tervitan sind {nimi}")
vanus = küsi_arv("Kui vana sa oled? ", int)
print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")



print("\n\n\n2. ülesanne: \n\n") # 2.
# Mis tüüpi on järgnevad muutujad:
# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 16.5
# d) kas_käib_koolis = True
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
# Kirjuta kood tüüpide kontrollimiseks.
# Muutujate defineerimine

vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print("a tüüp on:", type(vanus))
print("b tüüp on:", type(eesnimi))
print("c tüüp on:", type(pikkus))
print("d tüüp on:", type(kas_käib_koolis))



print("\n\n\n3. ülesanne: \n\n") # 3.
# Kirjuta enda koodis laual olevate kommide arv muutujasse(kommide arv on juhuslik). Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
# Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, kui palju komme laual nüüd on. 

import random
kommide_arv = random.randint(1, 100)
print(f"Laual on alguses {kommide_arv} kommi.")
soovitud_kommid = küsi_arv("Mitu kommi sa soovid laualt ära võtta? ", int)
kommide_arv = kommide_arv - soovitud_kommid
print(f"Laual on nüüd {kommide_arv} kommi.")



print("\n\n\n4. ülesanne: \n\n") # 4.
# Puu läbimõõdu arvutamine
# Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.

import math
umbermõõt = küsi_arv("Mis on ümbermõõt? (cm): ")
labimõõt = umbermõõt / math.pi
print(f"Teie läbimõõt on: {round(labimõõt, 2)} cm.")



print("\n\n\n5. ülesanne: \n\n") # 5.
# Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.

import math
a = küsi_arv("Mis on teie esimene külg: ")
b = küsi_arv("Mis on teie teine külg: ")
print(f"Teie diagonaal on: {round(math.sqrt(a**2 + b**2), 2)}")



print("\n\n\n6. ülesanne: \n\n") # 6.
# Leidke järgnevast näiteprogrammist loogiline viga:
# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = aeg / teepikkus
# print("Sinu kiirus oli " + str(kiirus) + " km/h")

aeg = küsi_arv("Mitu tundi kulus sõiduks? ")
teepikkus = küsi_arv("Mitu kilomeetrit sõitsid? ")
try:
    kiirus = teepikkus / aeg
    print("Sinu kiirus oli " + str(kiirus) + " km/h")
except ZeroDivisionError:
    print("Viga! Aeg ei saa olla 0, kuna nulliga jagada ei saa.")



print("\n\n\n7. ülesanne: \n\n") # 7.
# Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.
# Leia nende arvude summa, jagatuna kasutaja poolt sisestatud arvuga, täisarvuline osa ja jääk.

a = küsi_arv("Teie esimene arv: ")
c = küsi_arv("Teie teine arv: ")
d = küsi_arv("Teie kolmas arv: ")
e = küsi_arv("Teie neljas arv: ")
f = küsi_arv("Teie viies arv: ")
summa = a + c + d + e + f
aritmeetiline = summa / 5
print(f"Viie arvu aritmeetiline keskmine on: {aritmeetiline}")
print(f"Arvude summa on: {summa}")
jagaja = küsi_arv("Sisestage arv, millega summa jagada: ")
try:
    taisarvuline_osa = summa // jagaja
    jaak = summa % jagaja
    print(f"Summa ja sisestatud arvu jagamise täisarvuline osa: {taisarvuline_osa}")
    print(f"Jagamise jääk: {jaak}")
except ZeroDivisionError:
    print("Viga! Nulliga jagamine ei ole lubatud.")



print("\n\n\n8. ülesanne: \n\n") # 8.
# Joonista samasugune konn

konn = """
    @..@
   (----)
  ( \__/ )
  ^^ "" ^^
"""
print(konn)


print("\n\n\n9. ülesanne: \n\n") # 9.
# Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Kasuta valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)

a = küsi_arv("Teie esimene arv: ", int)
b = küsi_arv("Teie teine arv: ", int)
c = küsi_arv("Teie kolmas arv: ", int)
kolmnurga_ümbermõõt = a + b + c
print(f"Teie kolmnurga ümbermõõt: {kolmnurga_ümbermõõt}")



print("\n\n\n10. ülesanne: \n\n") # 10.
# Pitsa
#     Võtsite sõpradega (näiteks P inimest) suure pitsa, mille hind on 12,90 €.
#     Jätate teenindajale 10% jootraha.
#     Koosta programm, mis arvutab, kui palju igaüks peab maksma.

inimesed = küsi_arv("Kui palju inimesi tuli?: ", int)
jootraha = 12.90 * 0.10 
kogusumma = 12.90 + jootraha
try:
    igaüks_maksab = kogusumma / inimesed
    print(f"Kogusumma pitsa ja jootraha: {kogusumma:.2f} €")
    print(f"Igaüks peab maksma: {igaüks_maksab:.2f} €")
except ZeroDivisionError:
    print("Viga! Inimeste arv ei saa olla 0.")






