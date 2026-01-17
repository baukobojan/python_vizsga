def eldontes_szamitas():
    global orak_szama
    hany_orat_tanult = int(input("Add meg a heti tanulással töltött órák számát!\n "))
    orak_szama = hany_orat_tanult

    def ertekeles():
        if orak_szama >= 0 and orak_szama <= 4:
            return "Nem elegendő felkészülés"
        elif orak_szama >= 5 and orak_szama <= 9:
            return "Megfelelő felkészülés"
        elif orak_szama >= 10:
            return "Kiemelkedő szorgalom"
        else:
            return "Hibás adat"

    jegy_ertekeles = ertekeles()
    print(f"I/A, B:\n     {hany_orat_tanult}\nI/C:\n     {jegy_ertekeles}")



