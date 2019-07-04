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
        self.zgorne_karte.append(karta)
        if len(self.zgorne_karte) > 5:
            self.zgorne_karte.pop(0)
        self.igralci[self.trenutni_igralec].remove(karta)

    def priprava_za_igro(self):
        self.trenutni_kupcek = CELOTNI_KUPCEK.copy()
        self.zacetna()
        while len(self.igralci[3]) <= ZACETNO_STEVILO_KART:
            self.vleci()
            self.naslednji()
        self.trenutni_igralec = 0






