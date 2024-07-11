#Libreria para la API de Facebook
#pip install facebook-sdk

import json
import facebook

def main():
    #Token del usuario
    token={"EAADRTYmkjv4BAFWMM4fkSFrFN7ZCWinxQ5X8XQ77cR1eU0P8y9fD7PxsRNvUUdet6ii2lpX14iePojoqhww7VhboY5EKUP0wZCzb0uft0N1hXU7EUP3HdxHo1bDzY58qpXZBYeMeKmraeAZAvZAV6EoD0BhnPal1hFhfK4vljtQ1QSZCfgBCUyAkStZB40Nj7ZAHxSfMjmzNZAqwgyeL9IapTNSn6bZCoS0z88ubEKku1GMgZDZD"}
    graph=facebook.GraphAPI(token)

    #Peticion a la API para el nombre del usuario
    fields=['name']
    profile=graph.get_object('me', fields=fields)

    print("\nNombre: "+profile["name"])

    #Peticion para extraer los amigos del usuario
    fields=['friends']
    friends=graph.get_object('me', fields=fields)

    print("Total de amigos: "+str(friends['friends']['summary']['total_count']))

    #Peticion para extraer las paguinas que le gustan al usuario
    print("Paginas que me gustan")

    fields=['likes']
    likes=graph.get_object('me', fields=fields)

    for l in likes['likes']['data']:
        print("\t"+l['name'])
    print()

if __name__=="__main__":
    main()