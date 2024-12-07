import heapq

def prim(grafo, inicio):
    """
    Implementa el algoritmo de Prim para encontrar el Árbol de Expansión Mínima.
    
    :param grafo: Matriz de adyacencia del grafo.
    :param inicio: El vértice inicial desde donde comienza el algoritmo.
    :return: Lista de los bordes seleccionados en el AEM.
    """
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
# 0: sin conexión, 1, 2...: peso de la arista entre los vértices
grafo = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# Ejecutar Prim con el vértice de inicio 0
arbol_minimo = prim(grafo, 0)

# Mostrar el Árbol de Expansión Mínima
print("Arbol de Expansión Mínima (AEM):")
for u, v, peso in arbol_minimo:
    print(f"({u}, {v}) con peso {peso}")

