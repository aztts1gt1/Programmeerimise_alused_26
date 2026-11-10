
# 1. Juku
# a. Kui eesnimi on Juku siis lähme Jukuga kinno. Aga teeme seda nii, kui nimi oli kirjutatud suurtähtedega.
# b. Lisa valiku, kus Juku vanuse alusel otsustate mis pilet talle vaja osta. (Tee kontroll, kas sisestatud arv on täisarv)
#     <6 aastad  - tasuta
#     6-14 - lastepilet
#     15-65 - täispilet
#     >65 - sooduspilet
#     <0 ja >100 viga andmetega

nimi = input("Sisesta eesnimi: ")
if nimi == "JUKU":
    print("Lähme Jukuga kinno!")
    vanus_sisend = input("Sisesta Juku vanus: ")
    if vanus_sisend.isdigit(): 
        vanus = int(vanus_sisend)
          
        if vanus < 0 or vanus > 100:
            print("Viga andmetega!")
        elif vanus < 6:
            print("Pilet: tasuta")
        elif 6 <= vanus <= 14:
            print("Pilet: lastepilet")
        elif 15 <= vanus <= 65:
            print("Pilet: täispilet")
        elif vanus > 65:
            print("Pilet: sooduspilet") 
            
    else:
        print("Viga! Sisestatud vanus peab olema täisarv.") 
else:
    print("Nimi ei olnud kirjutatud suurtähtedega JUKU või polnud see Juku. Kinno ei lähe.")



# 2 Pinginaabrid
# Küsi kahe inimese nimed. Kui nimed koosnevad ainult tähedest siis  teavita kasutajat, kas nad on täna pinginaabrid või ei mitte.

import random

nimi1 = input("Sisesta esimese inimese nimi: ").strip()
nimi2 = input("Sisesta teise inimese nimi: ").strip()

if nimi1.replace(" ", "").isalpha() and nimi2.replace(" ", "").isalpha():
    are_neighbors = random.choice([True, False])
    if are_neighbors:
        print(f"Jah! {nimi1} ja {nimi2} on täna pinginaabrid.")
    else:
        print(f"Ei, {nimi1} ja {nimi2} ei ole täna pinginaabrid.")
else:
    print("Viga: Nimed peavad koosnema ainult tähtedest!")



# 3 Remont
# Küsi ristkülikukujulise toa seinte pikkused ning arvuta põranda pindala. Küsi kasutajalt remondi tegemise soov, kui ta on positiivne, siis küsi kui palju maksab ruutmeeter ja leia põranda vahetamise hind
# Lisaküsimus: kas ta teeb remonti ise või teeb seda professionaali abiga? Kui tegemist on professionaaliga, siis palun arvutage välja, kui palju remont koos tööga maksab.

try:
    pikkus = float(input("Sisesta ruumi pikkus (meetrites): "))
    laius = float(input("Sisesta ruumi laius (meetrites): "))
    kõrgus = float(input("Sisesta ruumi kõrgus (meetrites): "))

    if pikkus > 0 and laius > 0 and kõrgus > 0:
        perimeeter = 2 * (pikkus + laius)
        seinte_pindala = perimeeter * kõrgus       
        print(f"\nRuumi ümbermõõt on: {perimeeter:.2f} meetrit.")
        print(f"Remonditavate seinte kogupindala on: {seinte_pindala:.2f} ruutmeetrit.")       
    else:
        print("Viga: Mõõtmed peavad olema positiivsed arvud!")
except ValueError:
    print("Viga: Palun sisesta mõõtmeteks ainult numbreid!")



 # 4 Allahindus
 # Leia 30% soodustusega hinna, kui alghind on suurem kui 700

alghind_sisend = input("Sisesta alghind: ")
if alghind_sisend.isdigit():
    alghind = float(alghind_sisend)
    
    if alghind > 700:
        soodushind = alghind * 0.7
        print(f"Uus hind 30% soodustusega on: {soodushind}")
    else:
        print(f"Alghind ei ole üle 700. Hind jääb samaks: {alghind}")
else:
    print("Viga! Palun sisesta alghinnaks ainult täisarv tähemärke kasutamata.")



#  5 Temperatuur
# Küsi temperatuur ning teata, kas see on üle 18 kraadi (soovitav toasoojus talvel)

temperatuur_sisend = input("Sisesta praegune temperatuur: ")
temperatuur = float(temperatuur_sisend)

if temperatuur > 18:
    print("Temperatuur on üle 18 kraadi.")
else:
    print("Temperatuur on 18 kraadi või alla selle.")

    

# 6 Pikkus
# Küsi inimese pikkus ning teata, kas ta on lühike, keskmine või pikk (piirid pane ise paika)

pikkus = int(input("Sisesta oma pikkus sentimeetrites (nt 175): "))

if pikkus < 165:
    print("Sa oled lühike.")
elif pikkus <= 185:
    print("Sa oled keskmist kasvu.")
else:
    print("Sa oled pikk.")



# 7 Pikkus ja sugu
# Küsi inimeselt pikkus ja sugu ning teata, kas ta on lühike, keskmine või pikk (mitu tingimusplokki võib olla üksteise sees).

sugu = input("Sisesta oma sugu (mees/naine): ").lower()
pikkus = int(input("Sisesta oma pikkus sentimeetrites: "))

if sugu == "mees":
    if pikkus < 170:
        print("Mehe kohta oled lühike.")
    elif pikkus <= 185:
        print("Mehe kohta oled keskmist kasvu.")
    else:
        print("Mehe kohta oled pikk.")

elif sugu == "naine":
    if pikkus < 160:
        print("Naise kohta oled lühike.")
    elif pikkus <= 175:
        print("Naise kohta oled keskmist kasvu.")
    else:
        print("Naise kohta oled pikk.")
        
else:
    print("Viga: Sugu polnud korrektselt sisestatud (vali mees või naine).")



# 8 Poes
# Küsi inimeselt poes eraldi kas ta soovib osta piima, saia, leiba jne. Loo juhuslikud hinnad ja küsi mitu tükki tahad osta, kui tahad. Teata, mis summa maksma läheb(Kuva ekraanil tšekk).









