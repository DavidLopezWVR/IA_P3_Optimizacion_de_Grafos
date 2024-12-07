from heapq import heapify, heappop, heappush

class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph

    def shortest_distances(self, source: str):
        # Inicializar las distancias de todos los nodos a infinito
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0  # La distancia al nodo fuente es 0

        # Inicializar la cola de prioridad
        pq = [(0, source)]  # (distancia acumulada, nodo)
        heapify(pq)

        # Inicializar el diccionario de predecesores para reconstruir caminos
        predecessors = {node: None for node in self.graph}

        visited = set()  # Conjunto de nodos visitados

        while pq:
            current_distance, current_node = heappop(pq)

            # Si ya visitamos el nodo, continuamos
            if current_node in visited:
                continue

            visited.add(current_node)  # Marcamos el nodo como visitado

            # Actualizamos las distancias de los vecinos
            for neighbor, weight in self.graph[current_node].items():
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    predecessors[neighbor] = current_node
                    heappush(pq, (tentative_distance, neighbor))

        return distances, predecessors

    def shortest_path(self, source: str, target: str):
        # Obtener las distancias y predecesores
        distances, predecessors = self.shortest_distances(source)

        # Reconstruir el camino más corto
        path = []
        current_node = target

        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]

        path.reverse()  # Invertimos el camino para obtenerlo en orden
        return path, distances[target]

# Definimos el grafo como un diccionario de adyacencia
graph = {
    "A": {"B": 3, "C": 3},
    "B": {"A": 3, "D": 3.5, "E": 2.8},
    "C": {"A": 3, "E": 2.8, "F": 3.5},
    "D": {"B": 3.5, "E": 3.1, "G": 10},
    "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
    "F": {"G": 2.5, "C": 3.5},
    "G": {"F": 2.5, "E": 7, "D": 10},
}

# Creamos una instancia del grafo
G = Graph(graph)

# Encontrar el camino más corto de B a F
path, distance = G.shortest_path("B", "F")

print(f"El camino más corto de B a F es: {path}")
print(f"La distancia más corta de B a F es: {distance}")

