#API de Twitter => pip install tweepy
import tweepy
import json

def apiTwitter():
    print('Accediendo a la api de Twitter . . .')
    #autenticación poner sus propias claves :)
    consumer_key="oU3eRnB0ENoGq124quINXdrAZ"
    consumer_secret="2QMnOEuGbG6EUXccaOndksaTvT4LAmrKJ838bb2IuCZASonxCg"
    access_token = "418197577-pXUdPpPC6NJDbmaAgQSpNRkvEMSt1xep5foYjBqk"
    access_token_secret = "JxArOpeZg8B29dRsdnRGSQYWOtC1xeWe1DbrZULFNA6s0"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

    data = api.get_user("CarlosHerreraSi")
    dataRM = api.get_user("raulmoronO")
    dataJM = api.get_user("Magana_DeLaMora")
    Candidatos = []
    
    #print(json.dumps(data._json, indent=2))
    #Carlos Herrera
    print('\tCarlos Herrera . . .')
    CarlosHerrera = []
    followers = str(data.followers_count)
    noFavoritos = str(data.favourites_count)
    uTweet = str(data.status.text)
    CarlosHerrera.append("2")
    CarlosHerrera.append(followers)
    CarlosHerrera.append(noFavoritos)
    CarlosHerrera.append(uTweet)

    #Raúl Morón Orozco
    print('\tRaúl Morón Orozco . . .')
    RaulMoron = []
    RMfollowers = str(dataRM.followers_count)
    RMnoFavoritos = str(dataRM.favourites_count)
    RMuTweet = str(dataRM.status.text)
    RaulMoron.append("1")
    RaulMoron.append(RMfollowers)
    RaulMoron.append(RMnoFavoritos)
    RaulMoron.append(RMuTweet)

    #Juan Antonio Magaña de la Mora
    print('\tJuan Antonio Magaña de la Mora . . .')
    JuanMagania = []
    JMfollowers = str(dataJM.followers_count)
    JMnoFavoritos = str(dataJM.favourites_count)
    JMuTweet = str(dataJM.status.text)
    JuanMagania.append("3")
    JuanMagania.append(JMfollowers)
    JuanMagania.append(JMnoFavoritos)
    JuanMagania.append(JMuTweet)

    print('\tAnalizando datos . . .')
    Candidatos.append(RaulMoron)
    Candidatos.append(CarlosHerrera)
    Candidatos.append(JuanMagania)
    
    return Candidatos
