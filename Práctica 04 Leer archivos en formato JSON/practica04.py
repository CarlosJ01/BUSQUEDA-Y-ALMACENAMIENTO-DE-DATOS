# Práctica 4: Leer archivos en formato JSON
# Python 8.3 en Windows 10
# Libreria de requests -> pip install requests

import requests
import json
import sqlite3
from datetime import datetime
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt

#Funciones para la peticion a OpenWeatherMap API
def peticionAPI(ciudad):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    headers = {
        'x-rapidapi-key': "36e38d330amshdf10f3cb12f62dfp163d00jsn039be0388006",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }
    parametros = {
        "q": ciudad+',MX',
        "units": "metric"
    }
    response = requests.request("GET", url, headers=headers, params=parametros)
    return response

# Busqueda de la temperatura
def buscarTemperatura():
    boton.configure(state='disabled', text='Buscando')
    # Peticion a la API
    try:
        print('Peticiones a la API ...................................................')
        respuesta1 = peticionAPI(ciudad1.get())
        respuesta2 = peticionAPI(ciudad2.get())
    except:
        print('Error al hacer la peticion a la API')
    #Si la peticion a la API salio bien
    if respuesta1.status_code == 200 and respuesta2.status_code == 200:
        # Convertir a JSON
        print('Extraer datos a JSON ..................................................')
        datosCiudad1 = json.loads(respuesta1.text)
        datosCiudad2 = json.loads(respuesta2.text)

        #Base de Datos SQLite
        print('Conectando a SQLite ...................................................')
        conexionBD = sqlite3.connect('clima.db')
        cursorBD = conexionBD.cursor()
        cursorBD.execute("CREATE TABLE IF NOT EXISTS temperatura (id INTEGER PRIMARY KEY AUTOINCREMENT, ciudad TEXT, temperatura TEXT, fecha_hora TEXT)")
        conexionBD.commit()

        #Insertar a la Base de Datos
        print('Registrando temperaturas ..............................................')
        cursorBD.execute('INSERT INTO temperatura(ciudad, temperatura, fecha_hora) VALUES ("'+ciudad1.get()+'", "'+str(datosCiudad1['main']['temp'])+'°C", "'+str(datetime.today())+'")')
        cursorBD.execute('INSERT INTO temperatura(ciudad, temperatura, fecha_hora) VALUES ("'+ciudad2.get()+'", "'+str(datosCiudad2['main']['temp'])+'°C", "'+str(datetime.today())+'")')
        conexionBD.commit()

        #Temperaturas de ciudades
        print('Temperaturas encontradas ..............................................')
        print(ciudad1.get() + '\t=>\t' + str(datosCiudad1['main']['temp']) + '°C')
        print(ciudad2.get() + '\t=>\t' + str(datosCiudad2['main']['temp']) + '°C')
        boton.configure(state='enabled', text='Buscar')
        
        #Graficacion
        plt.subplots()
        ciudades = [ciudad1.get()+'\n'+str(datosCiudad1['main']['temp']) + '°C', ciudad2.get()+'\n'+str(datosCiudad2['main']['temp']) + '°C']
        temperaturas = [datosCiudad1['main']['temp'], datosCiudad2['main']['temp']]
        plt.title("Temperatura de dos ciudades")
        plt.bar(range(2), temperaturas, color=['red', 'blue'])
        plt.xticks(range(2), ciudades)
        plt.ylim(min(temperaturas)-1, max(temperaturas)+1)
        plt.show()
    else:
        print('No pudo conectarse a la API')
    
    boton.configure(state='enabled', text='Buscar')
    return

# GUI
window = Tk()
window.title("Práctica 4: Leer archivos en formato JSON")
window.geometry("600x170")
window.configure(bg='#2271b3')
window.resizable(0, 0)

# Titulos
titulo = Label(window, text="Clima de dos ciudades de México")
titulo.pack(anchor=CENTER)
titulo.config(
    fg="black",
    bg="#2271b3",
    font=("Courier", 20)
)
Label(window, text="Selecciona dos ciudades:").place(x=230, y=50)

# ComboBox
ciudades = ["Aguascalientes", "Mexicali", "La Paz", "San Francisco de Campeche", "Tuxtla Gutiérrez",
            "Chihuahua", "Saltillo", "Colima", "Victoria de Durango", "Toluca de Lerdo", "Guanajuato",
            "Chilpancingo de los Bravo", "Pachuca de Soto", "Guadalajara", "Morelia", "Cuernavaca",
            "Tepic", "Monterrey", "Oaxaca de Juárez", "Puebla de Zaragoza", "Santiago de Querétaro",
            "Chetumal", "San Luis Potosí", "Culiacán Rosales", "Hermosillo", "Villahermosa", "Ciudad Victoria",
            "Tlaxcala de Xicohténcatl", "Xalapa-Enríquez", "Mérida", "Zacatecas"]

ciudad1 = ttk.Combobox(window, width=17, state='readonly')
ciudad1.place(x=130, y=80)
ciudad1['values'] = ciudades
ciudad1.current(0)
ciudad1.config(
    font=("Courier", 10)
)
ciudad2 = ttk.Combobox(window, width=17, state='readonly')
ciudad2.place(x=300, y=80)
ciudad2['values'] = ciudades
ciudad2.current(0)
ciudad2.config(
    font=("Courier", 10)
)

# Boton
boton = ttk.Button(window, text="Buscar", command=buscarTemperatura)
boton.place(x=270, y=110)

window.mainloop()