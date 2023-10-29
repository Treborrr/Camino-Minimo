import tkinter as tk
from tkinter import messagebox, simpledialog
import networkx as nx
import random
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

camino_minimo_label = None
longitud_camino_label = None

# Función para mostrar la ventana de información
def mostrar_informacion():
    info_window = tk.Toplevel(app)
    info_window.title("Información")
    info_text = tk.Label(info_window, text="""
    Instrucciones de Uso:

    1. Para generar una matriz manualmente:
       - Haz clic en el botón "Generar Matriz Manualmente".
       - Ingresa el valor de "n" (tamaño de la matriz) en el cuadro de diálogo.
       - Ingresa los pesos de las aristas en la matriz cuadrada.
       - El programa generará un grafo y te pedirá que ingreses un nodo de origen y un nodo de destino para encontrar el camino mínimo.

    2. Para generar una matriz aleatoriamente:
       - Haz clic en el botón "Generar Matriz Aleatoriamente".
       - Ingresa el valor de "n" (tamaño de la matriz) en el cuadro de diálogo.
       - El programa generará una matriz de adyacencia con valores aleatorios y mostrará el grafo resultante.
       - Te pedirá que ingreses un nodo de origen y un nodo de destino para encontrar el camino mínimo.

    3. Para encontrar el camino mínimo:
       - Después de generar una matriz, ingresa el nodo de origen y el nodo de destino en los cuadros de diálogo que aparezcan.
       - El programa calculará el camino mínimo y mostrará el resultado en la ventana principal.

    ¡Disfruta explorando el problema del camino mínimo!
    """)
    info_text.pack()
    retroceder_button = tk.Button(info_window, text="Retroceder", command=info_window.destroy)
    retroceder_button.pack()

# Función para mostrar la ventana principal
def mostrar_ventana_principal():
    # Limpiar la ventana
    for widget in app.winfo_children():
        widget.destroy()

    # Botones para generar matriz
    generar_manual_button = tk.Button(app, text="Generar Matriz Manualmente", command=generar_matriz_manual)
    generar_manual_button.pack(padx=10, pady=5)

    generar_aleatorio_button = tk.Button(app, text="Generar Matriz Aleatoriamente", command=generar_matriz_aleatoria)
    generar_aleatorio_button.pack(padx=10, pady=5)

    global camino_minimo_label, longitud_camino_label
    camino_minimo_label = tk.Label(app, text="")
    longitud_camino_label = tk.Label(app, text="")
    camino_minimo_label.pack()
    longitud_camino_label.pack()

# Función para generar matriz manualmente
def generar_matriz_manual():
    n = simpledialog.askinteger("Ingresar n", "Ingrese n (entre 5 y 15):", parent=app)
    
    if n is None:
        return  # El usuario canceló la operación
    
    if n < 5 or n > 15:
        messagebox.showerror("Error", "El valor de n debe estar en el rango [5, 15].")
        return

    matriz = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i, n):
            if i == j:
                matriz[i][j] = 0
            else:
                if i < j:
                    peso = simpledialog.askinteger(f"Ingrese el peso para ({i}, {j})", f"Ingrese el peso para ({i}, {j}):", parent=app)
                    matriz[i][j] = peso
                    matriz[j][i] = peso
    
    mostrar_grafo(matriz)

# Función para generar matriz aleatoria
def generar_matriz_aleatoria():
    n = simpledialog.askinteger("Ingresar n", "Ingrese n (entre 5 y 15):", parent=app)
    
    if n is None:
        return  # El usuario canceló la operación
    
    if n < 5 or n > 15:
        messagebox.showerror("Error", "El valor de n debe estar en el rango [5, 15].")
        return

    matriz = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            if i == j:
                matriz[i][j] = 0
            else:
                if random.random() < 0.3:  # Ajusta este valor para controlar la densidad
                    # Genera valores aleatorios entre 1 y 30
                    matriz[i][j] = random.randint(1, 30)
                    matriz[j][i] = matriz[i][j]
    
    mostrar_grafo(matriz)

# Función para mostrar el grafo y el camino mínimo
def mostrar_grafo(matriz):
    global camino_minimo_label, longitud_camino_label
    
    G = nx.Graph()
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            if matriz[i][j] > 0:
                G.add_edge(i, j, weight=matriz[i][j])

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    plt.show()
    
    origen = simpledialog.askinteger("Nodo de Origen", "Ingrese el nodo de origen:", parent=app)
    destino = simpledialog.askinteger("Nodo de Destino", "Ingrese el nodo de destino:", parent=app)
    
    if origen is None or destino is None:
        return  # El usuario canceló la operación
    
    try:
        camino = nx.shortest_path(G, source=origen, target=destino, weight='weight')
        longitud = nx.shortest_path_length(G, source=origen, target=destino, weight='weight')
        camino_minimo_label.config(text=f"Camino Mínimo: {camino}")
        longitud_camino_label.config(text=f"Longitud del Camino Mínimo: {longitud}")
    except nx.NetworkXNoPath:
        messagebox.showerror("Error", "No hay un camino entre los nodos de origen y destino.")

# Ventana principal
app = tk.Tk()
app.title("Problema del Camino Mínimo")
app.geometry("800x600")

# Botones en la ventana principal
iniciar_button = tk.Button(app, text="Iniciar", command=mostrar_ventana_principal)
iniciar_button.pack(padx=1, pady=4)

informacion_button = tk.Button(app, text="Información", command=mostrar_informacion)
informacion_button.pack(padx=1, pady=5)

salir_button = tk.Button(app, text="Salir", command=app.quit)
salir_button.pack(padx=6, pady=6)

app.mainloop()
