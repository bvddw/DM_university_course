import networkx as nx
import matplotlib.pyplot as plt


def graph_building(set_of_items: tuple, rel: tuple):
    G = nx.DiGraph()
    for pair in rel:
        a, b = pair
        if a not in G.nodes:
            G.add_node(a)
        if b not in G.nodes:
            G.add_node(b)
        G.add_edge(b, a)
        
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=12, font_color='black', arrowsize=20)
    plt.show()


# Test Case 1
set_of_items_1 = ('a', 'b', 'c', 'd', 'e')
relation_1 = (('a', 'b'), ('b', 'd'), ('d', 'c'), ('c', 'e'), ('d', 'e'))
# This relation is reflexive, symmetric, and transitive.
graph_building(set_of_items_1, relation_1)
