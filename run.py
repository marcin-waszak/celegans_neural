import networkx as nx

# convert digraph to graph
G = nx.read_pajek("data/celegansneural.net")
nx.write_pajek(G.to_undirected(), "data/celegansneural_undirected_unstripped.net")

# strip
with open('data/celegansneural_undirected_unstripped.net', 'r') as src,\
     open('data/celegansneural_undirected.net', 'w') as dst:
    dst.writelines(line.replace(' 0.0 0.0 ellipse', '').replace(' 1.0', '') for line in src)
