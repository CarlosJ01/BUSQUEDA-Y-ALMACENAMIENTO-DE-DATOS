import requests
from bs4 import BeautifulSoup

#Llamnado al metodo 
from limpieza import depurar


def extraccion(direccion):
    print("Extrayendo datos de "+str(direccion))
    try:
        pagina = requests.get(direccion)
        html = BeautifulSoup(pagina.content, 'html.parser')
        conexion = True
        print("")
    except:
        print('No puede conectarse a la página '+str(direccion))
        conexion = False
    
    if conexion:
        arr=[]

        titulo = html.find('title') #titulo de la pagina
        if(titulo!=None):
            titulo=titulo.text
        else:
            titulo=""
        arr.append(titulo)
        #------------------METAS--------------------

        #Keyword
        keyword=html.find("meta", {"name":"keywords"})
        if(keyword!=None):
            keyword=keyword.get('content')
        else:
            keyword=""
        arr.append(keyword)

        #-------------- Get descripcion ----------------
        descripcion=html.find("meta", {"name":"description"})
        if(descripcion!=None):
            descripcion=descripcion.get('content')
        else:
            descripcion=""
        arr.append(descripcion)

        #----------- Get texto ---------------------
        textos=html.find_all('p')
        cadena=""

        for t in textos:
            cadena=cadena+" "+t.text
        
        #-------------- Get palabras -------------
        elementos=depurar(cadena)
        palabras=[]

        if(len(elementos)<3):
            indice=3-len(elementos)
            for elemento in elementos:
                palabras.append(elemento[0])
            for i in range(indice):
                palabras.append("")
        else:    
            for elemento in elementos:
                palabras.append(elemento[0])

        arr.append(palabras)
        
        #--------------- Get enlaces ---------------
        enlaces=[]
        urls=html.find_all('a')
        
        for url in urls:
            ##if((url.get('href'))[0:4] == "http"):
                enlaces.append(url.get('href'))

        arr.append(enlaces)
        
        return arr
    else:
        return []

        

    
