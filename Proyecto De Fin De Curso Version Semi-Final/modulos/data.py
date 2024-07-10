# Importamos la API Spotipy la cual será la herramienta principal de este programa
# EXTRA: para instalar la API se usa el siguiente comando = (pip install spotipy)
# Forma Alternativa de instalacion = (py -m pip install spotipy)
# Para actualizar = (pip install spotipy --upgrade)
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from modulos.gui import *
from modulos import gui




# Creamos la clase Artist la cual tendra el trabajo de buscar una lista de resultado segun lo que introduce el usuario

class Artist:
    def songs(ar):
        # lista para las canciones
        l = []
        # client id y client secret son dos variables que necesita la API para funcionar
        client_id = '2c93171bee504db4b754475a217bd842'
        client_secret = 'f7121a8bf8f9453b9a625fc13c154553'
        client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
        cantante = ar
        # Hacemos un control para asegurar que la variable "cantante" no este vacia
        if cantante:
        # usamos *results* para guardar los resultados de la busqueda
            results = sp.search(q=cantante, limit=30)
        else:
            # Si el usuario decide no introducir nada se le dara el valor "a" a cantante para evitar errores
            cantante = 'a'
            results = sp.search(q=cantante, limit=30)
        # con este for extraemos los datos necesarios de los resultados de la busqueda
        for i, t in enumerate(results['tracks']['items']):   
        # y finalmente con el append insertamos los nombres de las canciones en la lista **l**
            l.append(t['name'])
          
        # llamamos la funcion "listaCanciones" para insertar los resultados en las cajas de texto y asi el usuario podra ver los resultados de su busqueda
        gui.listaCanciones(l)         