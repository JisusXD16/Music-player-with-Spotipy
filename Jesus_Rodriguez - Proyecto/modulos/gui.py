# Importamos bibiliotecas y clases de otros modulos
from tkinter import *
from modulos.data import Artist
from modulos.open import Player
from modulos.graphics import *
from modulos.fav import *
p = Player
a = Artist
# lista que guardara las canciones para poder comparar con las favs del usuario
lSong = []


# Configuración de la raíz (ventana principal)
root = Tk()
root.title("Spotipy")
root.geometry("800x600")
root.configure(background='#121212')
root.iconbitmap('recursos/icono.ico')
# StringVars de las variables que se utilizaran para enviar datos a la API del programa
artista = StringVar()
cancion = StringVar()


# Función de búsqueda
def busqueda():
    b()  
    # Nos aseguramos de eliminar el texto por cada vez que se use el boton buscar
    if 'texto' in globals():
        texto.delete(0, END)
    if 'textoR' in globals():
        textoR.delete(0, END)
    select = texto.curselection()
    if select:
        pass
    # Se usa *artista* para guardar la busqueda del usuario, asi mismo con un .get() pasamos esos datos a una variable la cual es *artista1*
    # y finalmente añadimos los datos de *artista1* a *ar* la cual es una string ya que para que la busqueda funcione correctamente
    # se necesita que sea una string
    ar = ''
    artista1 = artista.get()
    ar += artista1
    a.songs(ar)

# esta funcion simplemente se utiliza para llamar a otra y enviar datos
def q():
    seleccion = textoR.curselection()
    if seleccion:
        cancionS = textoR.get(seleccion)
    play_song(artista, cancionS)

# esta funcion se encarga de reproducir la cancion elegida por el usuario
def play_song(artista, cancion):
    #r()
    # aqui repetimos lo mismo de la funcion **busqueda()** convertimos Stringvars en strings
    art = ''
    art1 = artista.get()
    art += art1

    can = ''
    can = cancion
    # y finalmente llamamos a funcion play la cual envia los datos introducidos por el usuario.
    # si todo esta correcto la cancion se reproducirá desde Spotify
    p.play(art, can)

# Función para hacer las listas de canciones
def listaCanciones(lista):
    # con estos for y el insert, añadimos las lista de canciones en los 2 cuadros listBox del programa
    # para poder mostrar los resultados de la busqueda al usuario
    for s in lista:
        texto.insert(END, s)
        
    for o in lista:
        textoR.insert(END, o)
    for l in lista:
        lSong.append(l)
# Esta funcion es de la ventana reproducir del programa la cual como dice su nombre es para reproducir las canciones
def reproducir():
    # con los siguientes controles nos aseguramos que las ventanas de busqueda : "main_frame" y info : "frame_info" 
    # se cierren cuando cambiemos de ventana.
    if main_frame.winfo_ismapped():
        main_frame.pack_forget()
    if frame_info.winfo_ismapped():
        frame_info.pack_forget()
    if frame_b.winfo_ismapped():
        frame_b.pack_forget()
        
    frame_r.pack(side=LEFT, fill=BOTH, expand=True)


# con este if nos aseguramos que la caja de texto se reinicie para no mostrar la lista repetida una y otra vez
def f():
    if 'textob' in globals():
        textob.delete(0, END)
    cancionSelec = textoR.curselection()
    if cancionSelec:                          # Ademas usamos un curselection para poder elegir las cancions dentro de los listbox
        songSelec = textoR.get(cancionSelec)    # y asi mismo obtenemos las canciones
        anadir_a_fav(lSong, songSelec)

# Funcion para llamar a otra funcion con el fin de añadir canciones a favoritas
def anadir_a_fav(lSong, song):
    favList(lSong, song)

# Funcion de control de frames en la interfaz grafica
def buscar_frame():
    for w in root.winfo_children():
        if w != sidebar:
            w.pack_forget()
    main_frame.pack(side=LEFT, fill=BOTH, expand=True)


# Apartado de biblioteca
# igualmente nos aseguramos de que los otros frames se cierren para abrir un nuevo frame
def biblio():
    if 'textob' in globals():                   # nos aseguramos de que se borre el contenido del listbox para evitar que se duplique
        textob.delete(0, END)           
    if main_frame.winfo_ismapped():
        main_frame.pack_forget()                   # y tambien aseguramos que se cierren las ventanas ya abiertas
    if frame_r.winfo_ismapped():
        frame_r.pack_forget()
    if frame_info.winfo_ismapped():
        frame_info.pack_forget()
    try:
        with open('recursos/favs_songs.json', 'r') as arch:     # abrimos el json desde esta funcion para asegurar que la lista de favoritos se muestre siempre
            content = arch.read()
            if content:
                fav = json.loads(content)
            else:
                fav = []
    except FileNotFoundError:               # hacemos controles de errores 
        fav = []
    except json.JSONDecodeError:
        fav = []  
    listasFav(fav)                      
    frame_b.pack(side=LEFT, fill=BOTH, expand=True)

#Esta funcion insterta las canciones favoritas en la listBox de la biblioteca
def listasFav(fav):
    for x in fav:
        textob.insert(END, x)

#def delet():
  #  eliminarfav(lSong, cancion)


# Funcion de info la cual muestra la ventana de informacion del programa
def info():
    # aqui igualmente nos aseguramos que otras ventanas se cierren
    if main_frame.winfo_ismapped():
        main_frame.pack_forget()
    if frame_r.winfo_ismapped():
        frame_r.pack_forget()
    if frame_b.winfo_ismapped():
        frame_b.pack_forget() 
    
    frame_info.pack(side=LEFT, fill=BOTH, expand=True)

# las funciones que no tienen mucho codigo son para solo para llamar a otra
def graphics():
    g()

# Barra de navegación lateral o "Sidebar"
sidebar = Frame(root, bg='#000000', width=250, height=600)
sidebar.pack(side=LEFT, fill=Y)

# Nombre del programa en la sidebar para darle un poco de estilo 
Label(sidebar, text='Spotipy', bg='#000000', fg='#1DB954', font=('Arial', 24)).pack(pady=20)
# Y sus ventanas para moverse por las funciones del programa
Button(sidebar, text='Buscar', bg='#000000', fg='white', font=('Arial', 18), relief=FLAT, command=buscar_frame).pack(fill=X)
Button(sidebar, text='Reproducir', bg='#000000', fg='white', font=('Arial', 18), relief=FLAT, command=reproducir).pack(fill=X)
Button(sidebar, text='Tu Biblioteca', bg='#000000', fg='white', font=('Arial', 18), relief=FLAT, command=biblio).pack(fill=X)
Button(sidebar, text='Info', bg='#000000', fg='white', font=('Arial', 18), relief=FLAT, command=info).pack(fill=X)

# Sección principal o de "busqueda"

main_frame = Frame(root, bg='#121212')
main_frame.pack(side=LEFT, fill=BOTH, expand=True)


Label(main_frame, text='Búsqueda', bg='#121212', fg='white', font=('Arial', 14)).pack(pady=10)
Entry(main_frame, justify='center', textvariable=artista, font=('Arial', 14)).pack(pady=10)

Button(main_frame, text='Buscar', command=busqueda, bg='#1DB954', fg='white', font=('Arial', 14)).pack(pady=10)     

Label(main_frame, text='Resultado de tu búsqueda', bg='#121212', fg='white', font=('Arial', 14)).pack(pady=10)
texto = Listbox(main_frame, bg='#282828', fg='white', font=('Arial', 12), selectbackground='#1DB954')
texto.pack(pady=10, fill=BOTH, expand=True)



# Seccion de Reproducir
frame_r = Frame(root, bg='#121212')
Label(frame_r, text='Introduce una cancion de la lista', bg='#121212', fg='white', font=('Arial', 14)).pack(pady=10)
Button(frame_r, text='Reproducir', bg='#1DB954', fg='white', font=('Arial', 14), command=q).pack(pady=10)
Button(frame_r, text='Añadir a Favoritos', bg='#1DB954', fg='white', font=('Arial', 14), command=f).pack(pady=10)
Label(frame_r, text='Lista de canciones', bg='#121212', fg='white', font=('Arial', 14)).pack(pady=10)
textoR = Listbox(frame_r, bg='#282828', fg='white', font=('Arial', 12), selectbackground='#1DB954')
textoR.pack(pady=10, fill=BOTH, expand=True)


# seccion de biblioteca
frame_b = Frame(root, bg='#121212')
Label(frame_b, text='Biblioteca', bg='#121212', fg='white', font=('Arial', 14)).pack(pady=10)
Label(frame_b, text='Lista de Favoritos', bg='#121212', fg='white', font=('Arial', 14)).pack(pady=10)
#Button(frame_b, text='Reproducir', bg='#1DB954', fg='white', font=('Arial', 14), command=m).pack(pady=10)
#Button(frame_b, text='Eliminar de favoritos', bg='#1DB954', fg='white', font=('Arial', 14), command=delet).pack(pady=10)
textob = Listbox(frame_b, bg='#282828', fg='white', font=('Arial', 12), selectbackground='#1DB954')
textob.pack(pady=10, fill=BOTH, expand=True)


# Seccion de Info 
frame_info = Frame(root, bg='#121212')
Label(frame_info, text='Grafica de datos', bg='#121212', fg='white', font=('Arial', 14)).pack(pady=10)
Label(frame_info, text='Busquedas y Reproducciones', bg='#121212', fg='white', font=('Arial', 14)).pack(pady=10)
Button(frame_info, text='Grafica', bg='#1DB954', fg='white', font=('Arial', 14), command=graphics).pack(pady=10)
Label(frame_info, text='Creditos: ', bg='#121212', fg='white', font=('Arial', 14)).pack(pady=10)
Label(frame_info, text='Web de Spotipy: https://spotipy.readthedocs.io/en/2.24.0/ ', bg='#121212', fg='white', font=('Arial', 14)).pack(pady=10)
Label(frame_info, text='GitHub de Spotipy: https://github.com/spotipy-dev/spotipy ', bg='#121212', fg='white', font=('Arial', 14)).pack(pady=10)
Label(frame_info, text='INFO: ', bg='#121212', fg='white', font=('Arial', 14)).pack(pady=10)
Label(frame_info, text='Es necesario que Spotifty esté instalado en el equipo', bg='#121212', fg='white', font=('Arial', 14)).pack(pady=10)
Label(frame_info, text='Mas informacion en el archivo "readme.ipynb" ', bg='#121212', fg='white', font=('Arial', 14)).pack(pady=10)
Label(frame_info, text='Realizado por: ', bg='#121212', fg='white', font=('Arial', 14)).pack(pady=10)
Label(frame_info, text='Jesus Rodriguez', bg='#121212', fg='white', font=('Arial', 14)).pack(pady=10)

# Bucle de la aplicación
root.mainloop()