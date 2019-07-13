import random

RDECA = 'rd'
RUMENA = 'ru'
MODRA = 'mo'
ZELENA = 'ze'
CRNA = 'cr'
ZAMENJAJ_STRAN = ' ⟳'
STOP = 'st'
SPREMENI_BARVO = 'sp'
VLECI_DVE = '+2'
VLECI_STIRI = '+4'
VLECI_PET = '+5'

VLECI = 'vleci'

BARVNE = []
for _ in range(2):
    for i in range(10):
        stevilo = ' ' + str(i)
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
IZPADEL = 'IZPADEL'

ZMAGA = 'ZMAGA!'


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
        if len(self.trenutni_kupcek) < 1:
            self.zmesaj()

    def naslednji(self):
        self.naslednji_zacetek()
        while self.igralci[self.trenutni_igralec] == [] or self.igralci[self.trenutni_igralec] == IZPADEL:
            self.naslednji_zacetek()

    def naslednji_bi(self):
        izbira = self.trenutni_igralec + self.smer
        if izbira < 0:
            izbira = 3
        if izbira > 3:
            izbira = 0
        while self.igralci[izbira] == [] or self.igralci[izbira] == IZPADEL:
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

    def izpadel(self):
        for i in range(4):
            if len(self.igralci[i]) > NAJVECJE_STEVILO_KART:
                self.igralci[i] = IZPADEL

    def zacetna(self):
        karta = random.choice(BARVNE)
        self.trenutni_kupcek.remove(karta)
        self.zgorne_karte.append(karta)
    
    def poklic(self, karta):
        if karta == VLECI:
            self.vleci()
    #        print(self.igralci)
    #        print(self.zgorne_karte)
            return
        self.zgorne_karte.append(karta)
        if len(self.zgorne_karte) > 5:
            self.zgorne_karte.pop(0)
        self.igralci[self.trenutni_igralec].remove(karta)
     #   print(self.igralci)
     #   print(self.zgorne_karte)

    def priprava_za_igro(self):
        self.trenutni_kupcek = CELOTNI_KUPCEK.copy()
        self.zacetna()
        while len(self.igralci[3]) < ZACETNO_STEVILO_KART:
            self.vleci()
            self.naslednji_zacetek()
        self.trenutni_igralec = 0

    def konec_igre(self):
        if self.igralci[0] == IZPADEL:
            return True
        igralci = 0
        for i in self.igralci:
            if i == []:
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

    def vleci_pet(self, barva):
        grom = self.trenutni_igralec 
        self.naslednji()
        while grom != self.trenutni_igralec:
            self.vleci()
            self.vleci()
            self.vleci()
            self.vleci()
            self.vleci()
            self.naslednji()
        self.zgorne_karte.append((barva, barva))
        if len(self.zgorne_karte) > 5:
            self.zgorne_karte.pop(0)

    def sprememba_barve(self, barva):
        self.zgorne_karte.append((barva, barva))
        if len(self.zgorne_karte) > 5:
            self.zgorne_karte.pop(0)

    def stop(self):
        self.trenutni_igralec += self.smer

    def zamenjaj_smer(self):
        self.smer *= -1
    
    def plus2(self, sez):
        for _ in range(2):
            karta = random.choice(self.trenutni_kupcek)
            self.trenutni_kupcek.remove(karta)
            if len(self.trenutni_kupcek) < 1:
                self.zmesaj()
            sez.append(karta)


    def verjetnost_vleci(self):
        verjetnost = 0.02
        mozni = self.mozne_izbire()
        nasled = self.naslednji_bi()
        poseben = []
        for i in mozni:
            if i[0] == ZAMENJAJ_STRAN or i[0] == STOP:
                poseben.append(i)
        crne = []
        for i in mozni:
            if i[1] == CRNA:
                crne.append(i)
        if len(self.igralci[nasled]) == 1:
            if crne == [] and poseben == []:
                verjetnost += 1
        return verjetnost


    def verjetnost_posebni(self):
        mozni = self.mozne_izbire()
        nasled = self.naslednji_bi()
        poseben = []
        for i in mozni:
            if i[0] == ZAMENJAJ_STRAN or i[0] == STOP:
                poseben.append(i)
        verjetnost = 0
        if poseben != []:
            verjetnost += 0.1
            if len(self.igralci[nasled]) <= 3:
                    verjetnost += 0.1
            if len(self.igralci[self.trenutni_igralec]) <= 3:
                verjetnost += 0.1
        return verjetnost

    def verjetnost_pet(self):
        mozni = self.mozne_izbire()
        nasled = self.naslednji_bi()
        verjetnost = 0
        if (VLECI_PET, CRNA) in mozni:
            verjetnost += 0.02
            stevilo_kart = 0
            for i in range(4):
                if i == self.trenutni_igralec:
                    pass
                else:
                    for j in self.igralci[i]:
                        stevilo_kart += 1
            if stevilo_kart <= 8:
                verjetnost += 0.4
            if len(self.igralci[nasled]) <= 3:
                verjetnost += 0.1
            if len(self.igralci[self.trenutni_igralec]) <= 3:
                    verjetnost /= 2
        return verjetnost

    def verjetnost_crne(self):
        mozni = self.mozne_izbire()
        nasled = self.naslednji_bi()
        verjetnost = 0
        crne = []
        for i in mozni:
            if i[1] == CRNA:
                crne.append(i)
        if crne != []:
            verjetnost += 0.1
            if len(self.igralci[nasled]) <= 4:
                    verjetnost += 0.05
            if len(self.igralci[nasled]) <= 3:
                    verjetnost += 0.05
            if len(self.igralci[nasled]) <= 1:
                    verjetnost += 0.1
            if len(self.igralci[self.trenutni_igralec]) <= 3:
                verjetnost /= 2 
        return verjetnost



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
        if (VLECI_PET, CRNA) in crne:
            crne.remove((VLECI_PET, CRNA))
     ######################################
        verjet_vleci = self.verjetnost_vleci()
        verjet_pet = self.verjetnost_pet() + verjet_vleci
        verjet_crne = verjet_pet + self.verjetnost_crne()
        verjet_pos = verjet_crne + self.verjetnost_posebni()

        inteligenca = random.random()
        if inteligenca < verjet_vleci:
            return 'VLECI'
        if inteligenca < verjet_pet:
            return (VLECI_PET, CRNA)
        if inteligenca < verjet_crne:
            return random.choice(crne)
        if inteligenca < verjet_pos:
            return random.choice(poseben)
        for i in mozni:
            n = mozni.count(i)
            if n > 1:
                return i
        if mozni != []:
            return random.choice(mozni)
        mozni = self.mozne_izbire()
        return random.choice(mozni)


    def dvakrat(self):
        gledamo = self.zgorne_karte[-1]
        return gledamo in self.igralci[self.trenutni_igralec]
        
    def nasprotnik_barva(self):
        seznam = []
        for karta in self.igralci[self.trenutni_igralec]:
            if karta in BARVNE or karta in POSEBNE_BARVNE:
                seznam.append(karta)
        if seznam == []:
            return random.choice[RDECA, RUMENA, MODRA, ZELENA]
        izbira = random.choice(seznam)
        return izbira[1]


    
#
#a = Igra()
#a.priprava_za_igro()
#while len(a.igralci[a.trenutni_igralec]) < 21:
#    a.vleci()
#a.izpadel()
#print(len(a.igralci[a.trenutni_igralec]))





