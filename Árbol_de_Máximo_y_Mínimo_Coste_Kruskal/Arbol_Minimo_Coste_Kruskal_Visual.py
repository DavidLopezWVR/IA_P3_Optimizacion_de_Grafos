import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib.animation as animation

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal(n, edges, uf, G, ax, pos, edge_labels):
    mst = []
    edges = sorted(edges)
    edge_artists = []
    
    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            edge = (u, v)
            edge_artists.append(edge)
            
            # Animate adding the edge to the graph
            nx.draw_networkx_edges(G, pos, edgelist=edge_artists, width=2, edge_color="red", ax=ax)
            nx.draw_networkx_labels(G, pos, ax=ax)
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
            plt.draw()
            plt.pause(0.5)  # Pause to create animation effect

    return mst

# Example graph represented by a list of edges (weight, node1, node2)
edges = [
    (1, 0, 1), 
    (4, 0, 2),
    (3, 1, 2),
    (2, 1, 3),
    (5, 2, 3)
]

n = 4  # Number of nodes (0 to 3)

# Create a graph object
G = nx.Graph()
for weight, u, v in edges:
    G.add_edge(u, v, weight=weight)

# Create a UnionFind object
uf = UnionFind(n)

# Define positions for nodes (static)
pos = nx.spring_layout(G, seed=42)

# Get edge labels (weights)
edge_labels = nx.get_edge_attributes(G, 'weight')

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Árbol de Expansión Mínima - Kruskal", fontsize=15)
ax.axis("off")  # Hide axes

# Draw the initial graph
nx.draw_networkx_nodes(G, pos, ax=ax)
nx.draw_networkx_labels(G, pos, ax=ax)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

# Run Kruskal's algorithm and animate the process
kruskal(n, edges, uf, G, ax, pos, edge_labels)

# Show the plot with animation
plt.show()
