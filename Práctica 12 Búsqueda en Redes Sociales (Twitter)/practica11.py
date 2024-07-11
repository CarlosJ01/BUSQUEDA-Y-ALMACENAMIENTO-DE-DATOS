#Libreria para la API de Twitter
#pip install tweepy

import tweepy
import json


#autenticación poner sus propias claves :)
consumer_key=""
consumer_secret=""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,
 wait_on_rate_limit_notify=True)

try:
    #Periciones
    London_woeid = 44418
    Mexico_woeid = 116545
    Morelia_woeid = 134091
    Medellin_woeid = 368150
    Rio_woeid = 455825
    Paris_woeid = 615702
    trends_result = api.trends_place(London_woeid)
    trends_mexico = api.trends_place(Mexico_woeid)
    trends_morelia = api.trends_place(Morelia_woeid)
    trends_medellin = api.trends_place(Medellin_woeid)
    trends_rio = api.trends_place(Rio_woeid)
    trends_paris = api.trends_place(Paris_woeid)
    #Inglaterra
    print("---------------------------------------------")
    print("Trending topics de Londres, Inglaterra")
    for trend in trends_result[0]["trends"][:10]:
        print(trend["name"])
    print("---------------------------------------------")
    #México
    print("Trending topics de CDMX, México")
    for trend in trends_mexico[0]["trends"][:10]:
        print(trend["name"])
    print("---------------------------------------------")
    #Colombia
    print("Trending topics de Medellín, Colombia")
    for trend in trends_medellin[0]["trends"][:10]:
        print(trend["name"])
    print("---------------------------------------------")
    #Brasil
    print("Trending topics de Rio de Janeiro, Brasil")
    for trend in trends_rio[0]["trends"][:10]:
        print(trend["name"])
    print("---------------------------------------------")
    #Francia
    print("Trending topics de Rio de París, Francia")
    for trend in trends_paris[0]["trends"][:10]:
        print(trend["name"])
    print("---------------------------------------------")
    #Morelia
    print("Trending topics de Morelia, México")
    for trend in trends_rio[0]["trends"][:10]:
        print(trend["name"])
    print("---------------------------------------------")
except tweepy.error.TweepError:
    print("Error")