import random
import Model


zgorna = (
    '|=====================================================================================|\n'
    '|                                       ______                                        |\n'
    '|                                      |      |                                       |\n'
    '|                                      |      |                                       |\n'
    '|                                      |      |                                       |\n'
    '|                                      |______|                                       |\n'
    '|                                                                                     |\n'
    '|                                                                                     |\n'
    '|      ______                           ______                          ______        |\n'
    '|     |      |                         |      |                        |      |       |\n'
    '|     |      |                         |      |                        |      |       |\n'
    '|     |      |                         |      |                        |      |       |\n'
    '|     |______|                         |______|                        |______|       |\n'
    '|                                                                                     |\n'
    '|                                                                                     |\n'
    '|                                                                                     |'
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
    print('---> Za nadaljevanje pritisnite ENTER <---')
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
    print('---> Za nadaljevanje pritisnite ENTER <---')
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

zacetek()











