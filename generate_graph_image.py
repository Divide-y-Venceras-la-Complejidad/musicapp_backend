import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from music_algorithm import bfs_first_height_max_heap

def draw_graph(G, connected_nodes, weighted=False):
    # Crear un objeto de grafo de NetworkX
    graph = nx.Graph()

    # Agregar nodos al grafo
    for node in connected_nodes:
        graph.add_node(node)

    # Agregar aristas al grafo
    for u in connected_nodes[1:]:
        if weighted:
            weight = G[connected_nodes[0], u]
            graph.add_edge(connected_nodes[0], u, weight=weight)
        else:
            graph.add_edge(connected_nodes[0], u)

    return graph

 