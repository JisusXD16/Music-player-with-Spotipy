# Importamos todo lo necesario
from dates.data import Artist
d = Artist

# Programa principal

def principal():
    
    while True:  
        op = input('Quieres buscar canciones?\nsi - no\n').lower()
        match op:
            case 'si':
                d.songs()
            case 'no':
                break
            case _:
                pass

if __name__ == '__main__':
    principal()