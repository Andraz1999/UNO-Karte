% rebase('base.tpl')

% if igra.trenutni_igralec == 0:
%   trenutni = 'Igralec'
% else: trenutni = 'Nasprotnik' + str(igra.trenutni_igralec)
% end
% import Model
% na1 = str(len(igra.igralci[1]))
% if igra.igralci[1] == Model.IZPADEL:
% na1 = 'X'
% end
% na2 = str(len(igra.igralci[2]))
% if igra.igralci[2] == Model.IZPADEL:
% na2 = 'X'
% end
% na3 = str(len(igra.igralci[3]))
% if igra.igralci[3] == Model.IZPADEL:
% na3 = 'X'
% end
% ime1 = '/static/' + 'nasprotnik' + na1 + '.jpg'
% ime2 = '/static/' + 'nasprotnik' + na2 + '.jpg'
% ime3 = '/static/' + 'nasprotnik' + na3 + '.jpg'
% obdelava = '/obdelava'

<h2 align='center'> Na vrsti je {{trenutni}}. </h2>


<table align= 'center' border="0" cellspacing="0" cellpadding="8" width="1000px">
 

<tr>
    <td>
% if igra.smer == 1:
% smer = '/static/smer1.png'
% drgac = 'smer urnega kazalca'
%else:
%smer = '/static/smer0.png'
% drgac = 'nasprotna smer urnega kazalca'
%end
        <img src= '{{smer}}' arc= '{{drgac}}' height="150" />


    </td>
    <td colspan="2">
        <h4 align = 'center'>Nasprotnik2</h4>
        <p align = 'center'> 
       
        
        
                <img src= {{ime2}} alt = {{na2}} height="150"/></p>
            
    </p>
  

</td>
</tr>
<tr>
<td >
    <h4 align = 'left' >Nasprotnik1</h4>

  
    <p align = 'center'> 
       
        
        
            <img src= {{ime1}} alt = {{na1}} height="150"/></p>
                   
</p> </td>

<td>
    <p align='left'> 
                % zgorna = igra.zgorne_karte[-1]
                % zgorna_karta = '/static/' + str(zgorna) + '.jpg'
                            <p><figure>
                                <figcaption align= "center">Zgorna karta</figcaption> 
                                <img align= 'center' src= '{{ zgorna_karta}}' alt= "{{ zgorna }}" height="150"/>
                            </figure>
</p></td><td>

        
            <figure>
                        <figcaption align= "center">Kupček</figcaption> 
                        <form align= "center" action="{{obdelava}}" method="post">
                                <input type="hidden" name="poteza" value="0">
                                <input type="image" src= '/static/nasprotnik1.jpg',  alt = "Kupček", height="150"/>
                                 </form>
                    
                    </figure>
                    

            
            </p>
</td>
<td>
 <h4 align= 'right'>Nasprotnik3</h4>

 <p align = 'center'> 
       
        
        
        <img src= {{ime3}} alt = {{na3}} height="150"/></p>
    
</p> </td> 
</tr>
<tr>
<td colspan="4" id="spodnja">
    <h4 align='center'>Tvoje karte</h4>

    <form align="center" action="{{obdelava}}" method="POST">
        % for i in range(len(igra.igralci[0])):
        % slika = '/static/' +  str(igra.igralci[0][i]) + '.jpg'
        % karta = str(igra.igralci[0][i])
        % vrednost = i + 1
        
        
        <button type="submit" name="poteza" value="{{vrednost}}"><img src= "{{ slika }}",  alt = "{{ karta }}", height="150"/></button>
        
    
        % end
    </form>


            
       
        

    </p>
</td>
</tr>
</table>