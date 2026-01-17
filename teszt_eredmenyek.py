from teszt_eredmenyek_Class import *


def eredmenyek_szamitasa():
    adatok = []
    with open("KategóriaFeladatPont.txt", "r", encoding="UTF-8") as f:
        fejlec = f.readline()
        for sor in f:
            if sor.strip():
                valtozo = Eredmenyek(sor)
                adatok.append(valtozo)
    kategoria_adatok = []
    for m in adatok:
        if m.kategoria == "Alap":
            kategoria_adatok.append(m.pont)
    ossz_ertek = sum(kategoria_adatok)
    ossz_darab = len(kategoria_adatok)
    atlag = float(ossz_ertek % ossz_darab)
    print(f"III:")
    print(f"     Az alap szintű feladatok átlagpontszáma:{atlag}")




