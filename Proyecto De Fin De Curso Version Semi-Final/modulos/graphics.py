import plotly.express as px
busquedas = 0
reproducciones = 0

def b():
    global busquedas
    busquedas += 1
    #print(busquedas)
def r():
    global reproducciones
    reproducciones += 1
    #print(reproducciones)

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