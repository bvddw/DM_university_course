import networkx as nx
import matplotlib.pyplot as plt


def graph_building(set_of_items: tuple, rel: list):
    graph = nx.DiGraph()
    # building the Hasse diagram
    for item in set_of_items:
        flag = True
        for possible_edge in set_of_items:
            if (item, possible_edge) in rel:
                for check in set_of_items:
                    if (item, check) in rel and (check, possible_edge) in rel:
                        flag = False
                        break
                if flag:
                    if item not in graph.nodes:
                        graph.add_node(item)
                    if possible_edge not in graph.nodes:
                        graph.add_node(possible_edge)
                    graph.add_edge(possible_edge, item)

    nx.draw(graph, with_labels=True, node_color='lightblue', node_size=500, font_size=12, font_color='black', arrowsize=20)
    plt.show()


# Test Case 1
set_of_items_1 = ('a', 'b', 'c', 'd', 'e')
relation_1 = [('a', 'b'), ('b', 'd'), ('d', 'c'), ('c', 'e'), ('d', 'e')]
graph_building(set_of_items_1, relation_1)

# Test Case 2
set_of_items_2 = (1, 2, 3, 5, 6, 7, 10, 14, 15, 21, 30, 35, 42, 70, 105, 210)
relation_2 = [(1, 2), (1, 3), (1, 5), (1, 6), (1, 7), (1, 10), (1, 14), (1, 15), (1, 21), (1, 30), (1, 35), (1, 42),
              (1, 70), (1, 105), (1, 210), (2, 6), (2, 10), (2, 14), (2, 30), (2, 42), (2, 70), (2, 210), (3, 6),
              (3, 15), (3, 30), (3, 42), (3, 105), (3, 210), (5, 10), (5, 15), (5, 30), (5, 35), (5, 70), (5, 105),
              (5, 210), (6, 30), (6, 42), (6, 210), (7, 14), (7, 21), (7, 35), (7, 42), (7, 70), (7, 105), (7, 210),
              (10, 30), (10, 70), (10, 210), (14, 42), (14, 70), (14, 210), (15, 30), (15, 105), (15, 210), (21, 42),
              (21, 105), (21, 210), (30, 210), (35, 70), (35, 105), (35, 210), (42, 210), (70, 210), (105, 210)]
graph_building(set_of_items_2, relation_2)
