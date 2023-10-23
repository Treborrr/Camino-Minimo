# Problema del Camino Mínimo en Python

Este es un programa en Python que utiliza la biblioteca `Tkinter` para crear una interfaz gráfica de usuario (GUI) que resuelve el Problema del Camino Mínimo en un grafo. El programa permite al usuario ingresar una matriz de adyacencia o generar una matriz aleatoria y luego calcular el camino mínimo entre dos nodos del grafo.

## Requisitos

Para ejecutar este programa, necesitas tener Python instalado en tu sistema. Además, las siguientes bibliotecas de Python deben estar instaladas:

- `Tkinter` para la creación de la interfaz de usuario.
- `networkx` para trabajar con grafos y cálculos de caminos mínimos.
- `matplotlib` para mostrar el grafo de manera gráfica.

Puedes instalar estas bibliotecas utilizando `pip`:

```bash
pip install tkinter
pip install networkx
pip install matplotlib
```
# Problema Propuesto 

Dado 𝑛 ∈ [5, 15] ingresado por el usuario, el programa debe generaraleatoriamente una matriz simétrica 𝑛 × 𝑛 (con elementos positivos) o solicitar el ingreso de cada elemento de la matriz (según decisión delusuario). Además, debe mostrar el grafo etiquetado asociado a esta matrizy el camino mínimo que existe entre dos vértices seleccionados por elusuario.


## Ejecución

Para ejecutar el programa, simplemente ejecuta el archivo `caminoMinimo.py`. Aparecerá una ventana de la interfaz de usuario con las siguientes opciones:

- **Ingresar Matriz Manualmente**: Permite al usuario ingresar manualmente los valores de la matriz de adyacencia del grafo. Se proporciona una forma sencilla de ingresar valores simétricos.

- **Generar Matriz Aleatoriamente**: Crea una matriz de adyacencia aleatoria con valores de peso limitados a un máximo de 30. La densidad de las conexiones aleatorias se puede ajustar.

El programa mostrará el grafo generado y, después de cerrar la ventana del grafo, permitirá al usuario ingresar nodos de origen y destino para calcular el camino mínimo. Los resultados se mostrarán en la ventana inicial.

## Autor

Este programa fue desarrollado por [Treborrr](https://github.com/Treborrr)

