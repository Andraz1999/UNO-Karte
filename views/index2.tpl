%  rebase('base.tpl')


  <h1 align="center" >Dobrodošli v UNO kartah!</h1>

  <img align= "center" src= '/static/uno-karte.jpg'/>


  

  <form align="center" action="/nova_igra/" method="post">
    <button type="submit">Igraj</button>
  </form>

  <form align="center" action="/pravila_igre/", method='GET'>
    <button type="submit">Pravila igre</button>
  </form>

   <form align="center" action="/igra", method='GET'>
    <button type="submit">Igraj od tam, kjer si ostal</button>
  </form>

%import Model
% stevec = 0
%zmaga = 0
 % for i in uno.igre:
 % stevec += 1
 % if uno.igre[i][1] == Model.ZMAGA:
 % zmaga += 1
 % end
 % end
 % razmerje = zmaga / stevec * 100
 % razmerje = int(razmerje)
 <p align="center"><h3> Trenutno je zmagalo {{ razmerje }}% igralcev.</h3></p>