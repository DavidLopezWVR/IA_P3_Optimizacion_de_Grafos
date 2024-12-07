import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib.animation as animation

class UnionFind:
    def __init__(self, n):
        # Inicializa los padres y el tamaño de cada conjunto
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        # Encuentra la raíz del conjunto que contiene el nodo u
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Compresión de camino
        return self.parent[u]

    def union(self, u, v):
        # Une los conjuntos que contienen u y v
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # Unión por rango (para mantener el árbol equilibrado)
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal_max(n, edges, uf, G, ax, pos, edge_labels):
    # edges: lista de aristas (peso, nodo1, nodo2)
    # n: número de nodos en el grafo
    mst = []  # Árbol de expansión máxima (AEMax)
    edge_artists = []  # Lista para las aristas del AEMax
    
    # Ordena las aristas por peso en orden descendente
    edges.sort(reverse=True, key=lambda x: x[0])
    
    for weight, u, v in edges:
        # Si los nodos u y v no están conectados, los unimos
        if uf.union(u, v):
            mst.append((u, v, weight))
            edge = (u, v)
            edge_artists.append(edge)
            
            # Animación: agregar la arista al grafo
            nx.draw_networkx_edges(G, pos, edgelist=edge_artists, width=2, edge_color="red", ax=ax)
            nx.draw_networkx_labels(G, pos, ax=ax)
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
            plt.draw()  # Redibuja la figura
            plt.pause(0.5)  # Pausa para animar el proceso (0.5 segundos)
    
    return mst

# Ejemplo de grafo representado por una lista de aristas
# (peso, nodo1, nodo2)
edges = [
    (1, 0, 1), 
    (4, 0, 2),
    (3, 1, 2),
    (2, 1, 3),
    (5, 2, 3)
]

n = 4  # Número de nodos (0 a 3)

# Crear el objeto grafo de NetworkX
G = nx.Graph()
for weight, u, v in edges:
    G.add_edge(u, v, weight=weight)

# Crear un objeto UnionFind para gestionar los conjuntos disjuntos
uf = UnionFind(n)

# Definir las posiciones de los nodos (con un layout estético)
pos = nx.spring_layout(G, seed=42)

# Obtener las etiquetas de las aristas (pesos)
edge_labels = nx.get_edge_attributes(G, 'weight')

# Configurar la visualización con Matplotlib
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Árbol de Expansión Máxima - Kruskal", fontsize=15)
ax.axis("off")  # Desactivar los ejes para una visualización más limpia

# Dibujar el grafo inicial (sin aristas seleccionadas)
nx.draw_networkx_nodes(G, pos, ax=ax)
nx.draw_networkx_labels(G, pos, ax=ax)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

# Ejecutar el algoritmo de Kruskal y animar el proceso
kruskal_max(n, edges, uf, G, ax, pos, edge_labels)

# Mostrar la visualización con la animación
plt.show()
