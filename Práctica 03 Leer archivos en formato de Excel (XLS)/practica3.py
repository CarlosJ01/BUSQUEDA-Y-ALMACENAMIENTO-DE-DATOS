# Práctica 3: Leer archivos en formato de Excel (XLS)
# Python 3.8
# Complemento de pandas para leer archivos xlsx
#   pip install xlrd
# ---------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

#Abriendo el archivo
print('Abriendo el archivo XLSX ..........................................')
datos_olimpiada=pd.read_excel("Olympic Athletes.xlsx")

#Base de Datos
print('Guardando en SQLite ...............................................')
conexionBD = sqlite3.connect('olimpiada.db')
cursorBD = conexionBD.cursor()
cursorBD.execute("DROP TABLE IF EXISTS medallas")
cursorBD.execute("CREATE TABLE IF NOT EXISTS medallas (id INTEGER PRIMARY KEY AUTOINCREMENT, Atheta TEXT, Edad TEXT, Pais TEXT, Anio TEXT, fecha_ceremonia TEXT, deporte TEXT, medallas_oro TEXT, medallas_plata TEXT, medallas_bronze TEXT, total_medallas TEXT)")
conexionBD.commit()

#Insetando registros
insertDB = 'INSERT INTO medallas(Atheta, Edad, Pais, Anio, fecha_ceremonia, deporte, medallas_oro, medallas_plata, medallas_bronze, total_medallas) VALUES'
cont = 0
while cont < len(datos_olimpiada)-1:
    insertDB += '("'+str(datos_olimpiada["Athlete"][cont])+'", "'+str(datos_olimpiada["Age"][cont])+'", "'+str(datos_olimpiada["Country"][cont])+'", "'+str(datos_olimpiada["Year"][cont])+'", "'+str(datos_olimpiada["Closing Ceremony Date"][cont])+'", "'+str(datos_olimpiada["Sport"][cont])+'", "'+str(datos_olimpiada["Gold Medals"][cont])+'", "'+str(datos_olimpiada["Silver Medals"][cont])+'", "'+str(datos_olimpiada["Bronze Medals"][cont])+'", "'+str(datos_olimpiada["Total Medals"][cont])+'"),'
    cont+=1
insertDB += '("'+str(datos_olimpiada["Athlete"][cont])+'", "'+str(datos_olimpiada["Age"][cont])+'", "'+str(datos_olimpiada["Country"][cont])+'", "'+str(datos_olimpiada["Year"][cont])+'", "'+str(datos_olimpiada["Closing Ceremony Date"][cont])+'", "'+str(datos_olimpiada["Sport"][cont])+'", "'+str(datos_olimpiada["Gold Medals"][cont])+'", "'+str(datos_olimpiada["Silver Medals"][cont])+'", "'+str(datos_olimpiada["Bronze Medals"][cont])+'", "'+str(datos_olimpiada["Total Medals"][cont])+'")'
cursorBD.execute(insertDB)
conexionBD.commit()

#agrupando
print('Agrupando los athetas .............................................')
nombre_atletas=datos_olimpiada['Athlete']
atletas = []
for at in nombre_atletas:
    if at not in atletas:
        atletas.append(at)

#Anlizando datos
print('Sumando medallas ..................................................')
oro=[]
plata=[]
bronce=[]
for atleta in atletas:
    consulta_atleta = datos_olimpiada[datos_olimpiada['Athlete']==atleta]
    suma_oro=sum(consulta_atleta['Gold Medals'])
    oro.append(suma_oro)    
    suma_plata=sum(consulta_atleta['Silver Medals'])
    plata.append(suma_plata)        
    suma_bronce=sum(consulta_atleta['Bronze Medals'])
    bronce.append(suma_bronce)    

print('Data Frame ......................................................')
final = pd.DataFrame({"Atleta":atletas, 
                        "Oro":oro,
                        "Plata":plata,
                        "Bronce":bronce})

#Obteniendo los ganadores
print('Extrallendo el mayor de cada medalla ............................')
consulta_oro = final['Oro']
max_oro=max(consulta_oro)
consulta_plata = final['Plata']
max_plata=max(consulta_plata)
consulta_bronce = final['Bronce']
max_bronce=max(consulta_bronce)

persona_oro=final['Atleta'][final['Oro']==max_oro]
personas_oro='(ORO)\n'
for oros in persona_oro:
    personas_oro+=oros
    personas_oro+='\n'


persona_plata=final['Atleta'][final['Plata']==max_plata]
personas_plata='(PLATA)\n'
for platas in persona_plata:
    personas_plata+=platas
    personas_plata+='\n'

persona_bronce=final['Atleta'][final['Bronce']==max_bronce]
personas_bronce='(BRONCE)\n'
for bronces in persona_bronce:
    personas_bronce+=bronces
    personas_bronce+='\n'

#Grafica
print('Graficando .....................................................')
personas=[personas_oro, personas_plata, personas_bronce]
medallas=[max_oro, max_plata, max_bronce]
plt.title("Medallistas Olimpicos")
plt.bar(personas, medallas, color=['yellow', 'gray', 'brown'])
plt.show()