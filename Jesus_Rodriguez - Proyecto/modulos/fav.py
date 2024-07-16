# Importamos json
from pathlib import Path 
import json
from modulos import gui
# en fav se guardaran las canciones que el usuario indique como favoritas
fav = []

# Esta funcion se encargará de comparar las canciones de la lista con la cancion que introdujo el usuario
# En lSong se encuentra la lista con todas las canciones segun la busqueda del usuario
# Y en song se encuentra la cancion que el usuario escogio 
def favList(lSong, song):
    try:
        with open('recursos/favs_songs.json', 'r') as arch:
            content = arch.read()                           #  nos aseguramos que el archivo exista y no tenga algun error
            if content:
                fav = json.loads(content)
            else:
                fav = []
    except FileNotFoundError:
        fav = []
    except json.JSONDecodeError:
        fav = []    
    if song in lSong and song not in fav:       # luego añadimos esta cancion en una lista dentro del archivo "favs_songs.json" donde se encuentran las canciones favoritas
        fav.append(song)                    
        with open('recursos/favs_songs.json', 'w') as archivo:
            json.dump(fav, archivo)
        gui.listasFav(fav)