import networkx as nx
import collections as col
import numpy as np
import scipy.cluster.hierarchy as hier
import matplotlib.pyplot as plt


def make_undirected(f_in, f_out):
    graph = nx.read_pajek(f_in)
    nx.write_pajek(graph.to_undirected(), f_out)


def read_graph(f_in):
    multigraph = nx.read_pajek(f_in)
    graph = nx.Graph(multigraph)
    return graph


def strong_components(graph):
    result = nx.connected_component_subgraphs(graph)

    gmax = nx.Graph()
    i = 0
    for subgraph in result:
        i += 1
        if subgraph.size() > gmax.size():
            gmax = subgraph

    print('Stronly connected components %d' % i)
    print('Biggest component nodes: %d' % len(gmax))
    print('Biggest component edges: %d' % gmax.size())

    nx.write_pajek(gmax, 'data/biggest_component.net')


def eigenvector(graph, list_size):
    nodes = nx.eigenvector_centrality(graph)
    max_list = sorted(nodes, key=nodes.__getitem__, reverse=True)
    print('Eigenvector:')
    print({node: nodes[node] for node in max_list[:list_size]})


def max_cliques(graph):
    cliques = list(nx.find_cliques(graph))
    print('Number of cliques: ' + str(len(cliques)))
    print('Cliques count: ')
    print(col.Counter([len(clique) for clique in cliques]))


def clustering(graph):
    distance = nx.floyd_warshall_numpy(graph)
    upper_triangular = np.triu(distance)
    Z = hier.linkage(upper_triangular, method='single')
    plt.figure(figsize=(20, 20))
    hier.dendrogram(Z)
    plt.show()


def main():
    make_undirected('data/celegansneural.net', 'data/celegansneural_undirected.net')
    G = read_graph('data/biggest_component.net')
    strong_components(G)
    eigenvector(G, 5)
    max_cliques(G)
    clustering(G)


if __name__ == "__main__":
    main()
