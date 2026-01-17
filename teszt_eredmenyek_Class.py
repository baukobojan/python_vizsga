class Eredmenyek():
    def __init__(self,sor):
        adatok = sor.strip().split(':')
        self.kategoria = str(adatok[0])
        self.feladat = str(adatok[1])
        self.pont = int(adatok[2])