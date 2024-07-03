# Importamos la API Spotipy la cual será la herramienta principal de este programa
# EXTRA: para instalar la API se usa el siguiente comando = (pip install spotipy)
# Forma Alternativa de instalacion = (py -m pip install spotipy)
# Para actualizar = (pip install spotipy --upgrade)
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Creamos la clase Artist la cual tendra el trabajo de pedirle al usuario un artista
class Artist:
    def songs():
        client_id = '2c93171bee504db4b754475a217bd842'
        client_secret = 'f7121a8bf8f9453b9a625fc13c154553'

        client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        results = sp.search(q= input('Introduzca un artista o cancion de su interes:\n'), limit=10)
        print('Aqui tienes los resultados segun tu busqueda:')
        for i, t in enumerate(results['tracks']['items']):
            print(' ', i, t['name'])