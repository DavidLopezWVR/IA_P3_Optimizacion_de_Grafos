import matplotlib.pyplot as plt
import networkx as nx
import heapq
import time

def prim(grafo, inicio):
    num_vertices = len(grafo)
    
    # Lista de distancias inicializadas a infinito, excepto el vértice de inicio
    distancias = [float('inf')] * num_vertices
    distancias[inicio] = 0
    
    # Cola de prioridad para almacenar los vértices y las distancias
    cola_prioridad = [(0, inicio)]  # (distancia, vértice)
    
    # Lista para almacenar los bordes seleccionados en el AEM
    arbol_minimo = []
    
    # Lista de vértices visitados
    visitado = [False] * num_vertices
    
    while cola_prioridad:
        # Extraemos el vértice con la menor distancia
        distancia, u = heapq.heappop(cola_prioridad)
        
        if visitado[u]:
            continue
        
        visitado[u] = True
        
        # Recorremos los vecinos del vértice u
        for v in range(num_vertices):
            if grafo[u][v] != 0 and not visitado[v]:  # Verifica si hay arista
                # Si encontramos un camino más corto
                if grafo[u][v] < distancias[v]:
                    distancias[v] = grafo[u][v]
                    heapq.heappush(cola_prioridad, (distancias[v], v))
                    arbol_minimo.append((u, v, grafo[u][v]))  # Agregar el borde al AEM
    
    return arbol_minimo

# Ejemplo de grafo representado como matriz de adyacencia
grafo = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# Crear un grafo de NetworkX
G = nx.Graph()

# Agregar nodos y aristas al grafo
for i in range(len(grafo)):
    for j in range(i+1, len(grafo)):
        if grafo[i][j] != 0:
            G.add_edge(i, j, weight=grafo[i][j])

# Ejecutar Prim con el vértice de inicio 0
arbol_minimo = prim(grafo, 0)

# Configurar la visualización
pos = nx.spring_layout(G)  # Distribución de los nodos
fig, ax = plt.subplots(figsize=(8, 6))

# Inicializar la animación
def update(frame):
    ax.clear()
    ax.set_title("Algoritmo de Prim - Paso " + str(frame))
    
    # Dibujar el grafo sin los bordes del AEM
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=500, node_color='lightblue')
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=12, font_weight='bold')
    edges_to_draw = arbol_minimo[:frame]
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=edges_to_draw, edge_color='g', width=2)
    
    # Dibujar las aristas restantes en gris
    edges_remaining = list(G.edges())[:]
    for u, v, weight in edges_to_draw:
        edges_remaining.remove((u, v))
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=edges_remaining, edge_color='gray', width=1, alpha=0.5)

# Crear la animación
from matplotlib.animation import FuncAnimation
ani = FuncAnimation(fig, update, frames=len(arbol_minimo)+1, repeat=False, interval=1000)

# Mostrar la animación
plt.show()
