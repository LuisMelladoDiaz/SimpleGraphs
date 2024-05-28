import csv
import networkx as nx
import matplotlib.pyplot as plt

def load_graph_from_csv(filename):
    G = nx.DiGraph()
    node_colors = {}
    
    with open(f'graphs\{filename}.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        nodes_section = True
        
        for row in reader:
            if row[0] == 'NODE':
                _, name, color = row
                G.add_node(name)
                node_colors[name] = color

            elif row[0] == 'EDGE':
                _, origin, target, direction, weight = row
                weight = float(weight)
                G = add_directed_edge(G, origin, target, direction, weight)

    return G, node_colors

def add_directed_edge(G, origin, target, direction, weight):
    if direction == 'to_origin':
        G.add_edge(target, origin, weight=weight)
    elif direction == 'to_destination':
        G.add_edge(origin, target, weight=weight)
    else:
        G.add_edge(origin, target, weight=weight)
        G.add_edge(target, origin, weight=weight)
    return G

def draw_graph(filename, path=None):
    G, node_colors = load_graph_from_csv(filename)

    pos = nx.spring_layout(G)
    node_color_values = [node_colors[node] for node in G.nodes()]

    nx.draw(G, pos, with_labels=True, node_color=node_color_values, edge_color='gray', node_size=2000, font_size=20, font_color='black', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})

    if path != None:
        path_edges = list(zip(path, path[1:]))
        print(path_edges)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=1)

    plt.show()