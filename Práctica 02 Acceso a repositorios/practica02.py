#pip install covid
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt 
from covid import Covid
import json

def obtener_pais():
    covid = Covid()
    covid.get_data()

    nombre_pais = lista.get()
    if(nombre_pais == "Alemania"):
        buscar = "germany" 
    elif (nombre_pais == "España"):
        buscar = "spain"
    elif (nombre_pais == "Francia"):
        buscar = "france"
    elif (nombre_pais == "Islandia"):
        buscar = "iceland"        
    elif (nombre_pais == "Mexico"):
        buscar = "mexico" 
    elif (nombre_pais == "Argentina"):
        buscar = "argentina"         
    elif (nombre_pais == "Italia"):
        buscar = "italy"
    elif (nombre_pais == "China"):
        buscar = "china"
    elif (nombre_pais == "Brasil"):
        buscar = "brazil"
    elif (nombre_pais == "Canada"):
        buscar = "canada"

    cases = covid.get_status_by_country_name(buscar)
    confirmados = cases['confirmed']
    muertos = cases['deaths']
    activos = cases['active']
    recuperados = cases['recovered']

    porcentaje_muertos = (100 * muertos)/confirmados
    porcentaje_activos = (100 * activos)/confirmados
    porcentaje_recuperados = (100 * recuperados)/confirmados
    print(cases)

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Activos', 'Muertos', 'Recuperados'
    sizes = [porcentaje_activos, porcentaje_muertos, porcentaje_recuperados]
    explode = (0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    #ax1.set_title("Estadísticas de casos confirmados de COVID-19 en "+ nombre_pais)
    plt.title("Estadísticas de casos confirmados de COVID-19 en "+ nombre_pais, fontsize=14)

    plt.xlabel("Total de casos confirmados: " + str(confirmados))                  
    plt.show()
    print(lista.get())

window = Tk()
window.title("Status Covid-19")
window.geometry("600x400")
window.resizable(0,0)

imagen = PhotoImage(file="fondo3.gif")
fondo = Label(window, image=imagen).place(x=0,y=0)

titulo = Label(window, text="Status Covid-19 en el mundo")
titulo.pack(anchor=CENTER)
titulo.config(fg="black",    # Foreground
             bg="white",   # Background
             font=("Courier",24)) 

#combobox
lista=ttk.Combobox(window, width=17, state='readonly')
lista.place(x=210, y=200)
my_list = ["Alemania", "Mexico", "Brasil", "Italia", "China", "España", "Canada", "Argentina", "Islandia", "Francia"]
lista['values']=my_list
lista.current(0)

selecciona_pais = Label(window, text="Selecciona un país:").place(x=230, y=170)

#botón
Button(window, text="Buscar!", command=obtener_pais, bg="blue").place(x=400, y=200)

window.mainloop()
