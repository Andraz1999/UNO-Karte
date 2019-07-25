import bottle
import Model
import random


uno = Model.Uno()

@bottle.get('/')
def prva_stran():
    return bottle.template('index.tpl')

@bottle.get('/static/<ime_slike>')
def prikazi_sliko(ime_slike):
    return bottle.static_file(ime_slike, root = './img')


@bottle.post('/nova_igra/')
def zacni_novo_igro():
    # naredi novo igro in preusmeri na nov naslov
    id_igre = uno.nova_igra()
    bottle.redirect('/igra/ ' + str(id_igre))
    return 


@bottle.get('/pravila_igre/')
def prikaz_pravil():
    return bottle.template('pravila_igre.tpl')

@bottle.get('/igra/<id_igre>')
def prikazi_igro(id_igre):
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    if stanje == Model.ZMAGA:
        return bottle.template('zmaga.tpl')
    elif stanje == Model.PORAZ:
        return bottle.template('poraz.tpl')
    if igra.trenutni_igralec == 0:
        return bottle.template('igra.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
    else:
        karta = igra.nasprotnik()
        uno.poklic_karte0(int(id_igre), karta)
        if karta == Model.VLECI:
            return bottle.template('igranasprotnikvleci.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
        else:
            return bottle.template('igranasprotnik.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)

@bottle.post('/obdelava/<id_igre>')
def poteza(id_igre):
    id_igre = int(id_igre)
    #print(str(id_igre))
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    vnos = int(bottle.request.forms['poteza'])
    if vnos == 0:
        karta = Model.VLECI
        uno.poklic_karte0(id_igre, karta)
        bottle.redirect('/igra/ ' + str(id_igre) + '/' + str(vnos) + '/' +  '1' )
    else:
        karta = igra.igralci[igra.trenutni_igralec][vnos - 1]
        if karta in igra.mozne_izbire():
            uno.poklic_karte0(id_igre, karta)
            bottle.redirect('/igra/ ' + str(id_igre) + '/' + str(vnos) + '/' +'1')
        else:
            bottle.redirect('/napaka/ ' + str(id_igre))

@bottle.get('/napaka/<id_igre>')
def poslji_nazaj(id_igre):
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    return bottle.template('igra_napaka.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)



@bottle.get('/igra/<id_igre>/<vnos>/<kljuc>')
def kaj_zdaj(id_igre, vnos, kljuc):
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    if vnos == '0':
        karta = Model.VLECI
    else: 
        karta = igra.zgorne_karte[-1]
    if kljuc == '0':
        kljuc = False
    else:
        kljuc == True
    uno.kaj_karta_naredi1(int(id_igre), karta, kljuc)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    if kaj == 2:
        return bottle.template('igra2.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
    elif kaj == 3:
        return bottle.template('igra3.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
    elif kaj == 4:
        return bottle.template('igra4.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
    elif kaj == 5:
        return bottle.template('igra5.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
    elif kaj == 7:
        return bottle.template('igra7.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
    elif kaj == 8:
        return bottle.template('igra8.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
    elif kaj == 6:
        if igra.trenutni_igralec == 0:
            return bottle.template('igra60.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
    else:
        return bottle.redirect('/igra/ ' + str(id_igre))


@bottle.post('/poglej2/<id_igre>')
def daj_dve2(id_igre):
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    vnos = bottle.request.forms['ali']
    if vnos == 'da':
        vnos = True
    else:
        vnos = False
    uno.ali_dve_enaki2(int(id_igre), vnos)
    igra.naslednji()
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    bottle.redirect('/igra/ ' + str(id_igre))

@bottle.post('/poglej3/<id_igre>')
def vleci3(id_igre):
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    vnos = bottle.request.forms['ali']
    if vnos == 'da':
        vnos = True
    else:
        vnos = False
    uno.vleci3(int(id_igre), vnos)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    if vnos:
        bottle.redirect('/igra/ ' + str(id_igre) + '/' + '1/0')
    else:
        bottle.redirect('/igra/ ' + str(id_igre))


@bottle.post('/poglej4/<id_igre>')
def barva(id_igre):
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    vnos = bottle.request.forms['barva']
    if vnos == 'rdeca':
        vnos = Model.RDECA
    elif vnos == 'modra':
        vnos = Model.MODRA
    elif vnos == 'rumena':
        vnos = Model.RUMENA
    else:
        vnos = Model.ZELENA
    uno.sprememba_barve4(int(id_igre), vnos)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    bottle.redirect('/igra/ ' + str(id_igre))


@bottle.get('/vlekelkazen/<id_igre>')
def vlekelkazen(id_igre):
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    kazen = []
    igra.naslednji()
    uno.igre[int(id_igre)] = (igra, stanje, kaj, kazen)
    bottle.redirect('/igra/ ' + str(id_igre))

@bottle.post('/poklickazni/<id_igre>')
def piklickazni(id_igre):
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    vnos = bottle.request.forms['ali']
    if vnos == 'da':
        vnos = True
    else:
        vnos = False
    uno.vleci_kazen6(int(id_igre), vnos)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    if vnos:
        bottle.redirect('/igra/ ' + str(id_igre) + '/' + '1/0')
    else:
        return bottle.template('igra8.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)

@bottle.get('/igran/<id_igre>/<vnos>/<kljuc>')
def kaj_zdajn(id_igre, vnos, kljuc):
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    if vnos == '0':
        karta = Model.VLECI
    else: 
        karta = igra.zgorne_karte[-1]
    if kljuc == '0':
        kljuc = False
    else:
        kljuc == True
    uno.kaj_karta_naredi1(int(id_igre), karta, kljuc)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    if kaj == 2:
        uno.ali_dve_enaki2(int(id_igre), True)
        return bottle.template('naspr2.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
    elif kaj == 3:
        if random.random() < 0.8:
            vnos = True
        else: 
            vnos = False
        uno.vleci3(int(id_igre), vnos)
        (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
        if vnos:
            return bottle.template('naspr3.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
        else:
            bottle.redirect('/igra/ ' + str(id_igre))
            #return bottle.template('igra3.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
        #######################################3
    elif kaj == 4:
        barva = igra.nasprotnik_barva()
        uno.sprememba_barve4(int(id_igre), barva)
        return bottle.template('naspr4.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
    elif kaj == 5:
        return bottle.template('igra5.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
    elif kaj == 7:
        return bottle.template('igra7.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
    elif kaj == 8:
        return bottle.template('igra8.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
    elif kaj == 6:
        if igra.trenutni_igralec == 0:
            return bottle.template('igra60.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
    else:
        return bottle.redirect('/igra/ ' + str(id_igre))


@bottle.get('/vmesnan/<id_igre>')
def naslednji(id_igre):
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    igra.naslednji()
    bottle.redirect('/igra/ ' + str(id_igre))



bottle.run(debug=True, reloader=True)