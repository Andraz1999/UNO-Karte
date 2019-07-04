import random

RDECA = 'rd'
RUMENA = 'ru'
MODRA = 'mo'
ZELENA = 'ze'
CRNA = 'cr'
ZAMENJAJ_STRAN = '⟳'
STOP = 'stop'
SPREMENI_BARVO = 'sp'
VLECI_DVE = '+2'
VLECI_STIRI = '+4'
VLECI_PET = '+5'

VLECI = 'vleci'

BARVNE = []
for _ in range(2):
    for stevilo in range(10):
        for barva in [RDECA, RUMENA, MODRA, ZELENA]:
            BARVNE.append((stevilo, barva))

POSEBNE_BARVNE = []
for _ in range(2):
    for stevilo in [ZAMENJAJ_STRAN, STOP]:
        for barva in [RDECA, RUMENA, MODRA, ZELENA]:
            POSEBNE_BARVNE.append((stevilo, barva))

CRNE = []
CRNE.append((VLECI_PET, CRNA))
for _ in range(8):
    CRNE.append((VLECI_DVE, CRNA))
for _ in range(4):
    CRNE.append((VLECI_STIRI, CRNA))
    CRNE.append((SPREMENI_BARVO, CRNA))

CELOTNI_KUPCEK = BARVNE.copy() + POSEBNE_BARVNE.copy() + CRNE.copy()

ZACETNO_STEVILO_KART = 7
NAJVECJE_STEVILO_KART = 20

ZMAGA = 'Z'


class Igra:

    def __init__(self):
        self.igralci = [[],[],[],[]]
        self.trenutni_kupcek = CELOTNI_KUPCEK.copy()
        self.zgorne_karte = []
        self.smer = 1
        self.trenutni_igralec = 0

    def vleci(self):
        karta = random.choice(self.trenutni_kupcek)
        self.trenutni_kupcek.remove(karta)
        self.igralci[self.trenutni_igralec].append(karta)

    def naslednji(self):
        self.naslednji_zacetek()
        while self.igralci[self.trenutni_igralec] == []:
            self.naslednji_zacetek()

    def naslednji_bi(self):
        izbira = self.trenutni_igralec + self.smer
        if izbira < 0:
            izbira = 3
        if izbira > 3:
            izbira = 0
        while self.igralci[izbira] == []:
            izbira = self.trenutni_igralec + self.smer
        if izbira < 0:
            izbira = 3
        if izbira > 3:
            izbira = 0
        return izbira

    def naslednji_zacetek(self):
        self.trenutni_igralec += self.smer
        if self.trenutni_igralec < 0:
            self.trenutni_igralec = 3
        if self.trenutni_igralec > 3:
            self.trenutni_igralec = 0

    def zmesaj(self):
        self.trenutni_kupcek = CELOTNI_KUPCEK.copy()

    def zacetna(self):
        karta = random.choice(BARVNE)
        self.trenutni_kupcek.remove(karta)
        self.zgorne_karte.append(karta)
    
    def poklic(self, karta):
        if karta == VLECI:
            self.vleci()
            return
        self.zgorne_karte.append(karta)
        if len(self.zgorne_karte) > 5:
            self.zgorne_karte.pop(0)
        self.igralci[self.trenutni_igralec].remove(karta)

    def priprava_za_igro(self):
        self.trenutni_kupcek = CELOTNI_KUPCEK.copy()
        self.zacetna()
        while len(self.igralci[3]) < ZACETNO_STEVILO_KART:
            self.vleci()
            self.naslednji_zacetek()
        self.trenutni_igralec = 0

    def konec_igre(self):
        igralci = 0
        for i in self.igralci:
            if i != []:
                igralci += 1
        return igralci == 1

    def mozne_izbire(self):
        vrhnja = self.zgorne_karte[-1]
        roka = self.igralci[self.trenutni_igralec]
        mozni = []
        for i in roka:
            if i[1] == CRNA:
                mozni.append(i)
            elif vrhnja[0] == i[0] or vrhnja[1] == i[1]:
                mozni.append(i)
        return mozni

    def nasprotnik(self):
        mozni = self.mozne_izbire()
        if mozni == []:
            return VLECI
        nasled = self.naslednji_bi()
        poseben = []
        for i in mozni:
            if i[0] == ZAMENJAJ_STRAN or i[0] == STOP:
                poseben.append(i)
                mozni.remove(i)
        crne = []
        for i in mozni:
            if i[1] == CRNA:
                crne.append(i)
                mozni.remove(i)
        verjetnost_za_pet = 0
        if (VLECI_PET, CRNA) in crne:
            grom = (VLECI_PET, CRNA)
            crne.remove((VLECI_PET, CRNA))
            verjetnost_za_pet += 0.02
            stevilo_kart = 0
            for i in range(4):
                if i == self.trenutni_igralec:
                    pass
                else:
                    for j in self.igralci[i]:
                        stevilo_kart += 1
            if stevilo_kart <= 8:
                verjetnost_za_pet = 0.4
            if len(self.igralci[nasled]) <= 3:
                verjetnost_za_pet += 0.1
            if len(self.igralci[self.trenutni_igralec]) <= 3:
                verjetnost_za_pet /= 2
        verjetnost_za_crne = verjetnost_za_pet
        if crne != []:
            verjetnost_za_crne += 0.1
            if len(self.igralci[nasled]) <= 4:
                    verjetnost_za_crne += 0.1
            if len(self.igralci[nasled]) <= 3:
                    verjetnost_za_crne += 0.1
            if len(self.igralci[nasled]) <= 1:
                    verjetnost_za_crne += 0.1
            if len(self.igralci[self.trenutni_igralec]) <= 3:
                verjetnost_za_crne = (verjetnost_za_crne + verjetnost_za_pet) / 2   
        verjetnost_za_posebne = verjetnost_za_crne
        if poseben != []:
            verjetnost_za_posebne += 0.2
            if len(self.igralci[nasled]) <= 3:
                    verjetnost_za_posebne += 0.1
        inteligenca = random.random()
        if inteligenca < verjetnost_za_pet:
            return (VLECI_PET, CRNA)
        if inteligenca < verjetnost_za_crne:
            return random.choice(crne)
        if inteligenca < verjetnost_za_posebne:
            return random.choice(poseben)
        for i in mozni:
            n = mozni.count(i)
            if n > 1:
                return i
        return random.choice(mozni)











