%  rebase('base.tpl')


  <h1>Dobrodošli v UNO kartah!</h1>

  <img src= '/static/uno-karte.jpg'/>


  <!--<img src="img/10.jpg" alt="obesanje">-->

  <form action="/nova_igra/" method="post">
    <button type="submit">Igraj</button>
  </form>

  <form action="/pravila_igre/", method='GET'>
    <button type="submit">Pravila igre</button>
  </form>