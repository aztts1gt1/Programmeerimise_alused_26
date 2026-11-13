
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



# 8. Poes
# Küsi kasutajalt iga toote kohta eraldi, kas ta soovib seda osta: piim, sai, leib ja vähemalt kaks toodet veel.
#     Toodete hinnad loo juhuslikult moodulist random, näiteks round(random.uniform(0.5, 3), 2).
#     Kui kasutaja soovib toodet osta, küsi kogus. Kontrolli, et kogus on täisarv (isdigit()).
#     Lõpus kuva tšekk: iga ostetud toote nimi, kogus, hind ja summa ning kõige all kogusumma.

import random
tooted = ["piim", "sai", "leib", "juust", "õunad"]
hinnad = {}
for toode in tooted:
    hinnad[toode] = round(random.uniform(0.50, 5.00), 2)

ostukorv = []
kogusumma = 0.0

print("Tere tulemast poodi! Vasta 'jah' või 'ei'.\n")

for toode in tooted:
    hind = hinnad[toode]
    vastus = input(f"Kas soovid osta toodet '{toode}' (hind {hind:.2f} €)? ").strip().lower()
    
    if vastus == "jah":
        ostukorv.append(toode)
        kogusumma += hind

print("\n--- OSTUTŠEKK ---")
if ostukorv:
    for toode in ostukorv:
        print(f"- {toode.capitalize()}: {hinnad[toode]:.2f} €")
    print(f"Kokku tasuda: {kogusumma:.2f} €")
else:
    print("Ostukorv on tühi.")


# 9. Ruut
# Kasutaja sisestab nelinurga nelja külje pikkused. Programm teatab, kas tegemist saab olla ruuduga (kõik küljed on võrdsed). Kontrolli ka, et kõik pikkused on positiivsed.
# Koosta programmi kohta plokkskeem ja salvesta see PNG-pildina programmiga samasse kausta.

a = float(input("Sisesta esimese külje pikkus: "))
b = float(input("Sisesta teise külje pikkus: "))
c = float(input("Sisesta kolmanda külje pikkus: "))
d = float(input("Sisesta neljanda külje pikkus: "))

if a <= 0 or b <= 0 or c <= 0 or d <= 0:
    print("Viga! Kõik külgede pikkused peavad olema positiivsed.")
elif a == b == c == d:
    print("Tegemist saab olla ruuduga.")
else:
    print("Tegemist ei ole ruuduga, sest küljed ei ole võrdsed.")



# 10. Matemaatika
# Kasutaja sisestab kaks arvu. Seejärel küsib programm, millist tehet ta soovib (+, -, *, /), ja kuvab tulemuse.
#     Kui sisestatakse tundmatu tehtemärk, kuva veateade.
#     Nulliga jagamise korral kuva arusaadav teade, mitte veateade Pythonist.
# Koosta programmi kohta plokkskeem ja salvesta see PNG-pildina programmiga samasse kausta.

arv1 = float(input("Sisesta esimene arv: "))
arv2 = float(input("Sisesta teine arv: "))
tehe = input("Vali tehe (+, -, *, /): ")

if tehe == "+":
    print("Tulemus:", arv1 + arv2)
elif tehe == "-":
    print("Tulemus:", arv1 - arv2)
elif tehe == "*":
    print("Tulemus:", arv1 * arv2)
elif tehe == "/":
    if arv2 == 0:
        print("Viga! Nulliga jagada ei saa.")
    else:
        print("Tulemus:", arv1 / arv2)
else:
    print("Viga! Tundmatu tehtemärk.")



# 11. Juubel
# Kasutaja sisestab oma sünniaasta. Programm arvutab, mitu aastat ta sel aastal saab, ja ütleb, kas tegemist on juubeliga (vanus jagub 10-ga). Kui ei ole, ütle, mitu aastat on järgmise juubelini.
# Vihje: jooksva aasta saad date.today().year abil, jäägi % abil.
# Plokkskeemi pole vaja.

from datetime import date

sünniaasta = int(input("Sisesta oma sünniaasta: "))
praegune_aasta = date.today().year
vanus = praegune_aasta - sünniaasta

print(f"Sa saad sel aastal {vanus}-aastaseks.")

if vanus % 10 == 0:
    print("Palju õnne! Tegemist on juubeliga!")
else:
    aastaid_juubelini = 10 - (vanus % 10)
    print(f"Tegemist ei ole juubeliga. Järgmise juubelini on {aastaid_juubelini} aastat.")



# 12. Müük
# Kasutaja sisestab toote hinna. Kui hind on kuni 10 eurot, saab ta 10% allahindlust. Üle 10 euro maksvad tooted saavad 20% allahindlust. Kuva toote lõplik hind kahe komakohaga.
# Plokkskeemi pole vaja.

hind = float(input("Sisesta toote hind (€): "))

if hind <= 0:
    print("Viga! Hind peab olema positiivne arv.")
elif hind <= 10:
    lõplik_hind = hind * 0.90
    print(f"Rakendus 10% allahindlus. Lõplik hind on {lõplik_hind:.2f} €.")
else:
    lõplik_hind = hind * 0.80
    print(f"Rakendus 20% allahindlus. Lõplik hind on {lõplik_hind:.2f} €.")



# 13. Jalgpallimeeskond
# Loo programm, mis kontrollib, kas kandideerija sobib meeskonda. Meeskonda võetakse ainult 16–18-aastaseid mehi.
#     Küsi kõigepealt sugu.
#     Kui kandideerija on naissoost, siis vanust üldse ei küsita ja programm teatab kohe, et ta ei sobi.
#     Meessoost kandideerijalt küsi vanus ja kontrolli, kas see jääb vahemikku 16–18.

sugu = input("Sisesta oma sugu (M/N või mees/naine): ").strip().lower()

if sugu == "m" or sugu == "mees":
    vanus = int(input("Sisesta oma vanus: "))
    if 16 <= vanus <= 18:
        print("Palju õnne! Sa sobid meeskonda.")
    else:
        print("Kahjuks sa ei sobi meeskonda vanuse tõttu (lubatud vanus on 16–18).")
elif sugu == "n" or sugu == "naine":
    print("Kahjuks sa ei sobi, sest meeskonda võetakse ainult mehi.")
else:
    print("Viga! Tundmatu sugu.")



# 14. Busside logistika
# On vaja transportida teatud arv inimesi bussidega, milles on teatud arv kohti. Programm küsib inimeste arvu ja ühe bussi kohtade arvu ning arvutab:
#     mitu bussi on vaja, et kõik inimesed kohale saaksid;
#     mitu inimest on viimases bussis, kui kõik eelmised bussid on täiesti täis.
# Kontrolli, et mõlemad sisestatud arvud on positiivsed täisarvud.
# Vihje: kasuta täisarvulist jagamist // ja jääki %. Mõtle, mis juhtub, kui inimesed mahuvad bussidesse täpselt ära.

inimesed_sisend = input("Sisesta inimeste arv: ")
kohad_sisend = input("Sisesta ühe bussi kohtade arv: ")

if inimesed_sisend.isdigit() and kohad_sisend.isdigit():
    inimesed = int(inimesed_sisend)
    kohad = int(kohad_sisend)

    if inimesed <= 0 or kohad <= 0:
        print("Viga! Mõlemad arvud peavad olema positiivsed täisarvud.")
    else:
        täis_busse = inimesed // kohad
        jaak = inimesed % kohad

        if jaak == 0:
            busse_kokku = täis_busse
            viimases_bussis = kohad
        else:
            busse_kokku = täis_busse + 1
            viimases_bussis = jaak

        print(f"Vaja on {busse_kokku} bussi.")
        print(f"Viimases bussis on {viimases_bussis} inimest.")
else:
    print("Viga! Palun sisesta ainult positiivsed täisarvud.")









































