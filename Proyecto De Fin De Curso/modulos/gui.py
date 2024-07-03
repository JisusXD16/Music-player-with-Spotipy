from tkinter import *
from modulos.data import Artist

a = Artist


    # configuracion de la raiz (ventana principal)
root = Tk()
root.configure(background='Green')

artista = StringVar()
def busqueda():
    texto.delete(1.0, END)
    ar = ' '
    # Variables de texto
    artista1 = StringVar()
    artista1.set(artista.get())
    ar += artista1.get()
    a.songs(ar)


def listaCanciones(lista):
    for s in lista:
         texto.insert(END, s + "\n", "blanco")

#def enumerar(lista):
    #for n, q in enumerate(lista):
            #print(n, q)
    


    # Creamos campos para texto
Label(root, text='Busqueda').pack()
Entry(root, justify='center', textvariable=artista).pack()

#Entry(root, justify='center', textvariable=artista, state='disabled').pack()
 
 # Boton
Button(root, text='Buscar', command= busqueda).pack()

# caja de texto
Label(root, text='Resultado de tu busqueda').pack()
texto = Text(root)
texto.configure(background='Black')
texto.pack()
texto.tag_configure("blanco", foreground="white")




#texto.pack(textvariable=)

    # bucle de la aplicacion
root.mainloop()