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
            # Unión por rango
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal_max(n, edges):
    # edges: lista de aristas (peso, nodo1, nodo2)
    # n: número de nodos en el grafo
    uf = UnionFind(n)
    mst = []  # Árbol de expansión máxima (AEMax)
    
    # Ordena las aristas por peso en orden descendente
    edges.sort(reverse=True, key=lambda x: x[0])
    
    for weight, u, v in edges:
        # Si los nodos u y v no están conectados, los unimos
        if uf.union(u, v):
            mst.append((u, v, weight))  # Añadimos la arista al AEMax
    
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

# Ejecutamos el algoritmo de Kruskal para el árbol de expansión máxima
mst_max = kruskal_max(n, edges)

# Mostramos el resultado
print("Árbol de Expansión Máxima (AEMax):")
for u, v, weight in mst_max:
    print(f"Arista: ({u}, {v}), Peso: {weight}")
