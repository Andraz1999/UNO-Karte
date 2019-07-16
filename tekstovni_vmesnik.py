import random
import Model


zgorna = (
    '|==============================================================================================================|\n'
    '|                                       ______                Trenutni:   {ena} |                        |\n'
    '|                                      |      |               Naslednji:  {dva} |   LEGENDA:             |\n'
    '|                       Nasprotnik2    |  {aa}  |   {aaa}                                 |   RDECA = rd           |\n' 
    '|                                      |      |                                       |   RUMENA = ru          |\n'
    '|                                      |______|                                       |   MODRA = mo           |\n'
    '|                                                                                     |   ZELENA = ze          |\n'
    '|     Nasprotnik1                       Kupček                         Nasprotnik3    |   CRNA = cr            |\n'
    '|      ______                           ______                          ______        |   ZAMENJAJ STRAN = ⟳   |\n'
    '|     |      |                         |      |                        |      |       |   STOP = st            |\n'
    '|     |  {bb}  |   {bbb}                   |  {cc}  |                  {ccc}   |  {ee}  |       |   SPREMENI BARVO = sp  |\n'
    '|     |      |                         |  {dd}  |                        |      |       |   VLECI DVE = +2       |\n'
    '|     |______|                         |______|                        |______|       |   VLECI STIRI = +4     |\n'
    '|                                                                                     |   VLECI PET = +5       |\n'
    '|                                                                                     |   IZPADEL = X          |\n'
    '|                                                                                     |                        |'
)

def titelscreen():
    izpis = (
        '|=====================================================================================|\n'
        '|                                                                                     |\n'
        '|                                                                                     |\n'
        '|           |       |                                                                 |\n'
        '|           |       |                                                                 |\n'
        '|           |       |                                                                 |\n'
        '|           |       |                                                                 |\n'
        '|           |_______|           |\    |                                               |\n'
        '|                               | \   |                                               |\n'
        '|                               |  \  |                                               |\n'
        '|                               |   \ |             _______                           |\n'
        '|                               |    \|            |       |                          |\n'
        '|                                                  |       |                          |\n'
        '|                                                  |       |                          |\n'
        '|                                                  |       |                          |\n'
        '|                                                  |_______|                          |\n'
        '|                                                                                     |\n'
        '|                                                                                     |\n'
        '|                                                                                     |\n'
        '|=====================================================================================|'
    )
    print(izpis)
    
    return
    
def tutorial1():
    izpis = (
        '|=====================================================================================|\n'
        '|                                     DOBRODOŠLI V UNO!                               |\n'
        '|                                                                                     |\n'
        '|      Pred vami je najbolj popularna igra poletja, pravila pa so zelo enostavna.     |\n'
        '|      Na začetku dobi vsak po sedem kart, kdo se jih pa prvi znebi, zmaga.           |\n'
        '|      Osnove igre predvidevam, da poznate, določene podrobnosti pa sem spremenil     |\n'
        '|      ali pa poenostavil. V tem uvodu bom na kratko razložil, kaj se dogaja na       |\n'
        '|      zaslonu, vse ostalo pa odkrite sami.                                           |\n'
        '|                                                                                     |\n'
        '|      Če želite nadaljevati z uvodom, pritisnite ENTER,                              |\n'
        '|      če pa želite kar začeti z igro, pa napišite START in nato pritisnite ENTER.    |\n'
        '|                                                                                     |\n'
        '|                                                                                     |\n'
        '|      (lahko tudi napišete start, Start, STArt, StArT...)                            |\n'
        '|                                                                                     |\n'
        '|                                                                                     |\n'
        '|                                                                                     |\n'
        '|                                                                                     |\n'
        '|                                                                                     |\n'
        '|=====================================================================================|'
    )
    print(izpis)
    
    return

def tutorial2():
    print('blablabla')
    

def tutorial3():
    print('tratralalala')

def enter():
    vnos = input('---> Za nadaljevanje pritisnite ENTER <---')
    vnos = vnos.upper()
    return vnos



def zacetek():
    titelscreen()
    poskus = enter()
    if poskus == 'START':
        tutorial3()
    else:
        tutorial1()
    poskus = enter()
    if poskus == 'START':
        tutorial3()
    else:
        tutorial2()
    poskus = enter()
    tutorial3()
    return

def prikaz_zgornih(zgorne):
    prikaz = (
        '|==============================================================================================================|'
    )
    prikaz2 = (
        '| zgorne: {}'.format(zgorne)
    )
    while len(prikaz2) < 111:
        prikaz2 += ' '
    prikaz2 += '|'
    print(prikaz)
    print(prikaz2)

def prikaz_igralca1(stevilo, barva):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec                                   __1___                                                            |\n'
        '|                  ___                      |      |                                                           |\n'
        '|     |   | |\  | |   |  |                  |  {aa}  |                                                           |\n'
        '|     |   | | \ | |   |  |                  |  {bb}  |                                                           |\n'
        '|     |___| |  \| |___|  O                  |______|                                                           |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo, bb = barva)) 
    
def prikaz_igralca2(stevilo0, barva0, stevilo1, barva1):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec                               __1___         __2___                                                 |\n'
        '|                                       |      |       |      |                                                |\n'
        '|                                       |  {aa}  |       |  {cc}  |                                                |\n'
        '|                                       |  {bb}  |       |  {dd}  |                                                |\n'
        '|                                       |______|       |______|                                                |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1)) 

def prikaz_igralca3(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec                         __1___         __2___         __3___                                        |\n'
        '|                                 |      |       |      |       |      |                                       |\n'
        '|                                 |  {aa}  |       |  {cc}  |       |  {ee}  |                                       |\n'
        '|                                 |  {bb}  |       |  {dd}  |       |  {ff}  |                                       |\n'
        '|                                 |______|       |______|       |______|                                       |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2)) 

def prikaz_igralca4(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2, stevilo3, barva3):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec                   __1___         __2___         __3___         __4___                               |\n'
        '|                           |      |       |      |       |      |       |      |                              |\n'
        '|                           |  {aa}  |       |  {cc}  |       |  {ee}  |       |  {gg}  |                              |\n'
        '|                           |  {bb}  |       |  {dd}  |       |  {ff}  |       |  {hh}  |                              |\n'
        '|                           |______|       |______|       |______|       |______|                              |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2, gg = stevilo3, hh = barva3)) 



def prikaz_igralca5(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2, stevilo3, barva3, stevilo4, barva4):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec            __1___         __2___         __3___         __4___         __5___                       |\n'
        '|                    |      |       |      |       |      |       |      |       |      |                      |\n'
        '|                    |  {aa}  |       |  {cc}  |       |  {ee}  |       |  {gg}  |       |  {ii}  |                      |\n'
        '|                    |  {bb}  |       |  {dd}  |       |  {ff}  |       |  {hh}  |       |  {jj}  |                      |\n'
        '|                    |______|       |______|       |______|       |______|       |______|                      |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2, gg = stevilo3, hh = barva3, ii = stevilo4, jj = barva4)) 




def prikaz_igralca6(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2, stevilo3, barva3, stevilo4, barva4, stevilo5, barva5):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec        __1___         __2___         __3___         __4___         __5___         __6___            |\n'
        '|                |      |       |      |       |      |       |      |       |      |       |      |           |\n'
        '|                |  {aa}  |       |  {cc}  |       |  {ee}  |       |  {gg}  |       |  {ii}  |       |  {kk}  |           |\n'
        '|                |  {bb}  |       |  {dd}  |       |  {ff}  |       |  {hh}  |       |  {jj}  |       |  {ll}  |           |\n'
        '|                |______|       |______|       |______|       |______|       |______|       |______|           |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2, gg = stevilo3, hh = barva3, ii = stevilo4, jj = barva4, kk = stevilo5, ll = barva5)) 



def prikaz_igralca7(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2, stevilo3, barva3, stevilo4, barva4, stevilo5, barva5, stevilo6, barva6):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec    __1___       __2___       __3___       __4___       __5___       __6___       __7___             |\n'
        '|            |      |     |      |     |      |     |      |     |      |     |      |     |      |            |\n'
        '|            |  {aa}  |     |  {cc}  |     |  {ee}  |     |  {gg}  |     |  {ii}  |     |  {kk}  |     |  {mm}  |            |\n'
        '|            |  {bb}  |     |  {dd}  |     |  {ff}  |     |  {hh}  |     |  {jj}  |     |  {ll}  |     |  {nn}  |            |\n'
        '|            |______|     |______|     |______|     |______|     |______|     |______|     |______|            |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2, gg = stevilo3, hh = barva3, ii = stevilo4, jj = barva4, kk = stevilo5, ll = barva5, mm = stevilo6, nn = barva6)) 



def prikaz_igralca8(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2, stevilo3, barva3, stevilo4, barva4, stevilo5, barva5, stevilo6, barva6, stevilo7, barva7):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec    __1___     __2___     __3___     __4___     __5___     __6___     __7___     __8___              |\n'
        '|            |      |   |      |   |      |   |      |   |      |   |      |   |      |   |      |             |\n'
        '|            |  {aa}  |   |  {cc}  |   |  {ee}  |   |  {gg}  |   |  {ii}  |   |  {kk}  |   |  {mm}  |   |  {oo}  |             |\n'
        '|            |  {bb}  |   |  {dd}  |   |  {ff}  |   |  {hh}  |   |  {jj}  |   |  {ll}  |   |  {nn}  |   |  {pp}  |             |\n'
        '|            |______|   |______|   |______|   |______|   |______|   |______|   |______|   |______|             |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2, gg = stevilo3, hh = barva3, ii = stevilo4, jj = barva4, kk = stevilo5, ll = barva5, mm = stevilo6, nn = barva6, oo = stevilo7, pp = barva7)) 



def prikaz_igralca9(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2, stevilo3, barva3, stevilo4, barva4, stevilo5, barva5, stevilo6, barva6, stevilo7, barva7, stevilo8, barva8):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec    __1___     __2___     __3___     __4___     __5___     __6___     __7___     __8___     __9___   |\n'
        '|            |      |   |      |   |      |   |      |   |      |   |      |   |      |   |      |   |      |  |\n'
        '|            |  {aa}  |   |  {cc}  |   |  {ee}  |   |  {gg}  |   |  {ii}  |   |  {kk}  |   |  {mm}  |   |  {oo}  |   |  {rr}  |  |\n'
        '|            |  {bb}  |   |  {dd}  |   |  {ff}  |   |  {hh}  |   |  {jj}  |   |  {ll}  |   |  {nn}  |   |  {pp}  |   |  {ss}  |  |\n'
        '|            |______|   |______|   |______|   |______|   |______|   |______|   |______|   |______|   |______|  |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2, gg = stevilo3, hh = barva3, ii = stevilo4, jj = barva4, kk = stevilo5, ll = barva5, mm = stevilo6, nn = barva6, oo = stevilo7, pp = barva7, rr = stevilo8, ss = barva8)) 


def prikaz_igralca10(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2, stevilo3, barva3, stevilo4, barva4, stevilo5, barva5, stevilo6, barva6, stevilo7, barva7, stevilo8, barva8, stevilo9, barva9):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec    __1___ __2___ __3___ __4___ __5___ __6___ __7___ __8___ __9___ __10__                            |\n'
        '|            |      |      |      |      |      |      |      |      |      |      |                           |\n'
        '|            |  {aa}  |  {cc}  |  {ee}  |  {gg}  |  {ii}  |  {kk}  |  {mm}  |  {oo}  |  {rr}  |  {tt}  |                           |\n'
        '|            |  {bb}  |  {dd}  |  {ff}  |  {hh}  |  {jj}  |  {ll}  |  {nn}  |  {pp}  |  {ss}  |  {uu}  |                           |\n'
        '|            |______|______|______|______|______|______|______|______|______|______|                           |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2, gg = stevilo3, hh = barva3, ii = stevilo4, jj = barva4, kk = stevilo5, ll = barva5, mm = stevilo6, nn = barva6, oo = stevilo7, pp = barva7, rr = stevilo8, ss = barva8, tt = stevilo9, uu = barva9)) 


def prikaz_igralca11(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2, stevilo3, barva3, stevilo4, barva4, stevilo5, barva5, stevilo6, barva6, stevilo7, barva7, stevilo8, barva8, stevilo9, barva9, stevilo10, barva10):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec    __1___ __2___ __3___ __4___ __5___ __6___ __7___ __8___ __9___ __10__ __11__                     |\n'
        '|            |      |      |      |      |      |      |      |      |      |      |      |                    |\n'
        '|            |  {aa}  |  {cc}  |  {ee}  |  {gg}  |  {ii}  |  {kk}  |  {mm}  |  {oo}  |  {rr}  |  {tt}  |  {vv}  |                    |\n'
        '|            |  {bb}  |  {dd}  |  {ff}  |  {hh}  |  {jj}  |  {ll}  |  {nn}  |  {pp}  |  {ss}  |  {uu}  |  {zz}  |                    |\n'
        '|            |______|______|______|______|______|______|______|______|______|______|______|                    |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2, gg = stevilo3, hh = barva3, ii = stevilo4, jj = barva4, kk = stevilo5, ll = barva5, mm = stevilo6, nn = barva6, oo = stevilo7, pp = barva7, rr = stevilo8, ss = barva8, tt = stevilo9, uu = barva9, vv = stevilo10, zz = barva10)) 


def prikaz_igralca12(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2, stevilo3, barva3, stevilo4, barva4, stevilo5, barva5, stevilo6, barva6, stevilo7, barva7, stevilo8, barva8, stevilo9, barva9, stevilo10, barva10, stevilo11, barva11):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec    __1___ __2___ __3___ __4___ __5___ __6___ __7___ __8___ __9___ __10__ __11__ __12__              |\n'
        '|            |      |      |      |      |      |      |      |      |      |      |      |      |             |\n'
        '|            |  {aa}  |  {cc}  |  {ee}  |  {gg}  |  {ii}  |  {kk}  |  {mm}  |  {oo}  |  {rr}  |  {tt}  |  {vv}  |  {ab}  |             |\n'
        '|            |  {bb}  |  {dd}  |  {ff}  |  {hh}  |  {jj}  |  {ll}  |  {nn}  |  {pp}  |  {ss}  |  {uu}  |  {zz}  |  {ba}  |             |\n'
        '|            |______|______|______|______|______|______|______|______|______|______|______|______|             |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2, gg = stevilo3, hh = barva3, ii = stevilo4, jj = barva4, kk = stevilo5, ll = barva5, mm = stevilo6, nn = barva6, oo = stevilo7, pp = barva7, rr = stevilo8, ss = barva8, tt = stevilo9, uu = barva9, vv = stevilo10, zz = barva10, ab = stevilo11, ba = barva11)) 


def prikaz_igralca13(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2, stevilo3, barva3, stevilo4, barva4, stevilo5, barva5, stevilo6, barva6, stevilo7, barva7, stevilo8, barva8, stevilo9, barva9, stevilo10, barva10, stevilo11, barva11, stevilo12, barva12):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec    __1___ __2___ __3___ __4___ __5___ __6___ __7___ __8___ __9___ __10__ __11__ __12__ __13__       |\n'
        '|            |      |      |      |      |      |      |      |      |      |      |      |      |      |      |\n'
        '|            |  {aa}  |  {cc}  |  {ee}  |  {gg}  |  {ii}  |  {kk}  |  {mm}  |  {oo}  |  {rr}  |  {tt}  |  {vv}  |  {ab}  |  {bc}  |      |\n'
        '|            |  {bb}  |  {dd}  |  {ff}  |  {hh}  |  {jj}  |  {ll}  |  {nn}  |  {pp}  |  {ss}  |  {uu}  |  {zz}  |  {ba}  |  {cb}  |      |\n'
        '|            |______|______|______|______|______|______|______|______|______|______|______|______|______|      |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2, gg = stevilo3, hh = barva3, ii = stevilo4, jj = barva4, kk = stevilo5, ll = barva5, mm = stevilo6, nn = barva6, oo = stevilo7, pp = barva7, rr = stevilo8, ss = barva8, tt = stevilo9, uu = barva9, vv = stevilo10, zz = barva10, ab = stevilo11, ba = barva11, bc = stevilo12, cb = barva12)) 


def prikaz_igralca14(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2, stevilo3, barva3, stevilo4, barva4, stevilo5, barva5, stevilo6, barva6, stevilo7, barva7, stevilo8, barva8, stevilo9, barva9, stevilo10, barva10, stevilo11, barva11, stevilo12, barva12, stevilo13, barva13):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec    1_ 2_ 3_ 4_ 5_ 6_ 7_ 8_ 9_ 10 11 12 13 14                                                        |\n'
        '|            |  |  |  |  |  |  |  |  |  |  |  |  |  |  |                                                       |\n'
        '|            |{aa}|{cc}|{ee}|{gg}|{ii}|{kk}|{mm}|{oo}|{rr}|{tt}|{vv}|{ab}|{bc}|{cd}|                                                       |\n'
        '|            |{bb}|{dd}|{ff}|{hh}|{jj}|{ll}|{nn}|{pp}|{ss}|{uu}|{zz}|{ba}|{cb}|{dc}|                                                       |\n'
        '|            |__|__|__|__|__|__|__|__|__|__|__|__|__|__|                                                       |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2, gg = stevilo3, hh = barva3, ii = stevilo4, jj = barva4, kk = stevilo5, ll = barva5, mm = stevilo6, nn = barva6, oo = stevilo7, pp = barva7, rr = stevilo8, ss = barva8, tt = stevilo9, uu = barva9, vv = stevilo10, zz = barva10, ab = stevilo11, ba = barva11, bc = stevilo12, cb = barva12, cd = stevilo13, dc = barva13)) 

# prikaz_igralca14('01', 'aa', '02', 'bb', '03', 'cc', '04', 'dd', '05', 'ee', '06', 'ff', '07', 'gg', '08', 'hh', '09', 'ii', '10', 'jj', '11', 'kk', '12', 'll', '13', 'mm', '14', 'nn')

def prikaz_igralca15(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2, stevilo3, barva3, stevilo4, barva4, stevilo5, barva5, stevilo6, barva6, stevilo7, barva7, stevilo8, barva8, stevilo9, barva9, stevilo10, barva10, stevilo11, barva11, stevilo12, barva12, stevilo13, barva13, stevilo14, barva14):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec    1_ 2_ 3_ 4_ 5_ 6_ 7_ 8_ 9_ 10 11 12 13 14 15                                                     |\n'
        '|            |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |                                                    |\n'
        '|            |{aa}|{cc}|{ee}|{gg}|{ii}|{kk}|{mm}|{oo}|{rr}|{tt}|{vv}|{ab}|{bc}|{cd}|{de}|                                                    |\n'
        '|            |{bb}|{dd}|{ff}|{hh}|{jj}|{ll}|{nn}|{pp}|{ss}|{uu}|{zz}|{ba}|{cb}|{dc}|{ed}|                                                    |\n'
        '|            |__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|                                                    |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2, gg = stevilo3, hh = barva3, ii = stevilo4, jj = barva4, kk = stevilo5, ll = barva5, mm = stevilo6, nn = barva6, oo = stevilo7, pp = barva7, rr = stevilo8, ss = barva8, tt = stevilo9, uu = barva9, vv = stevilo10, zz = barva10, ab = stevilo11, ba = barva11, bc = stevilo12, cb = barva12, cd = stevilo13, dc = barva13, de = stevilo14, ed = barva14)) 


def prikaz_igralca16(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2, stevilo3, barva3, stevilo4, barva4, stevilo5, barva5, stevilo6, barva6, stevilo7, barva7, stevilo8, barva8, stevilo9, barva9, stevilo10, barva10, stevilo11, barva11, stevilo12, barva12, stevilo13, barva13, stevilo14, barva14, stevilo15, barva15):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec    1_ 2_ 3_ 4_ 5_ 6_ 7_ 8_ 9_ 10 11 12 13 14 15 16                                                  |\n'
        '|            |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |                                                 |\n'
        '|            |{aa}|{cc}|{ee}|{gg}|{ii}|{kk}|{mm}|{oo}|{rr}|{tt}|{vv}|{ab}|{bc}|{cd}|{de}|{ef}|                                                 |\n'
        '|            |{bb}|{dd}|{ff}|{hh}|{jj}|{ll}|{nn}|{pp}|{ss}|{uu}|{zz}|{ba}|{cb}|{dc}|{ed}|{fe}|                                                 |\n'
        '|            |__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|                                                 |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2, gg = stevilo3, hh = barva3, ii = stevilo4, jj = barva4, kk = stevilo5, ll = barva5, mm = stevilo6, nn = barva6, oo = stevilo7, pp = barva7, rr = stevilo8, ss = barva8, tt = stevilo9, uu = barva9, vv = stevilo10, zz = barva10, ab = stevilo11, ba = barva11, bc = stevilo12, cb = barva12, cd = stevilo13, dc = barva13, de = stevilo14, ed = barva14, ef = stevilo15, fe = barva15)) 



def prikaz_igralca17(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2, stevilo3, barva3, stevilo4, barva4, stevilo5, barva5, stevilo6, barva6, stevilo7, barva7, stevilo8, barva8, stevilo9, barva9, stevilo10, barva10, stevilo11, barva11, stevilo12, barva12, stevilo13, barva13, stevilo14, barva14, stevilo15, barva15, stevilo16, barva16):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec    1_ 2_ 3_ 4_ 5_ 6_ 7_ 8_ 9_ 10 11 12 13 14 15 16 17                                               |\n'
        '|            |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |                                              |\n'
        '|            |{aa}|{cc}|{ee}|{gg}|{ii}|{kk}|{mm}|{oo}|{rr}|{tt}|{vv}|{ab}|{bc}|{cd}|{de}|{ef}|{fg}|                                              |\n'
        '|            |{bb}|{dd}|{ff}|{hh}|{jj}|{ll}|{nn}|{pp}|{ss}|{uu}|{zz}|{ba}|{cb}|{dc}|{ed}|{fe}|{gf}|                                              |\n'
        '|            |__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|                                              |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2, gg = stevilo3, hh = barva3, ii = stevilo4, jj = barva4, kk = stevilo5, ll = barva5, mm = stevilo6, nn = barva6, oo = stevilo7, pp = barva7, rr = stevilo8, ss = barva8, tt = stevilo9, uu = barva9, vv = stevilo10, zz = barva10, ab = stevilo11, ba = barva11, bc = stevilo12, cb = barva12, cd = stevilo13, dc = barva13, de = stevilo14, ed = barva14, ef = stevilo15, fe = barva15, fg = stevilo16, gf = barva16)) 


def prikaz_igralca18(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2, stevilo3, barva3, stevilo4, barva4, stevilo5, barva5, stevilo6, barva6, stevilo7, barva7, stevilo8, barva8, stevilo9, barva9, stevilo10, barva10, stevilo11, barva11, stevilo12, barva12, stevilo13, barva13, stevilo14, barva14, stevilo15, barva15, stevilo16, barva16, stevilo17, barva17):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec    1_ 2_ 3_ 4_ 5_ 6_ 7_ 8_ 9_ 10 11 12 13 14 15 16 17 18                                            |\n'
        '|            |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |                                           |\n'
        '|            |{aa}|{cc}|{ee}|{gg}|{ii}|{kk}|{mm}|{oo}|{rr}|{tt}|{vv}|{ab}|{bc}|{cd}|{de}|{ef}|{fg}|{gh}|                                           |\n'
        '|            |{bb}|{dd}|{ff}|{hh}|{jj}|{ll}|{nn}|{pp}|{ss}|{uu}|{zz}|{ba}|{cb}|{dc}|{ed}|{fe}|{gf}|{hg}|                                           |\n'
        '|            |__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|                                           |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2, gg = stevilo3, hh = barva3, ii = stevilo4, jj = barva4, kk = stevilo5, ll = barva5, mm = stevilo6, nn = barva6, oo = stevilo7, pp = barva7, rr = stevilo8, ss = barva8, tt = stevilo9, uu = barva9, vv = stevilo10, zz = barva10, ab = stevilo11, ba = barva11, bc = stevilo12, cb = barva12, cd = stevilo13, dc = barva13, de = stevilo14, ed = barva14, ef = stevilo15, fe = barva15, fg = stevilo16, gf = barva16, gh = stevilo17, hg = barva17)) 


def prikaz_igralca19(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2, stevilo3, barva3, stevilo4, barva4, stevilo5, barva5, stevilo6, barva6, stevilo7, barva7, stevilo8, barva8, stevilo9, barva9, stevilo10, barva10, stevilo11, barva11, stevilo12, barva12, stevilo13, barva13, stevilo14, barva14, stevilo15, barva15, stevilo16, barva16, stevilo17, barva17, stevilo18, barva18):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec    1_ 2_ 3_ 4_ 5_ 6_ 7_ 8_ 9_ 10 11 12 13 14 15 16 17 18 19                                         |\n'
        '|            |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |                                        |\n'
        '|            |{aa}|{cc}|{ee}|{gg}|{ii}|{kk}|{mm}|{oo}|{rr}|{tt}|{vv}|{ab}|{bc}|{cd}|{de}|{ef}|{fg}|{gh}|{hi}|                                        |\n'
        '|            |{bb}|{dd}|{ff}|{hh}|{jj}|{ll}|{nn}|{pp}|{ss}|{uu}|{zz}|{ba}|{cb}|{dc}|{ed}|{fe}|{gf}|{hg}|{ih}|                                        |\n'
        '|            |__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|                                        |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2, gg = stevilo3, hh = barva3, ii = stevilo4, jj = barva4, kk = stevilo5, ll = barva5, mm = stevilo6, nn = barva6, oo = stevilo7, pp = barva7, rr = stevilo8, ss = barva8, tt = stevilo9, uu = barva9, vv = stevilo10, zz = barva10, ab = stevilo11, ba = barva11, bc = stevilo12, cb = barva12, cd = stevilo13, dc = barva13, de = stevilo14, ed = barva14, ef = stevilo15, fe = barva15, fg = stevilo16, gf = barva16, gh = stevilo17, hg = barva17, hi = stevilo18, ih = barva18)) 

# prikaz_igralca19('01', 'aa', '02', 'bb', '03', 'cc', '04', 'dd', '05', 'ee', '06', 'ff', '07', 'gg', '08', 'hh', '09', 'ii', '10', 'jj', '11', 'kk', '12', 'll', '13', 'mm', '14', 'nn', '15', 'oo', '16', 'pp', '17', 'rr', '18', 'ss', '19', 'tt')

def prikaz_igralca20(stevilo0, barva0, stevilo1, barva1, stevilo2, barva2, stevilo3, barva3, stevilo4, barva4, stevilo5, barva5, stevilo6, barva6, stevilo7, barva7, stevilo8, barva8, stevilo9, barva9, stevilo10, barva10, stevilo11, barva11, stevilo12, barva12, stevilo13, barva13, stevilo14, barva14, stevilo15, barva15, stevilo16, barva16, stevilo17, barva17, stevilo18, barva18, stevilo19, barva19):
    prikaz1 = (
        '|==============================================================================================================|\n'
        '|  Igralec    1_ 2_ 3_ 4_ 5_ 6_ 7_ 8_ 9_ 10 11 12 13 14 15 16 17 18 19 20                                      |\n'
        '|            |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |                                     |\n'
        '|            |{aa}|{cc}|{ee}|{gg}|{ii}|{kk}|{mm}|{oo}|{rr}|{tt}|{vv}|{ab}|{bc}|{cd}|{de}|{ef}|{fg}|{gh}|{hi}|{ij}|                                     |\n'
        '|            |{bb}|{dd}|{ff}|{hh}|{jj}|{ll}|{nn}|{pp}|{ss}|{uu}|{zz}|{ba}|{cb}|{dc}|{ed}|{fe}|{gf}|{hg}|{ih}|{ji}|                                     |\n'
        '|            |__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|                                     |\n'
        '|                                                                                                              |\n'
        '|==============================================================================================================|\n'
     )
    print(prikaz1.format(aa = stevilo0, bb = barva0, cc = stevilo1, dd = barva1, ee = stevilo2, ff = barva2, gg = stevilo3, hh = barva3, ii = stevilo4, jj = barva4, kk = stevilo5, ll = barva5, mm = stevilo6, nn = barva6, oo = stevilo7, pp = barva7, rr = stevilo8, ss = barva8, tt = stevilo9, uu = barva9, vv = stevilo10, zz = barva10, ab = stevilo11, ba = barva11, bc = stevilo12, cb = barva12, cd = stevilo13, dc = barva13, de = stevilo14, ed = barva14, ef = stevilo15, fe = barva15, fg = stevilo16, gf = barva16, gh = stevilo17, hg = barva17, hi = stevilo18, ih = barva18, ij = stevilo19, ji = barva19)) 

def prikaz_igralca0():
    prikaz = (
        '|==============================================================================================================|\n'
        '|  Igralec           ____                       ______                         _____                           |\n'
        '|                       /  |\    /|     /\     |      |    /\     |           |        |       |               |\n'
        '|                      /   | \  / |    /  \    |          /  \    |           |_____   |       |               |\n'
        '|                     /    |  \/  |   /----\   |   ____  /----\   |                 |  |       |               |\n'
        '|                    /     |      |  /      \  |      | /      \  |                 |  |       |               |\n'
        '|                   /____  |      | /        \ |______|/        \ |_____      ______|  |       O               |\n'
        '|==============================================================================================================|\n'
    )
    return print(prikaz)

def izberi_barvo():
    while True:
        vnos = input('Izberi barvo: ("{}", "{}", "{}", "{}"): '.format(Model.RDECA, Model.RUMENA, Model.MODRA, Model.ZELENA))
        if vnos in [Model.RDECA, Model.RUMENA, Model.MODRA, Model.ZELENA]:
            return vnos
        print('Neveljavna izbira!')

def da_ali_ne(stavek):
    while True:
        vnos = input(stavek)
        vnos = vnos.upper()
        if vnos == 'DA':
            return True
        elif vnos == 'NE':
            return False
        print('Neveljavna izbira!')

def main():
    igra = Model.Igra()
    igra.priprava_za_igro()
    def osnova():
        prikaz_zgornih(igra.zgorne_karte)
        
        ########################################
        un1 = '   '
        un2 = '   '
        un3 = '   '
        if len(igra.igralci[1]) == 1:
            un1 = 'UNO'
        if len(igra.igralci[2]) == 1:
            un2 = 'UNO'
        if len(igra.igralci[3]) == 1:
            un3 = 'UNO'
        n1 = str(len(igra.igralci[1]))
        if len(n1) == 1:
            n1 = ' ' + n1
        n2 = str(len(igra.igralci[2]))
        if len(n2) == 1:
            n2 = ' ' + n2
        n3 = str(len(igra.igralci[3]))
        if len(n3) == 1:
            n3 = ' ' + n3
        if igra.igralci[1] == Model.IZPADEL:
            n1 = ' X'
        if igra.igralci[2] == Model.IZPADEL:
            n2 = ' X'
        if igra.igralci[3] == Model.IZPADEL:
            n3 = ' X'
        p1 = igra.trenutni_igralec
        if p1 == 0:
            p1 = 'Igralec    '
        else:
            p1 = 'Nasprotnik{}'.format(p1)
        p2 = igra.naslednji_bi()
        if p2 == 0:
            p2 = 'Igralec    '
        else:
            p2 = 'Nasprotnik{}'.format(p2)
        print(zgorna.format(aa = n2, bb = n1, ee = n3, aaa = un2, bbb = un1, ccc = un3, cc = igra.zgorne_karte[-1][0], dd = igra.zgorne_karte[-1][1], ena = p1, dva = p2))
#################################################
        ig = igra.igralci[0]
        if len(ig) == 0:
            return prikaz_igralca0()
        if len(ig) == 1:
            prikaz_igralca1(ig[0][0], ig[0][1])
        elif len(ig) == 2:
            prikaz_igralca2(ig[0][0], ig[0][1], ig[1][0], ig[1][1])
        elif len(ig) == 3:
            prikaz_igralca3(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1])
        elif len(ig) == 4:
            prikaz_igralca4(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1], ig[3][0], ig[3][1])
        elif len(ig) == 5:
            prikaz_igralca5(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1], ig[3][0], ig[3][1], ig[4][0], ig[4][1])
        elif len(ig) == 6:
            prikaz_igralca6(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1], ig[3][0], ig[3][1], ig[4][0], ig[4][1], ig[5][0], ig[5][1])
        elif len(ig) == 7:
            prikaz_igralca7(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1], ig[3][0], ig[3][1], ig[4][0], ig[4][1], ig[5][0], ig[5][1], ig[6][0], ig[6][1])
        elif len(ig) == 8:
            prikaz_igralca8(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1], ig[3][0], ig[3][1], ig[4][0], ig[4][1], ig[5][0], ig[5][1], ig[6][0], ig[6][1], ig[7][0], ig[7][1])
        elif len(ig) == 9:
            prikaz_igralca9(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1], ig[3][0], ig[3][1], ig[4][0], ig[4][1], ig[5][0], ig[5][1], ig[6][0], ig[6][1], ig[7][0], ig[7][1], ig[8][0], ig[8][1])
        elif len(ig) == 10:
            prikaz_igralca10(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1], ig[3][0], ig[3][1], ig[4][0], ig[4][1], ig[5][0], ig[5][1], ig[6][0], ig[6][1], ig[7][0], ig[7][1], ig[8][0], ig[8][1], ig[9][0], ig[9][1])
        elif len(ig) == 11:
            prikaz_igralca11(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1], ig[3][0], ig[3][1], ig[4][0], ig[4][1], ig[5][0], ig[5][1], ig[6][0], ig[6][1], ig[7][0], ig[7][1], ig[8][0], ig[8][1], ig[9][0], ig[9][1], ig[10][0], ig[10][1])
        elif len(ig) == 12:
            prikaz_igralca12(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1], ig[3][0], ig[3][1], ig[4][0], ig[4][1], ig[5][0], ig[5][1], ig[6][0], ig[6][1], ig[7][0], ig[7][1], ig[8][0], ig[8][1], ig[9][0], ig[9][1], ig[10][0], ig[10][1], ig[11][0], ig[11][1])
        elif len(ig) == 13:
            prikaz_igralca13(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1], ig[3][0], ig[3][1], ig[4][0], ig[4][1], ig[5][0], ig[5][1], ig[6][0], ig[6][1], ig[7][0], ig[7][1], ig[8][0], ig[8][1], ig[9][0], ig[9][1], ig[10][0], ig[10][1], ig[11][0], ig[11][1], ig[12][0], ig[12][1])
        elif len(ig) == 14:
            prikaz_igralca14(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1], ig[3][0], ig[3][1], ig[4][0], ig[4][1], ig[5][0], ig[5][1], ig[6][0], ig[6][1], ig[7][0], ig[7][1], ig[8][0], ig[8][1], ig[9][0], ig[9][1], ig[10][0], ig[10][1], ig[11][0], ig[11][1], ig[12][0], ig[12][1], ig[13][0], ig[13][1])
        elif len(ig) == 15:
            prikaz_igralca15(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1], ig[3][0], ig[3][1], ig[4][0], ig[4][1], ig[5][0], ig[5][1], ig[6][0], ig[6][1], ig[7][0], ig[7][1], ig[8][0], ig[8][1], ig[9][0], ig[9][1], ig[10][0], ig[10][1], ig[11][0], ig[11][1], ig[12][0], ig[12][1], ig[13][0], ig[13][1], ig[14][0], ig[14][1])
        elif len(ig) == 16:
            prikaz_igralca16(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1], ig[3][0], ig[3][1], ig[4][0], ig[4][1], ig[5][0], ig[5][1], ig[6][0], ig[6][1], ig[7][0], ig[7][1], ig[8][0], ig[8][1], ig[9][0], ig[9][1], ig[10][0], ig[10][1], ig[11][0], ig[11][1], ig[12][0], ig[12][1], ig[13][0], ig[13][1], ig[14][0], ig[14][1], ig[15][0], ig[15][1])
        elif len(ig) == 17:
            prikaz_igralca17(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1], ig[3][0], ig[3][1], ig[4][0], ig[4][1], ig[5][0], ig[5][1], ig[6][0], ig[6][1], ig[7][0], ig[7][1], ig[8][0], ig[8][1], ig[9][0], ig[9][1], ig[10][0], ig[10][1], ig[11][0], ig[11][1], ig[12][0], ig[12][1], ig[13][0], ig[13][1], ig[14][0], ig[14][1], ig[15][0], ig[15][1], ig[16][0], ig[16][1])
        elif len(ig) == 18:
            prikaz_igralca18(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1], ig[3][0], ig[3][1], ig[4][0], ig[4][1], ig[5][0], ig[5][1], ig[6][0], ig[6][1], ig[7][0], ig[7][1], ig[8][0], ig[8][1], ig[9][0], ig[9][1], ig[10][0], ig[10][1], ig[11][0], ig[11][1], ig[12][0], ig[12][1], ig[13][0], ig[13][1], ig[14][0], ig[14][1], ig[15][0], ig[15][1], ig[16][0], ig[16][1], ig[17][0], ig[17][1])
        elif len(ig) == 19:
            prikaz_igralca19(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1], ig[3][0], ig[3][1], ig[4][0], ig[4][1], ig[5][0], ig[5][1], ig[6][0], ig[6][1], ig[7][0], ig[7][1], ig[8][0], ig[8][1], ig[9][0], ig[9][1], ig[10][0], ig[10][1], ig[11][0], ig[11][1], ig[12][0], ig[12][1], ig[13][0], ig[13][1], ig[14][0], ig[14][1], ig[15][0], ig[15][1], ig[16][0], ig[16][1], ig[17][0], ig[17][1], ig[18][0], ig[18][1])
        elif len(ig) == 20:
            prikaz_igralca20(ig[0][0], ig[0][1], ig[1][0], ig[1][1], ig[2][0], ig[2][1], ig[3][0], ig[3][1], ig[4][0], ig[4][1], ig[5][0], ig[5][1], ig[6][0], ig[6][1], ig[7][0], ig[7][1], ig[8][0], ig[8][1], ig[9][0], ig[9][1], ig[10][0], ig[10][1], ig[11][0], ig[11][1], ig[12][0], ig[12][1], ig[13][0], ig[13][1], ig[14][0], ig[14][1], ig[15][0], ig[15][1], ig[16][0], ig[16][1], ig[17][0], ig[17][1], ig[18][0], ig[18][1], ig[19][0], ig[19][1])
        else: 
            print('igralec ima prevec kart')
    ###################################################
    def poteza():
        while True:
            vnos = input('Izberi zaporedno številko karte. "0" pomeni, "vleci karto": ')
            if vnos.isdigit():
                vnos = int(vnos)
                if vnos in range(len(igra.igralci[0]) + 1):
                    if vnos == 0:
                        return Model.VLECI
                    elif igra.igralci[0][vnos - 1] in igra.mozne_izbire():
                        return igra.igralci[0][vnos - 1]
            print('Neveljavna poteza!')
    ################################################################3
    def vleci_kazen(n, karta, zgorna_karta):
        vnos = (karta, Model.CRNA)
        kazen = []
        for _ in range(n):
            karta = random.choice(igra.trenutni_kupcek)
            igra.trenutni_kupcek.remove(karta)
            kazen.append(karta)
            if len(igra.trenutni_kupcek) < 1:
                igra.zmesaj()
        igra.naslednji()
        kljuc = True
        while vnos in igra.igralci[igra.trenutni_igralec] and kljuc:
            if igra.trenutni_igralec == 0:
                if da_ali_ne(f'Ali želiš karto {vnos} zdaj poklicati? ("DA" ali "NE"): '):
                    igra.poklic(vnos)
                    for _ in range(n):
                        karta = random.choice(igra.trenutni_kupcek)
                        igra.trenutni_kupcek.remove(karta)
                        kazen.append(karta)
                        if len(igra.trenutni_kupcek) < 1:
                            igra.zmesaj()
                    igra.naslednji()
                else:
                    igra.igralci[0] += kazen
                    x = len(kazen)
                    if x == 2:
                        print('Vlekel si 2 karti!')
                    elif x == 3 or x == 4:
                        print(f'Vlekel si {x} karte!')
                    else:
                        print(f'Vlekel si {x} kart!')
                    kljuc = False
            else:
                verjetnost = random.random()
                if verjetnost <= 0.8:
                    igra.poklic(vnos)
                    for _ in range(n):
                        karta = random.choice(igra.trenutni_kupcek)
                        igra.trenutni_kupcek.remove(karta)
                        kazen.append(karta)
                        if len(igra.trenutni_kupcek) < 1:
                            igra.zmesaj()
                    igra.naslednji()
                else: 
                    igra.igralci[igra.trenutni_igralec] += kazen
                    x = len(kazen)
                    y = igra.trenutni_igralec
                    if x == 2:
                        print(f'Nasprotnik{y} je vlekel 2 karti!')
                    elif x == 3:
                        print(f'Nasprotnik{y} je vlekel 3 karte!')
                    else:
                        print(f'Nasprotnik{y} je vlekel {x} kart!')
                    kljuc = False
        if kljuc:
            if igra.trenutni_igralec == 0:
                igra.igralci[0] += kazen
                x = len(kazen)
                if x == 2:
                    print('Vlekel si 2 karti!')
                elif x == 3:
                    print('Vlekel si 3 karte!')
                else:
                    print(f'Vlekel si {x} kart!')
            else:  
                igra.igralci[igra.trenutni_igralec] += kazen
                x = len(kazen)
                y = igra.trenutni_igralec
                if x == 2:
                    print(f'Nasprotnik{y} je vlekel 2 karti!')
                elif x == 3:
                    print(f'Nasprotnik{y} je vlekel 3 karte!')
                else:
                    print(f'Nasprotnik{y} je vlekel {x} kart!') 
        igra.zgorne_karte.append((zgorna_karta, zgorna_karta))
        if len(igra.zgorne_karte) > 5:
            igra.zgorne_karte.pop(0)
    ##############################################33
    def krog_igralec(vnos, pogoj):
        zgorna_karta = igra.zgorne_karte[-1]
        igra.poklic(vnos)
        osnova()
        if vnos == Model.VLECI:
            print('Vlekel si novo karto.')
        else:
            print(f'Poklical si karto: {vnos}.')
        if vnos[0] == Model.ZAMENJAJ_STRAN:
            igra.zamenjaj_smer()
            print('Spremenila se je smer.')
        elif vnos[0] == Model.STOP:
            p1 = igra.naslednji_bi()
            if p1 == 0:
                print('Preskočili so te.')
            else:
                p1 = 'Nasprotnika{}'.format(p1)
                print(f'{p1} ste preskočili.')
            igra.naslednji()
        elif vnos[0] == Model.SPREMENI_BARVO:
            vnos2 = izberi_barvo()
            igra.sprememba_barve(vnos2)
            print(f'Barva se je spremenila na: {vnos2}.')
        elif vnos[0] == Model.VLECI_PET:
            igra.vleci_pet(zgorna_karta[1])
            print('Vsak je vlekel 5 kart!!!')
        elif vnos == Model.VLECI:
            nova = igra.igralci[0][-1]
            if nova in igra.mozne_izbire():
                if da_ali_ne('Ali želiš to karto zdaj poklicati? ("DA" ali "NE"): '):
                    krog_igralec(nova, False)
        elif vnos[0] == Model.VLECI_DVE:
            vleci_kazen(2, Model.VLECI_DVE, zgorna_karta[1])        
        elif vnos[0] == Model.VLECI_STIRI:
            vleci_kazen(4, Model.VLECI_STIRI, zgorna_karta[1])  
        elif vnos in Model.BARVNE and pogoj:
            if vnos in igra.igralci[0]:
                if da_ali_ne(f'Ali želiš še eno {vnos} poklicat? ("DA" ali "NE"): '):
                    igra.poklic(vnos)
                    print(f'Poklical si dve {vnos}.')              
                    ######################################################################
    def krog_nasprotnik(vnos, pogoj):
        zgorna_karta = igra.zgorne_karte[-1]
        z = igra.trenutni_igralec
        igra.poklic(vnos)
        osnova()
        if vnos == Model.VLECI:
            print(f'Nasprotnik{z} je vlekel novo karto.')
        else:
            print(f'Nasprotnik{z} je poklical karto: {vnos}.')
        enter()
        if vnos[0] == Model.ZAMENJAJ_STRAN:
            igra.zamenjaj_smer()
            print('Spremenila se je smer.')
        elif vnos[0] == Model.STOP:
            p1 = igra.naslednji_bi()
            if p1 == 0:
                print('Preskočili so te.')
            else:
                p1 = 'Nasprotnika{}'.format(p1)
                print(f'{p1} ste preskočili.')
            igra.naslednji()
        elif vnos[0] == Model.SPREMENI_BARVO:
            vnos2 = igra.nasprotnik_barva()
            igra.sprememba_barve(vnos2)
            print(f'Barva se je spremenila na: {vnos2}.')
        elif vnos[0] == Model.VLECI_PET:
            igra.vleci_pet(zgorna_karta[1])
            print('Vsak je vlekel 5 kart!!!')
        elif vnos == Model.VLECI:
            nova = igra.igralci[igra.trenutni_igralec][-1]
            if nova in igra.mozne_izbire():
                if random.random() < 0.8:
                    krog_nasprotnik(nova, False)
        elif vnos[0] == Model.VLECI_DVE:
            vleci_kazen(2, Model.VLECI_DVE, zgorna_karta[1])
        elif vnos[0] == Model.VLECI_STIRI:
            vleci_kazen(4, Model.VLECI_STIRI, zgorna_karta[1])  
        elif vnos in Model.BARVNE and pogoj:
            if vnos in igra.igralci[igra.trenutni_igralec]:
                    igra.poklic(vnos)
                    print(f'Nasprotnik{z} je poklical dve {vnos}.') 
            
    
    while True:
        osnova()
        #zgorna_karta = igra.zgorne_karte[-1]
        if igra.trenutni_igralec == 0:
            vnos = poteza()
            krog_igralec(vnos, True)
        
        else:
            vnos = igra.nasprotnik()
            krog_nasprotnik(vnos, True)
        enter()
        igra.izpadel()
        if igra.konec_igre():
            if igra.igralci[0] == []:
                print('ZMAGAL SI!!!')
                return
            else: 
                print('IZGUBIL SI.')
                return
        igra.naslednji() 



main()


