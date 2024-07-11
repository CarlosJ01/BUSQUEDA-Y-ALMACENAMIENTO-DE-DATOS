# pip install beautifulsoup4
#pip install request

import requests
from bs4 import BeautifulSoup

def webScrapingFacebook():
    print('Web Scraping de paguinas estaticas de facebook . . .')
    urls=[]
    urls.append("https://www.facebook.com/pg/raulmoronorozco/community/?ref=page_internal")
    urls.append("https://www.facebook.com/pg/CarlosHerreraSi/community/?ref=page_internal")
    urls.append("https://www.facebook.com/pg/juanAntonioMdelaMora/community/?ref=page_internal")

    candidatos=[]
    cont=0

    for url in urls:
        datos=[]
        cont=cont+1

        datos.append(str(cont))

        #Conectamos con la pagina
        print('\tConectando con la paguina: '+url+' . . .')
        try:
            pag = requests.get(url)
            html = BeautifulSoup(pag.content, 'html.parser')
            conexion = True
        except:
            print('\tNo puede conectarse a la página '+url)
            conexion = False

        if conexion:
            print('\tAnalizando paguina: '+url+' . . .')
            comunidad = html.find('div', class_='clearfix _ikh _3xol')
            
            #Obtener los likes de la página
            seccion = (comunidad.find_all('div', class_='_3xom'))
            seccion_likes=seccion[0].text
            likes=seccion_likes.replace("\xa0mil", "000")

            seccion_seguidores=seccion[1].text
            seguidores=seccion_seguidores.replace("\xa0mil", "000")

            likes=likes.replace(".", "")
            seguidores=seguidores.replace(".", "")


            datos.append(likes)
            datos.append(seguidores)

            candidatos.append(datos)
        else:
            datos.append("")
            datos.append("")
            candidatos.append(datos)
    return candidatos
        
    