# codigo extraido de la web
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import webbrowser as web 
import pyautogui
from time import sleep

# La clase Player tendrá el trabajo de reproducir la cancion que elija el usuario de las disponibles segun su busqueda
class Player:
    def play(art, can):
        # Con los datos de las StringsVars de la gui hacemos lo mismo que en la busqueda
        
        # variables necesarias para el funcionamiento de la API
        client_id = '2c93171bee504db4b754475a217bd842'
        client_secret = 'f7121a8bf8f9453b9a625fc13c154553'
        
        while True:
            if art == '' or can == '':
                break
            else:
                author = art
                song = can
                sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
                # usamos result para buscar las canciones como en "data.py" usando la variable que guarda a nuestro artista anteriormente elegido en "Buscar"
                result = sp.search(author, limit=40)

                # Extraemos los datos de la busqueda
                for i in range(0, len(result["tracks"]["items"])):
                # creamos la variable name_song para poder reproducir la cancion mediante otra variable la cual sera "song" donde se almacena la cancion que eligio el usuario
                    name_song = result["tracks"]["items"][i]["name"]
                    
                    # Por cuestion de un error la variable que guarda al artista no puede tener el mismo valor que la variable que guarda el nombre de la cancion
                    # Ya que si sus valores son iguales el programa va a reproducir todas las canciones con ese nombre sin importar el artista entrando asi en un bucle
                    if author == song:
                        print('Introduce algo valido')
                        break
                    else:
                        pass
                    # si la cancion que introdujo el usuario está en la lista, está se reproducira en la aplicación de Spotify
                    if song == name_song:
                        web.open(result["tracks"]["items"][i]["uri"])
                        sleep(5)
                        pyautogui.press("enter")
            break