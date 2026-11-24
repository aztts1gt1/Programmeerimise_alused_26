


while True:
    print("\nTee valik:")
    print("1. while-tsükkel")
    print("2. while True ja break")
    print("3. for-tsükkel")
    print("4. summa ja keskmine")
    print("5. loendamine ja suurim")
    print("0. Välju")

    valik = int(input("Vali tegevus: "))

    if valik == 1:
        x = 0
        while x < 30:
            if x % 2 == 1:
                print(x, end=" ")
            x += 1
        continue

    elif valik == 2:
        x = 0
        while True:
            if x % 2 == 1:
                print(x, end=" ")
            if x == 30:
                break
            x += 1
        continue

    elif valik == 3:
        for i in range(1, 31, 2):
            print(i, end=" ")
        continue

    elif valik == 4:
        N = int(input("N: "))
        summa = 0
        i = 1
        while i <= N:
            summa = summa + i
            i = i + 1
        print("Summa:", summa)
        print("Keskmine:", summa / N)
        continue

    elif valik == 5:
        kogus = 0
        suurim = None
        for i in range(5):
            arv = float(input(f"{i + 1}. arv: "))
            if arv > 0:
                kogus += 1
            if suurim is None or arv > suurim:
                suurim = arv
        print("Positiivseid arve:", kogus)
        print("Suurim arv:", suurim)
        continue

    elif valik == 0:
        print("Head aega.")
        break

    else:
        print("Vali teise numbri (0-6) sellest ei ole")
        continue













