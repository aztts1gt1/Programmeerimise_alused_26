
# Ülesanne 1.

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

tulemus_1 = 3 + 8 / (4 - 2) * 4
tulemus_2 = 3 + 8 / 4 - 2 * 4
tulemus_3 = (3 + 8) / (4 - 2) * 4
tulemus_4 = 3 + 8 / ((4 - 2) * 4)
print(f"Algne tehe 3 + 8 / (4 - 2) * 4 vastus: {tulemus_1}")
print(f"Ilma sulgudeta tehe 3 + 8 / 4 - 2 * 4 vastus: {tulemus_2}")
print(f"Liitmine esimesena (3 + 8) / (4 - 2) * 4 vastus: {tulemus_3}")
print(f"Kogu jagaja sulgudes 3 + 8 / ((4 - 2) * 4) vastus: {tulemus_4}")


# Ülesanne 3.

import math

R = float(input("Sisesta ringi raadius R: "))
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

maa_ümbermoot_km = 40075.017
mündi_diameeter_mm = 25.75
maa_ümbermoot_mm = maa_ümbermoot_km * 1000 * 1000
müntide_arv = maa_ümbermoot_mm / mündi_diameeter_mm
print(f"Maa ekvaatori kohal ümbermõõdu katmiseks läheb vaja umbes {round(müntide_arv):,} münti.")


# Ülesanne 5.

osa1 = "kill-koll"
osa2 = "killadi-koll"
lause = f"{osa1} {osa1} {osa2} {osa1} {osa1} {osa2} {osa1}"
print(lause)
# VÕI
tekst = "kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll"
print(tekst.title())


# Ülesanne 6.

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

a = float(input("Sisesta esimese külje pikkus: "))
b = float(input("Sisesta teise külje pikkus: "))
ümbermoot = 2 * (a + b)
pindala = a * b
print(f"Ristküliku ümbermõõt on: {ümbermoot}")
print(f"Ristküliku pindala on: {pindala}")


# Ülesanne 8.

tangitud_liitrid = float(input("Sisesta tangitud kütuse liitrid: "))
labitud_kilomeetrid = float(input("Sisesta läbitud kilomeetrid: "))
kutusekulu_100km = (tangitud_liitrid / labitud_kilomeetrid) * 100
print(f"\nSinu auto keskmine kütusekulu on {kutusekulu_100km:.2f} liitrit 100 km kohta.")


# Ülesanne 9.

kiirus_km_h = 29.9
M = float(input("Sisesta aeg minutites (M): "))
aeg_tundides = M / 60
vahemaa_km = kiirus_km_h * aeg_tundides
print(f"Rulluisutaja jõuab {M} minutiga umbes {vahemaa_km:.2f} km kaugusele.")


# Ülesanne 10.

minutid_kokku = int(input("Sisesta aeg minutites: "))
tunnid = minutid_kokku // 60
minutid = minutid_kokku % 60
print(f"Vastus {tunnid}:{minutid:02d}")





