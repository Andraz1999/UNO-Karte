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

VLECI = 'VLECI'

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

ZMAGA = 'ZMAGA'
PORAZ = 'PORAZ'

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
            izbira += self.smer
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
        if self.igralci[0] == IZPADEL:
            return True
        if self.igralci[1] == IZPADEL and self.igralci[2] == IZPADEL and self.igralci[3] == IZPADEL:
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
        roka = self.igralci[self.trenutni_igralec]
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
            return VLECI
        elif inteligenca < verjet_pet and (VLECI_PET, CRNA) in roka:
            return (VLECI_PET, CRNA)
        elif inteligenca < verjet_crne and crne != []:
            return random.choice(crne)
        elif inteligenca < verjet_pos and poseben != []:
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
    
    def zgorna_barvna_karta(self):
        to = []
        for i in self.zgorne_karte:
            to = [i] + to
        for i in to:
            if i[1] in [RDECA, RUMENA, MODRA, ZELENA]:
                return i
    def stanje(self):
        if self.konec_igre():
            if self.igralci[0] == []:
                return ZMAGA
            elif self.igralci[1] == IZPADEL and self.igralci[2] == IZPADEL and self.igralci[3] == IZPADEL:
                return ZMAGA
            else: 
                return PORAZ
        else:
            return V_SREDINI

##########################################################################################################
#Za Spletni vmesnik:
ZACETEK = 'ZACETEK'
V_SREDINI = 'V_SREDINI'

class Uno:
    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            for i in range(len(self.igre) + 1):
                if i not in self.igre.keys():
                    return i
        
    def nova_igra(self):
        igra = Igra()
        igra.priprava_za_igro()
        id = self.prost_id_igre()
        self.igre[id] = (igra, ZACETEK, 0, [])
        return id

    def poklic_karte0(self, id_igre, karta):
        igra = self.igre[id_igre][0]
        kazen = self.igre[id_igre][3]
        igra.poklic(karta)
        stanje = igra.stanje() 
        zgorna = self.zgorna_barvna_karta()
        self.igre[id_igre] = (igra, stanje, 1, kazen)

    def kaj_karta_naredi1(self, id_igre, kljuc=True):
        igra = self.igre[id_igre][0]
        stanje = self.igre[id_igre][1]
        kazen = self.igre[id_igre][3]
        vnos = igra.zgorne_karte[-1]
        if kljuc and vnos[1] in [RDECA, RUMENA, MODRA, ZELENA] and vnos in igra.igralci[igra.trenutni_igralec]:
            self.igre[id_igre] = (igra, stanje, 2, kazen)
        elif vnos == VLECI:
            nova = igra.igralci[igra.trenitni_igralec][-1]
            if nova in igra.mozne_izbire():
                self.igre[id_igre] = (igra, stanje, 3, kazen)
        elif vnos[0] == ZAMENJAJ_STRAN:
            igra.zamenjaj_smer()
            igra.nasledji()
            self.igre[id_igre] = (igra, stanje, 0, kazen)
        elif vnos[0] == STOP:
            igra.nasledji()
            igra.nasledji()
            self.igre[id_igre] = (igra, stanje, 0, kazen)
        elif vnos[0] == SPREMENI_BARVO:
            self.igre[id_igre] = (igra, stanje, 4, kazen)
        elif vnos[0] == VLECI_PET:
            zgorna = igra.zgorna_barvna_karta()
            igra.vleci_pet(zgorna[1])
            self.igre[id_igre] = (igra, stanje, 0, kazen)
        elif vnos[0] == VLECI_DVE:
            for _ in range(2):
                karta = random.choice(igra.trenutni_kupcek)
                igra.trenutni_kupcek.remove(karta)
                kazen.append(karta)
                if len(igra.trenutni_kupcek) < 1:
                    igra.zmesaj()
            igra.naslednji()
            if vnos in igra.igralci[igra.trenutni_igralec]:
                self.igre[id_igre] = (igra, stanje, 5, kazen)
            else:
                igra.igralci[igra.trenutni_igralec] += kazen
                kazen = []
                igra.naslednji
                self.igre[id_igre] = (igra, stanje, 0, kazen)
        elif vnos[0] == VLECI_STIRI:
            for _ in range(4):
                karta = random.choice(igra.trenutni_kupcek)
                igra.trenutni_kupcek.remove(karta)
                kazen.append(karta)
                if len(igra.trenutni_kupcek) < 1:
                    igra.zmesaj()
            igra.naslednji()
            if vnos in igra.igralci[igra.trenutni_igralec]:
                self.igre[id_igre] = (igra, stanje, 5, kazen)
            else:
                igra.igralci[igra.trenutni_igralec] += kazen
                kazen = []
                igra.naslednji
                self.igre[id_igre] = (igra, stanje, 0, kazen)
        else:
            igra.naslednji()
            self.igre[id_igre] = (igra, stanje, 0, kazen)


    def ali_dve_enaki2(self, id_igre, da=False):
        igra = self.igre[id_igre][0]
        stanje = self.igre[id_igre][1]
        kazen = self.igre[id_igre][3]
        vnos = igra.zgorne_karte[-1]
        if da:
            igra.poklic(vnos)
            igra.naslednji
        stanje = igra.stanje()
        self.igre[id_igre] = (igra, stanje, 0, kazen)


    def vleci3(self, id_igre, da=False):
        igra = self.igre[id_igre][0]
        stanje = self.igre[id_igre][1]
        kazen = self.igre[id_igre][3]
        vnos = igra.zgorne_karte[-1]
        nova = igra.igralci[igra.trenitni_igralec][-1]
        if da:
            igra.poklic(nova)
            stanje = igra.stanje()
            self.igre[id_igre] = (igra, stanje, 1, kazen)
            self.kaj_karta_naredi1(id_igre, False)
        else:
            igra.naslednji()
            self.igre[id_igre] = (igra, stanje, 0, kazen)

    def sprememba_barve4(self, id_igre, barva):
        igra = self.igre[id_igre][0]
        stanje = self.igre[id_igre][1]
        kazen = self.igre[id_igre][3]
        vnos = igra.zgorne_karte[-1]
        igra.sprememba_barve(barva)
        igra.naslednji()
        self.igre[id_igre] = (igra, stanje, 0, kazen)

    def vleci_kazen5(self, id_igre, da=False):
        igra = self.igre[id_igre][0]
        stanje = self.igre[id_igre][1]
        kazen = self.igre[id_igre][3]
        vnos = igra.zgorne_karte[-1]
        if da:
            igra.poklic(vnos)
            stanje = igra.stanje()
            self.igre[id_igre] = (igra, stanje, 1, kazen)
            self.kaj_karta_naredi1(id_igre, False)
        else:
            if vnos[0] == VLECI_DVE:
                n = 2
            elif vnos[0] == VLECI_STIRI:
                n = 4
            for _ in range(n):
                karta = random.choice(igra.trenutni_kupcek)
                igra.trenutni_kupcek.remove(karta)
                kazen.append(karta)
                if len(igra.trenutni_kupcek) < 1:
                    igra.zmesaj()
            igra.igralci[igra.trenutni_igralec] += kazen
            kazen = []
            igra.naslednji()
            stanje = stanje()
            self.igre[id_igre] = (igra, stanje, 0, kazen)




            




