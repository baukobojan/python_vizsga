def sorozat_szamitas():
    global szamok
    import random
    def eredmenyek():
        szamok = []
        for i in range(1, 8):
            szamok.append(random.randint(-2, 5))
        return szamok

    szamok = eredmenyek()

    def sikertelen():
        szamok2 = 0
        for i in szamok:
            if i < 0:
                szamok2 += 1

    negativ_szamok = sikertelen
    print(f"II/A,B:")
    print(f"        {eredmenyek()}\n")
    print(f"II/C, D:")
    print(f"        A sikertelen próbálkozások száma: {sikertelen()}.")


