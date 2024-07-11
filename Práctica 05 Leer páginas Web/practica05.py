# Práctica 5 Leer páginas Web
# Leer y extraer información de páginas Web los principales titulos
#---------------------------------------------------------------------
# Python 3.8.6 => Windows 10
# Libreria Beautifulsoup => pip install beautifulsoup4
# Libreria de requests => pip install requests
# Libreria para imagenes tkinter => pip install image
#---------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk, PhotoImage, Label
from PIL import ImageTk, Image

#Obtener URL de las fotografias
def obtener_url(estilo):
    explode1=estilo.split("(")
    explode2=explode1[1].split(")")
    url=explode2[0]
    return url

#Conectamos con la paguina
try:
    paguina = requests.get("https://www.fayerwayer.com/")
    html = BeautifulSoup(paguina.content, 'html.parser')
    conexion = True
except:
    print('No puede conectarse a la página https://www.fayerwayer.com/')
    conexion = False

if conexion:
    #Analizando las paguinas
    titulos = []
    enlaces = []
    seccion = html.find_all('section', class_='featured-news container js-skin-content-wrapper')
    items = seccion[0].find_all('div', class_='item')
    for item in items:
        enlace=item.find('a')
        if enlace != None:
            estilo=(enlace.get('style'))
            enlaces.append(obtener_url(estilo))
        contenido = item.find('div', class_='content')
        if contenido != None:
            titulos.append(contenido.find('h2').text)
    
    #Imprimir principales titulos Consola
    print("TÍTULOS PRINCIPALES EXTRAÍDOS DE UNA PÁGINA WEB => www.fayerwayer.com")
    imagenes=[]
    for i in [0, 1, 2]:
        imagen=enlaces[i].split("/")[6]
        nombre_imagen=str(i+1)+"."+imagen.split(".")[1]
        imagenes.append(nombre_imagen)
        imagen=requests.get(enlaces[i]).content
        with open(nombre_imagen, 'wb') as handler:
            handler.write(imagen)  
        print('\t['+str(i+1)+'] => \t'+titulos[i])
    
    #Grafico
    ventana=tk.Tk()
    ventana.geometry("650x400")
    ventana.configure(bg='#ff3300')
    ventana.title("Titulos principales de www.fayerwayer.com")

    titulo1 = ttk.Label(ventana, text="NOTICIA 1: "+titulos[0]).place(x=100, y=0)
    img1=ImageTk.PhotoImage(Image.open(imagenes[0]).resize((100,100), Image.ANTIALIAS))
    Label(ventana,image=img1).place(x=270, y=20)
    
    ttk.Label(ventana, text="NOTICIA 2: "+titulos[1]).place(x=100, y=130)
    img2=ImageTk.PhotoImage(Image.open(imagenes[1]).resize((100,100), Image.ANTIALIAS))
    Label(ventana,image=img2).place(x=270, y=150)

    ttk.Label(ventana, text="NOTICIA 3: "+titulos[2]).place(x=100, y=270)
    img3=ImageTk.PhotoImage(Image.open(imagenes[2]).resize((100,100), Image.ANTIALIAS))
    Label(ventana,image=img3).place(x=270, y=290)

    ventana.mainloop()