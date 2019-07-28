import bottle
import Model
import random
SKRIVNI_KLJUC = 'Uno karte so fajn'


uno = Model.Uno('stanje.json')

@bottle.get('/')
def prva_stran():
    uno.nalozi_igre_iz_datotek()
    if uno.igre == {}:
        return bottle.template('index.tpl')
    else:
        return bottle.template('index2.tpl', uno= uno)

@bottle.get('/static/<ime_slike>')
def prikazi_sliko(ime_slike):
    return bottle.static_file(ime_slike, root = './img')




@bottle.post('/nova_igra/')
def zacni_novo_igro():
    # naredi novo igro in preusmeri na nov naslov
    id_igre = uno.nova_igra()
    bottle.response.set_cookie('id_igre', id_igre, secret=SKRIVNI_KLJUC, path='/')
    bottle.redirect('/igra')
    return 


@bottle.get('/pravila_igre/')
def prikaz_pravil():
    return bottle.template('pravila_igre.tpl')

@bottle.get('/igra')
def prikazi_igro():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    uno.nalozi_igre_iz_datotek()
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    if stanje == Model.ZMAGA:
        return bottle.template('zmaga.tpl')
    elif stanje == Model.PORAZ:
        return bottle.template('poraz.tpl')
    if igra.trenutni_igralec == 0:
        return bottle.template('igra.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)    
    else:
        return bottle.template('igranpriprava.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
        

@bottle.post('/igranpri')
def nasprotnik():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    karta = igra.nasprotnik()
    uno.poklic_karte0(int(id_igre), karta)
    if karta == Model.VLECI:
        bottle.redirect('/naspr/0')
    else:
        bottle.redirect('/naspr/1')

@bottle.get('/naspr/<st>')
def naspr(st):
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    if st == '0':
        return bottle.template('igranasprotnikvleci.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
    else:
        return bottle.template('igranasprotnik.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)


@bottle.post('/obdelava')
def poteza():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    id_igre = int(id_igre)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    vnos = int(bottle.request.forms['poteza'])
    if vnos == 0:
        karta = Model.VLECI
        print('obdelava vlece')
        uno.poklic_karte0(id_igre, karta)
        bottle.redirect('/igra/ ' + str(vnos) + '/' +  '1' )
    else:
        karta = igra.igralci[igra.trenutni_igralec][vnos - 1]
        if karta in igra.mozne_izbire():
            uno.poklic_karte0(id_igre, karta)
            bottle.redirect('/igra/ ' + str(vnos) + '/' +'1')
        else:
            bottle.redirect('/napaka')

@bottle.get('/napaka')
def poslji_nazaj():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    return bottle.template('igra_napaka.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)



@bottle.get('/igra/<vnos>/<kljuc>')
def kaj_zdaj(vnos, kljuc):
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    if int(vnos) == 0:
        karta = Model.VLECI
        print('igra vlece')
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
            bottle.redirect('/kolikobovlekel')
    else:
        bottle.redirect('/shrani1')
        

@bottle.get('/kolikobovlekel')
def nasprotnik():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    verjetnost = random.random()
    if verjetnost <= 0.8:
        vnos = True
    else:
        vnos = False
    uno.vleci_kazen6(int(id_igre), vnos)
    if vnos:
        bottle.redirect('/igra/pocasi')
    else:
        bottle.redirect('/igra/hitro')



@bottle.get('/igra/hitro')
def neka_za_vmes():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    return bottle.template('igra8.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)

@bottle.get('/igra/pocasi')
def vmes():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    return bottle.template('igranasprotnik0.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)

@bottle.post('/poglej2')
def daj_dve2():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    vnos = bottle.request.forms['ali']
    if vnos == 'da':
        vnos = True
    else:
        vnos = False
    uno.ali_dve_enaki2(int(id_igre), vnos)
    igra.naslednji()
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    bottle.redirect('/shrani1')
    

@bottle.post('/poglej3')
def vleci3():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    vnos = bottle.request.forms['ali']
    if vnos == 'da':
        vnos = True
    else:
        vnos = False
    uno.vleci3(int(id_igre), vnos)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    if vnos:
        bottle.redirect('/igra/1/0')
    else:
        bottle.redirect('/shrani1')
        


@bottle.post('/poglej4')
def barva():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
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
    bottle.redirect('/shrani1')
    


@bottle.post('/vlekelkazen')
def vlekelkazen():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    kazen = []
    igra.naslednji()
    uno.igre[int(id_igre)] = (igra, stanje, kaj, kazen)
    bottle.redirect('/shrani1')
    

@bottle.post('/poklickazni')
def poklickazni():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    vnos = bottle.request.forms['ali']
    if vnos == 'da':
        vnos = True
    else:
        vnos = False
    uno.vleci_kazen6(int(id_igre), vnos)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    if vnos:
        bottle.redirect('/igra/1/0')
    else:
        return bottle.template('igra8.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)

@bottle.get('/igran/<vnos>/<kljuc>')
def kaj_zdajn(vnos, kljuc):
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
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
        return bottle.template('naspr2.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)
    elif kaj == 3:
            bottle.redirect('/nas3')
    elif kaj == 4:
        bottle.redirect('/pobarvan')
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
            bottle.redirect('/kolikobovlekel')
    else:
        bottle.redirect('/shrani1')
        

@bottle.get('/pobarvan')
def nasprotnik_barva():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    barva = igra.nasprotnik_barva()
    uno.sprememba_barve4(int(id_igre), barva)
    bottle.redirect('/prikazbarve')

@bottle.get('/prikazbarve')
def prikaz_barve():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    return bottle.template('naspr4.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)



@bottle.get('/vmesnan')
def naslednji():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    igra.naslednji()
    bottle.redirect('/shrani1')
    

@bottle.post('/stop')
def stop():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    igra.naslednji()
    igra.naslednji()
    bottle.redirect('/shrani1')
    

@bottle.post('/spremembasmeri')
def sprememba_smeri():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    igra.zamenjaj_smer()
    igra.naslednji()
    bottle.redirect('/shrani1')
    

@bottle.post('/poglej5')
def vleci5():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    zgorna = igra.zgorna_barvna_karta()
    igra.vleci_pet(zgorna[1])
    igra.naslednji()
    bottle.redirect('/shrani1')
    

@bottle.post('/nas2')
def poglej2():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    uno.ali_dve_enaki2(int(id_igre), True)
    igra.naslednji()
    bottle.redirect('/shrani1')
   

@bottle.get('/nas3')
def ali_je_v_redu():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    if random.random() < 0.8:
        vnos = True
    else: 
        vnos = False
    uno.vleci3(int(id_igre), vnos)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    if vnos:
        bottle.redirect('/vmesna1/vleci')
    else:
        bottle.redirect('/vmesna2/vleci')

@bottle.get('/vmesna1/vleci')
def vmesna1():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    return bottle.template('naspr31.tpl', id_igre= id_igre, igra= igra, stanje= stanje, kaj= kaj, kazen= kazen)

@bottle.get('/vmesna2/vleci')
def vmesna2():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    bottle.redirect('/shrani1')
    


@bottle.post('/shrani/')
def shrani():
    uno.zapisi_igre_v_datoteko()
    bottle.redirect('/')

@bottle.get('/shrani1')
def shrani():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, stanje, kaj, kazen) = uno.igre[int(id_igre)]
    uno.zapisi_igre_v_datoteko()
    bottle.redirect('/igra')


bottle.run(debug=True, reloader=True)