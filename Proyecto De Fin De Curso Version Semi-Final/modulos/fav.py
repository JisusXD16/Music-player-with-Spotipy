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
    for i in lSong:
        if song != '':
            pass
        else:
            break
        if song == i:
            if song not in fav:
                fav.append(song)
                with open('recursos/favs_songs.json', 'w') as archivo:
                    json.dump(fav, archivo)
                    gui.listasFav(fav)