
def küsi_arv(tekst, tüüp=int):
    while True:
        try:
            if tekst == 1 or tekst == 2 or tekst == 3 or tekst == 4:
                return tüüp(input(tekst))
            break
        except ValueError:
            print(f"Vigane valik.")

while True:
    print("Vali programm:")
    print("1 - Kolmnurga kontroll")
    print("2 - Hinde arvutamine")
    print("3 - Pileti hind")
    print("4 - Sule programm")
    valik = küsi_arv("Sisesta valik (1-3) => ")

    if valik == 1:
        print("Kolmnurga kontroll")   
        while True:
            try:
                a = float(input("Sisesta 1. külje pikkus => "))                    # ei olnud float()
                b = float(input("Sisesta 2. külje pikkus => "))             # ei olnud viimase )
                c = float(input("Sisesta 3. külje pikkus => "))
                if a <= 0 or b <= 0 or c <= 0:
                    print("Küljad ei saa olla null!")
                    continue
                break
            except ValueError:
                print("Viga! Palun sisesta korrektne arv (murdarv või täisarv).")
        # print("Kolmnurga kontroll")                                               # ei olnud samasugused jutumärgid
        # a = float(input("Sisesta 1. külje pikkus => "))                                # ei olnud float()
        # b = float(input("Sisesta 2. külje pikkus => "))                                          # ei olnud viimase )
        # c = float(input("Sisesta 3. külje pikkus => "))
        if a + b > c or a + c > b or b + c > a:                                          # ei ole :
            print("Kolmnurk on olemas")
            if a == b == c:                                                               # peab olema == mitte =
                print("Kolmnurk on võrdkülgne")
            elif a == b or b == c:                                                # siin ei saa olla else peab olema elif ja pärast elif ei saa olla if
                print("Kolmnurk on võrdhaarne")
            elif (a == b and b == a) or (a == c and c == a) or (c == b and b == c):
                print("Kolmnurk on täisnurkne")
            else:
                print("Kolmnurk on erikülgne")                   # ei ole 4 tühikud
        else:
            print("Sellist kolmnurka ei ole olemas")
        print()
        continue

    if valik == 2:
        print("Hinde arvutamine")
        punktid = int(input("Sisesta punktide arv (0-100) => "))
        if punktid < 0 and punktid > 100:
            print("Vigane punktide arv")
        elif punktid >= 50:
            print("Hinne: 3")
        elif punktid >= 75:
            print("Hinne: 4")
        elif punktid >= 90:
            print("Hinne: 5")
        else:
            print("Hinne: 2")
        print()
        continue

    if valik == 3:
        print("Pileti hind")
        vanus = int(input("Sisesta oma vanus => "))
        if vanus < 7:
            print("Pilet on tasuta")
        elif 7 <= vanus <= 18 or vanus >= 65:                    # oli =>  aga peab olema >=
            print("Pileti hind on 3 €")
        else:
            print("Pileti hind on 6 €")                           # ei olnud )
        continue

    if valik == 4:
        break











