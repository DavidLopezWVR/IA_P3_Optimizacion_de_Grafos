from heapq import heappop, heappush, heapify
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import time

# El grafo original
graph = {
    "A": {"B": 3, "C": 3},
    "B": {"A": 3, "D": 3.5, "E": 2.8},
    "C": {"A": 3, "E": 2.8, "F": 3.5},
    "D": {"B": 3.5, "E": 3.1, "G": 10},
    "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
    "F": {"G": 2.5, "C": 3.5},
    "G": {"F": 2.5, "E": 7, "D": 10},
}

# Crear un grafo dirigido usando NetworkX
G = nx.Graph(graph)

# Posiciones de los nodos
positions = {
    "A": (100, 50),
    "B": (50, 200),
    "C": (200, 50),
    "D": (50, 350),
    "E": (150, 200),
    "F": (250, 50),
    "G": (250, 350),
}

# Inicializar la figura y los ejes para la visualización
plt.figure(figsize=(8, 6))

# Función para dibujar el grafo con animaciones
def draw_graph(G, path=None, visited=None, edges_color='grey'):
    # Dibujar los nodos
    node_colors = ['green' if node in visited else 'blue' for node in G.nodes]
    nx.draw_networkx_nodes(G, positions, node_size=700, node_color=node_colors)

    # Dibujar las aristas
    nx.draw_networkx_edges(G, positions, width=2, edge_color=edges_color)
    
    # Dibujar las etiquetas de los nodos
    nx.draw_networkx_labels(G, positions, font_size=16, font_weight='bold', font_color='white')

    # Dibujar las etiquetas de las aristas (pesos)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, positions, edge_labels=edge_labels)

    # Resaltar el camino más corto
    if path:
        edges_in_path = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, positions, edgelist=edges_in_path, width=3, edge_color='yellow')

    # Mostrar el gráfico
    plt.axis('off')
    plt.show()

# Algoritmo de Dijkstra con animación
def dijkstra(graph, source, target):
    distances = {node: float("inf") for node in graph}
    distances[source] = 0
    pq = [(0, source)]
    visited = set()
    predecessors = {node: None for node in graph}

    while pq:
        current_distance, current_node = heappop(pq)
        if current_node in visited:
            continue

        visited.add(current_node)
        draw_graph(G, visited=visited, edges_color='red')  # Actualizar la visualización
        time.sleep(0.5)

        for neighbor, weight in graph[current_node].items():
            tentative_distance = current_distance + weight
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                predecessors[neighbor] = current_node
                heappush(pq, (tentative_distance, neighbor))
        
        # Actualizar la visualización
        draw_graph(G, visited=visited, edges_color='grey')
        time.sleep(0.5)

    # Reconstruir el camino más corto
    path = []
    while target:
        path.append(target)
        target = predecessors[target]
    path.reverse()

    # Resaltar el camino más corto
    draw_graph(G, path=path, visited=visited, edges_color='grey')
    time.sleep(0.5)
    
    return path, distances[path[-1]]

# Ejecutar el algoritmo
path, distance = dijkstra(graph, "B", "F")
print(f"Camino más corto: {path}")
print(f"Distancia más corta: {distance}")