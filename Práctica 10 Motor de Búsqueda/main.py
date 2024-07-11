# Práctica 10: Motor de Búsqueda
# Objetivo: Construir un motor de búsqueda de información en Internet
# ---------------------------------------------------------------------------
# Libreria para MongoDB
# pip install pymongo
# ----------------------------------------------------------------------------

# ------------------------------------ Librerias ------------------------------------
import pymongo
import json

from pymongo import MongoClient
from webScraping import extraccion
#------------------------------------------------------------------------------------

#Inicia el motor
def motorBusqueda(coleccion):
    salir = True
    while salir:
        #Optener el primer elemento que no esta revisado
        jsonQuery = coleccion.find_one({'revisada':False})
        if(jsonQuery):
            #print(jsonQuery)
            print(jsonQuery['direccion'])
            datos=extraccion(jsonQuery['direccion'])
            #print(datos)
            if(len(datos)==0):
                myquery = { "_id": jsonQuery['_id'] }
                newvalues = { "$set": { "revisada": True } }
                coleccion.update_one(myquery, newvalues)
            else: 
                myquery = { "_id": jsonQuery['_id'] }
                newvalues = { "$set": { "titulo": datos[0],
                                        "keywords": datos[1],
                                        "descripcion": datos[2],
                                        "palabra1": datos[3][0],
                                        "palabra2": datos[3][1],
                                        "palabra3": datos[3][2],
                                        "revisada": True } }
                coleccion.update_one(myquery, newvalues)
                #Obtener enlaces
                for url in datos[4]:    
                    pag_existe = coleccion.find_one({'direccion': url})
                    if(pag_existe):
                        myquery = { "_id": pag_existe['_id'] }
                        newvalues = { "$set": { "ranking": (pag_existe['ranking']+1) } }
                        coleccion.update_one(myquery, newvalues)
                    else:
                        registroNuevo = {
                            "direccion": url,
                            "titulo": "",
                            "keywords": "",
                            "descripcion": "",
                            "palabra1": "",
                            "palabra2": "",
                            "palabra3": "",
                            "ranking": 0,
                            "revisada": False
                        }
                        coleccion.insert_one(registroNuevo)
                
        else:
            print("No hay registros por buscar")
            salir=False


#Funcion principal
def main():
    # Conectar con el servidor de mongo DB
    cliente = MongoClient()
    db = cliente['BAD-Motor']  # Base de datos
    coleccion = db['Motor-Busqueda']  # Coleccion (Tabla)

    #Contar el numero de registros en la BD y si es 0 insertear el primer dato
    if coleccion.count_documents({}) == 0:
        # Insertar
        registroInicial = {
            "direccion": "http://sagitario.itmorelia.edu.mx/~rogelio/hola.htm",
            "titulo": "",
            "keywords": "",
            "descripcion": "",
            "palabra1": "",
            "palabra2": "",
            "palabra3": "",
            "ranking": 0,
            "revisada": False
        }
        coleccion.insert_one(registroInicial)
    
    # Iniciamos el motor
    motorBusqueda(coleccion)
    
if __name__ == "__main__":
    main()
