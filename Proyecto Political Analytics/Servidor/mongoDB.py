#Contiene funciones para conectar con la base de datos
import pymongo
import time

from pymongo import MongoClient
from datetime import datetime


cliente = MongoClient()
db = cliente['Political_Analytics']

#Crea la base de datos
def crearBD():
    print('Conectando con Mongo DB . . .')
    coleccion = db['candidatos']

    #Crear tabla de candidatos
    if coleccion.count_documents({}) == 0:
        print('Creando candidatos . . .')
        candidatos = [
            {'id': 1, 'nombre': 'Raúl Morón Orozco', 'url_facebook': 'https://www.facebook.com/raulmoronorozco/?ref=page_internal', 'url_twitter': 'https://twitter.com/raulmoronO?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'},
            {'id': 2, 'nombre': 'Carlos Herrera Tello', 'url_facebook': 'https://www.facebook.com/CarlosHerreraSi/?ref=page_internal', 'url_twitter': 'https://twitter.com/carlosherrerasi?fbclid=IwAR3XV7fmGUzKRUlXpOURzT37BoZi3_k_sMmf03aIgq-JCJUga2yg7-dSTrU'},
            {'id': 3, 'nombre': 'Juan Antonio Magaña de la Mora', 'url_facebook': 'https://www.facebook.com/juanAntonioMdelaMora/community/?ref=page_internal', 'url_twitter': 'https://twitter.com/magana_delamora?lang=es'}
        ]
        coleccion.insert_many(candidatos)
    return

#Almacenar resultados de la API y WS en la BD
def almacenarAPIWS(api, webscraping):
    print('Conectando y Almacenando con Mongo DB . . .')
    datosAlmacenados = {
        'api': [],
        'webScraping': [],
        'fechaHora': time.strftime("%d/%m/%y %H:%M:%S")
    }

    #Almacenar datos del api de Twitter
    print('Registrando datos de api de twitter . . .')
    coleccion = db['twitter']
    for datosTW in api:
        documento = {'seguidores': datosTW[1], 'favoritos': datosTW[2], 'twitt': datosTW[3], 'fecha-hora': datosAlmacenados['fechaHora'], 'id_candidato': datosTW[0]}
        datosAlmacenados['api'].append(documento)
        coleccion.insert_one(documento)
    
    #ALmacenar datos del web scraping de facebook
    print('Registrando datos del web scraping de facebook . . .')
    coleccion = db['facebook']
    for datosFB in webscraping:
        documento = {'likes': datosFB[1], 'seguidores': datosFB[2], 'fecha-hora': datosAlmacenados['fechaHora'], 'id_candidato': datosFB[0]}
        datosAlmacenados['webScraping'].append(documento)
        coleccion.insert_one(documento)

    return datosAlmacenados

def almacenarPuntajesTotales(totales, datos):
    print('Conectando y Almacenando con Mongo DB . . .')
    coleccion = db['puntajes_totales']

    #Almacenar Datos
    puntajesTotales = [
        {'puntaje': totales[0], 'fecha-hora': datos['fechaHora'], 'id_candidato': 1},
        {'puntaje': totales[1], 'fecha-hora': datos['fechaHora'], 'id_candidato': 2},
        {'puntaje': totales[2], 'fecha-hora': datos['fechaHora'], 'id_candidato': 3},
    ]
    datos['puntajesTotales'] = puntajesTotales
    coleccion.insert_many(puntajesTotales)

    return datos

def getCandidatos():
    print('Conectando y Almacenando con Mongo DB . . .')
    coleccion = db['candidatos']
    #Optener a los candidatos
    candidatos = []
    for candidato in coleccion.find({}, {'_id': 0}):
        candidatos.append(candidato)
    return candidatos

def getPuntajesAcumalos():
    print('Conectando y Almacenando con Mongo DB . . .')
    datos = {
        '1': {
            'tw': [],
            'fb': []
        },
        '2': {
            'tw': [],
            'fb': []
        },
        '3': {
            'tw': [],
            'fb': []
        },
    }

    print('Extrayendo datos almacenados . . .')
    #Datos de Twitter
    coleccion = db['twitter']
    for i in (range(3)):
        i += 1
        for puntajes in coleccion.find({'id_candidato': str(i)}, {'twitt':0, 'fecha-hora': 0, 'id_candidato': 0}):
            datos[str(i)]['tw'].append(puntajes)

    #Datos de Facebook
    coleccion = db['facebook']
    for i in (range(3)):
        i += 1
        for puntajes in coleccion.find({'id_candidato': str(i)}, {'_id': 0, 'fecha-hora': 0, 'id_candidato': 0}):
            datos[str(i)]['fb'].append(puntajes)
    return datos

def getTweet(id):
    print('Conectando y Almacenando con Mongo DB . . .')
    coleccion = db['twitter']
    
    #Extrayendo el ultimo tweet almacenado
    print('Extrayendo twitt . . .')
    tweet = coleccion.find_one({'_id': id})
    return tweet['twitt']

def getPuntosTotales():
    print('Conectando y Almacenando con Mongo DB . . .')
    coleccion = db['puntajes_totales']
    datos = {
        '1': [],
        '2': [],
        '3': [],
    }

    #Extrayendo puntajes totales
    print('Extrayendo datos almacenados . . .')
    for i in (range(3)):
        i += 1
        orden = 1
        for puntos in coleccion.find({'id_candidato': i}, {'_id': 0, 'id_candidato': 0}):
            puntos['orden'] = orden
            datos[str(i)].append(puntos)
            orden += 1
    return datos