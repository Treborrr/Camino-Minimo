import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
import networkx as nx
import random
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

# Ventana principal
app = tk.Tk()
app.title("Problema del Camino Mínimo")

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
                else:
                    matriz[i][j] = matriz[j][i]
    
    mostrar_grafo(matriz)

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

def mostrar_grafo(matriz):
    G = nx.Graph()
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            if matriz[i][j] > 0:
                G.add_edge(i, j, weight=matriz[i][j])

    # Mostrar el grafo de manera gráfica
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

# Botones para generar matriz
generar_manual_button = tk.Button(app, text="Ingresar Matriz Manualmente", command=generar_matriz_manual)
generar_manual_button.pack()

generar_aleatorio_button = tk.Button(app, text="Generar Matriz Aleatoriamente", command=generar_matriz_aleatoria)
generar_aleatorio_button.pack()

# Etiquetas para mostrar resultados
camino_minimo_label = tk.Label(app, text="")
camino_minimo_label.pack()

longitud_camino_label = tk.Label(app, text="")
longitud_camino_label.pack()

app.mainloop()

