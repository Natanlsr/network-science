import networkx as nx
import numpy as np
from matplotlib import pyplot as plt


def plot_histogram(dict_values, graph_name):
    np_values = np.array(list(dict_values.values()))

    # Creating histogram
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.hist(np_values, bins="sqrt")

    # Show plot
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title(graph_name)
    plt.show()


def read_graph_from_file_and_add_nodes(file_name, graph):
    with open(file_name) as f:
        for line in f:
            number_1, number_2 = line.replace('\n', "").split("\t")
            i = int(number_1)
            j = int(number_2)
            graph.add_edge(i, j)


def main():
    graphs_names = ["internet", "collaboration", "protein", "email",
                    "metabolic", "phonecalls", "powergrid", "www", "citation", "actor"]
    selected_networks = ["protein", "powergrid"]

    for graph_name in graphs_names:
        graph = nx.Graph()
        read_graph_from_file_and_add_nodes("./resources/" + graph_name + ".edgelist.txt", graph)

        print("Number of nodes from network", graph_name, ": ", graph.number_of_nodes())

        if graph_name in selected_networks:
            # shortest_paths = nx.shortest_path(graph)
            betweenness_centrality = nx.betweenness_centrality(graph)
            eigenvector_centrality = nx.eigenvector_centrality(graph)
            # print(shortest_paths)
            plot_histogram(betweenness_centrality, "Betweenness Centrality: " + graph_name)
            plot_histogram(eigenvector_centrality, "Eigenvector Centrality: " + graph_name)

        print("Degree Assortativity Coefficient from network", graph_name, ": ",
              nx.degree_assortativity_coefficient(graph))
        print("Degree Pearson Correlation Coefficient", graph_name, ": ",
              nx.degree_pearson_correlation_coefficient(graph))
        print("-----------------------------------------------------------------")
        print()


if __name__ == '__main__':
    main()
