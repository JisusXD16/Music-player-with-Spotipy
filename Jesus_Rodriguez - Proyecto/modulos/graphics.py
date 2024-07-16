import plotly.express as px
busquedas = 0
reproducciones = 0

# esta funcion se llama cuando se presiona el boton buscar asi sumandole un valor, esto con el fin de mostrar en una grafica cuantas veces se realizo una busqueda

def b():
    global busquedas
    busquedas += 1
 
 # esta funcion es similar a la anterior pero esta realiza la misma accion pero con las reproducciones
def r():
    global reproducciones
    reproducciones += 1

# esta funcion es llamada por el boton de grafico para mostrar una grafica con la cantidad de busquedas y reproducciones
def g():
    bq = busquedas
    rp = reproducciones
    titulo = 'Cantidad de Busquedas y Reproducciones'
    # Crear un DataFrame con las variables
    data = {'categoria': ['busqueda', 'reproducciones'],
            'cantidad': [bq, rp]}

    # Crear la gráfica de barras
    fig = px.bar(data, x='categoria', y='cantidad', title=titulo)

    # Cambiar colores de la grafica
    fig.update_traces(marker_color='green')
    fig.update_layout(
        plot_bgcolor='black',  # Fondo del área de la gráfica
        paper_bgcolor='black',  # Fondo de la imagen completa
        font_color='white'  # Color del texto
    )

    # Mostrar la gráfica
    fig.show()