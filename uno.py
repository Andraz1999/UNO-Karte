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
    return bottle.template('igra.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)


@bottle.post('/obdelava/<id_igre>')
def poteza(id_igre):
    id_igre = int(id_igre)
    #print(str(id_igre))
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    vnos = int(bottle.request.forms['poteza'])
    if vnos == 0:
        karta = Model.VLECI
        uno.poklic_karte0(id_igre, karta)
        bottle.redirect('/igra/ ' + str(id_igre))
        #bottle.redirect('/igra/ ' + str(id_igre) + '/' + str(karta))
    else:
        karta = igra.igralci[igra.trenutni_igralec][vnos - 1]
        if karta in igra.mozne_izbire():
            uno.poklic_karte0(id_igre, karta)
            bottle.redirect('/igra/ ' + str(id_igre) + '/' + '1')
        else:
            bottle.redirect('/napaka/ ' + str(id_igre))

@bottle.get('/napaka/<id_igre>')
def poslji_nazaj(id_igre):
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    return bottle.template('igra_napaka.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)



@bottle.get('/igra/<id_igre>/1')
def kaj_zdaj(id_igre):
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    uno.kaj_karta_naredi1(int(id_igre))
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    if kaj == 2:
        return bottle.template('igra2.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)

@bottle.post('/poglej2/<id_igre>')
def daj_dve2(id_igre):
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    vnos = bottle.request.forms['ali']
    if vnos == 'da':
        vnos = True
    else:
        vnos = False
    uno.ali_dve_enaki2(int(id_igre), vnos)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    bottle.redirect('/igra/ ' + str(id_igre))















bottle.run(debug=True, reloader=True)