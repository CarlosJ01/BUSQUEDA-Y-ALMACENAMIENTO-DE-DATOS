# Web Services de Polytical Analitics
#------------------------------------------------------------------------------------------
# Bottle => pip install bottle
# Libreria para MongoDB => pip install pymongo
#------------------------------------------------------------------------------------------

#Librerias
import bottle
import pymongo
import random

from bottle import route, run, template
from bottle import response
from pymongo import MongoClient

#Archivos externos
from candidatosTwitter import apiTwitter
from candidatosFacebook import webScrapingFacebook
from mongoDB import crearBD 
from mongoDB import almacenarAPIWS, almacenarPuntajesTotales, getCandidatos
from mongoDB import getPuntajesAcumalos, getTweet, getPuntosTotales

#Variables Globales
cliente = MongoClient()
db = cliente['BAD-Motor']
app = bottle.app()

#CORS
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            return fn(*args, **kwargs)
    return _enable_cors

#Metodo principal
def main():
    #Crear la base de datos de los candidatos
    crearBD()
    #Arranque del Web Services
    app.run(port=8080)
#-------------------------------- Web Services -------------------------------------------------------

@app.route('/', method=['GET'])
def index():
    return 'http://127.0.0.1:8080/consulta => Consulta de la informacion a la base de datos y la analisa <br> http://127.0.0.1:8080/recoleccion/api-webScraping => Recoleta informacion de API y Web Scraping, Analiza y Almacena'

@route('/consulta')
@enable_cors
def consulta_info():
    response.headers['Content-type'] = 'application/json'

    #JSON a enviar
    datos = {
        '1': {
            'likes_F': 0,
            'seguidores_F': 0,
            'seguidores_T': 0,
            'favoritos_T': 0,
            'twett': '',
            'puntajes': []
        },
        '2': {
            'likes_F': 0,
            'seguidores_F': 0,
            'seguidores_T': 0,
            'favoritos_T': 0,
            'twett': '',
            'puntajes': []
        },
        '3': {
            'likes_F': 0,
            'seguidores_F': 0,
            'seguidores_T': 0,
            'favoritos_T': 0,
            'twett': '',
            'puntajes': []
        },
    }
    #Analizando los datos de likes, seguidores y favoritos de la Base de Datos
    puntajes = getPuntajesAcumalos()
    for i in range(3):
        i += 1
        print('Analizando los datos del candidato '+ str(i) + '. . .')

        puntosFB = puntajes[str(i)]['fb']
        for puntoFB in puntosFB:
            datos[str(i)]['likes_F'] += int(puntoFB['likes'])
            datos[str(i)]['seguidores_F'] += int(puntoFB['seguidores'])

        puntosTW = puntajes[str(i)]['tw']
        for puntoTW in puntosTW:
            datos[str(i)]['seguidores_T'] += int(puntoTW['seguidores'])
            datos[str(i)]['favoritos_T'] += int(puntoTW['favoritos'])

        datos[str(i)]['twett'] = getTweet(puntoTW['_id'])
    
    #Analizando puntajes totales
    puntosTotales = getPuntosTotales()
    for i in range(3):
        i += 1

        #Variables regresion lineal
        #----------------------------------------------
        # x => 'orden'
        # y => 'puntaje'
        #----------------------------------------------

        n = len(puntosTotales[str(i)])
        xy = 0
        x = 0
        y = 0
        x2 = 0

        for punto in puntosTotales[str(i)]:
            xy += int(punto['orden']) * int(punto['puntaje'])
            x += int(punto['orden'])
            y += int(punto['puntaje'])
            x2 += int(punto['orden']) * int(punto['orden'])
        
        #Formulas de regresion lineal
        #----------------------------------------------
        # a = (n*Exy - ExEy) / (nEx2 - (Ex)2)
        # b = (Ey - aEx) / n
        # y = ax + b
        #----------------------------------------------
        a = ((n*xy) - (x*y)) / ((n*x2) - (x*x))
        b = (y - (a*x)) / n
        
        for j in range(7):
            j += 1
            y = int((a*(n+j)) + b)
            puntosTotales[str(i)].append({
                'puntaje': y,
                'fecha-hora': '+'+str(j)+' dia',
                'orden': n+j
            })

    datos['1']['puntajes'] = puntosTotales['1']
    datos['2']['puntajes'] = puntosTotales['2']
    datos['3']['puntajes'] = puntosTotales['3']

    #Retornar JSON con el analisis de los datos
    return datos

@route('/recoleccion/api-webScraping')
@enable_cors
def data_mine():
    response.headers['Content-type'] = 'application/json'

    #Peticiones a API y Web Scraping
    datosTwitter = apiTwitter()
    datosFacebook = webScrapingFacebook()

    """ datosTwitter = [['1', str(random.randint(7494, 8494)), str(random.randint(350, 500)), 'Nuestro propósito es mejorar la calidad de vida de los Morelianos, pero sobre todo de quienes más lo necesitan, por… https://t.co/BbfAzvvjFJ'], ['2', str(random.randint(3809, 4709)), str(random.randint(313, 513)), 'Los michoacanos somos gente trabajadora que alza la voz para defender lo suyo. Reconozco a los trabajadores del est… https://t.co/YNDxFwF84F'], ['3', str(random.randint(215, 815)), str(random.randint(50, 250)), 'Estuve en entrevista en el programa "Elecciones Michoacán 2021" en @candelamorelia  con Aned Ayala y Ariel Ramírez.… https://t.co/UWqQiCOFlh']]
    datosFacebook = [['1', str(random.randint(41114, 50114)), str(random.randint(45496, 55496))], ['2', str(random.randint(121000, 123000)), str(random.randint(141000, 143000))], ['3', str(random.randint(3067, 3567)), str(random.randint(2567, 4160))]] """
    
    #Almacenar los datos en la base de datos
    datos = almacenarAPIWS(datosTwitter, datosFacebook)

    #Analizar el puntaje total de los candidatos
    totales = [0 ,0 ,0] 
    for i in range(3):
        totales[i] = int(datos['api'][i]['seguidores']) + int(datos['api'][i]['favoritos']) + int(datos['webScraping'][i]['likes']) + int(datos['webScraping'][i]['seguidores']) 
    datos = almacenarPuntajesTotales(totales, datos)

    #Optener informacion de los candidatos
    datos['candidatos'] = getCandidatos()

    #Quitar _id
    for ele in datos['api']:
        ele['_id'] = ''
    for ele in datos['webScraping']:
        ele['_id'] = ''
    for ele in datos['puntajesTotales']:
        ele['_id'] = ''
    
    #Retornar JSON con los datos extraidos
    return datos
#-----------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()