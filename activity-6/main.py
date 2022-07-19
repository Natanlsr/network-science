import networkx as nx
import networkx.algorithms.community as nxcom
from matplotlib import pyplot as plt


def set_node_community(G, communities):
    """Add community to node attributes"""
    for c, v_c in enumerate(communities):
        for v in v_c:
            # Add 1 to save 0 for external edges
            G.nodes[v]['community'] = c + 1


def set_edge_community(G):
    """Find internal edges and add their community to their attributes"""
    for v, w, in G.edges:
        if G.nodes[v]['community'] == G.nodes[w]['community']:
            # Internal edge, mark with community
            G.edges[v, w]['community'] = G.nodes[v]['community']
        else:
            # External edge, mark as 0
            G.edges[v, w]['community'] = 0


def get_color(i, r_off=1, g_off=1, b_off=1):
    """Assign a color to a vertex."""
    r0, g0, b0 = 0, 0, 0
    n = 16
    low, high = 0.1, 0.9
    span = high - low
    r = low + span * (((i + r_off) * 3) % n) / (n - 1)
    g = low + span * (((i + g_off) * 5) % n) / (n - 1)
    b = low + span * (((i + b_off) * 7) % n) / (n - 1)
    return r, g, b


def read_graph_from_file_and_add_nodes(file_name, graph):
    with open(file_name) as f:
        for line in f:
            number_1, number_2 = line.replace('\n', "").split("\t")
            i = int(number_1)
            j = int(number_2)
            graph.add_edge(i, j)


def greedy_modularity_communities(graph):
    plt.rcParams.update(plt.rcParamsDefault)
    plt.rcParams.update({'figure.figsize': (15, 10)})
    plt.style.use('dark_background')
    communities = sorted(nxcom.greedy_modularity_communities(graph), key=len, reverse=True)
    # Set node and edge communities
    set_node_community(graph, communities)
    set_edge_community(graph)
    node_color = [get_color(graph.nodes[v]['community']) for v in graph.nodes]
    # Set community color for edges between members of the same community (internal) and intra-community edges (
    # external)
    external = [(v, w) for v, w in graph.edges if graph.edges[v, w]['community'] == 0]
    internal = [(v, w) for v, w in graph.edges if graph.edges[v, w]['community'] > 0]
    internal_color = ['black' for e in internal]
    node_color = [get_color(graph.nodes[v]['community']) for v in graph.nodes]
    # external edges
    pos = nx.spring_layout(graph)
    plt.rcParams.update({'figure.figsize': (15, 10)})
    # Draw external edges
    nx.draw_networkx(
        graph,
        pos=pos,
        node_size=0,
        edgelist=external,
        edge_color="silver")
    # Draw nodes and internal edges
    nx.draw_networkx(
        graph,
        pos=pos,
        node_color=node_color,
        edgelist=internal,
        edge_color=internal_color)


def greedy_modularity_communities_2(graph):
    plt.rcParams.update(plt.rcParamsDefault)
    plt.rcParams.update({'figure.figsize': (15, 10)})
    plt.style.use('dark_background')
    communities = sorted(nxcom.greedy_modularity_communities(graph), key=len, reverse=True)
    # Set node and edge communities
    set_node_community(graph, communities)
    set_edge_community(graph)
    node_color = [get_color(graph.nodes[v]['community']) for v in graph.nodes]
    # Set community color for edges between members of the same community (internal) and intra-community edges (
    # external)
    external = [(v, w) for v, w in graph.edges if graph.edges[v, w]['community'] == 0]
    internal = [(v, w) for v, w in graph.edges if graph.edges[v, w]['community'] > 0]
    internal_color = ['black' for e in internal]
    node_color = [get_color(graph.nodes[v]['community']) for v in graph.nodes]
    # external edges
    pos = nx.spring_layout(graph)
    plt.rcParams.update({'figure.figsize': (15, 10)})
    # Draw external edges
    nx.draw_networkx(
        graph,
        pos=pos,
        node_size=0,
        edgelist=external,
        edge_color="silver",
        with_labels=False)
    # Draw nodes and internal edges
    nx.draw_networkx(
        graph,
        pos=pos,
        node_color=node_color,
        edgelist=internal,
        edge_color=internal_color,
        with_labels=False)


def girvan_newman(graph):
    result = nxcom.girvan_newman(graph)
    communities = next(result)
    len(communities)
    plt.rcParams.update(plt.rcParamsDefault)
    plt.rcParams.update({'figure.figsize': (15, 10)})
    # Set node and edge communities
    set_node_community(graph, communities)
    set_edge_community(graph)
    # Set community color for nodes
    node_color = [get_color(graph.nodes[v]['community']) for v in graph.nodes]
    # Set community color for internal edges
    external = [(v, w) for v, w in graph.edges if graph.edges[v, w]['community'] == 0]
    internal = [(v, w) for v, w in graph.edges if graph.edges[v, w]['community'] > 0]
    internal_color = [get_color(graph.edges[e]['community']) for e in internal]
    karate_pos = nx.spring_layout(graph)
    # Draw external edges
    nx.draw_networkx(
        graph, pos=karate_pos, node_size=0,
        edgelist=external, edge_color="#333333", with_labels=False)
    # Draw nodes and internal edges
    nx.draw_networkx(
        graph, pos=karate_pos, node_color=node_color,
        edgelist=internal, edge_color=internal_color, with_labels=False)


def main():
    graphs_names = ["protein", "powergrid"]

    for graph_name in graphs_names:
        graph = nx.Graph()
        read_graph_from_file_and_add_nodes("./resources/" + graph_name + ".edgelist.txt", graph)

        print("Number of nodes from network", graph_name, ": ", graph.number_of_nodes())

        greedy_modularity_communities(graph)
        greedy_modularity_communities_2(graph)
        girvan_newman(graph)


if __name__ == '__main__':
    main()
