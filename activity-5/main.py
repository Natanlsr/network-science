import networkx as nx
from matplotlib import pyplot as plt
from math import e, sqrt, pi


def degree_distribution(degree_freq, number_nodes):
    degrees_distribution = [0] * len(degree_freq)

    for i in range(len(degree_freq)):
        degrees_distribution[i] = degree_freq[i] / number_nodes

    return degrees_distribution


def get_average_degree(graph):
    return 2 * graph.number_of_edges() / graph.number_of_nodes()


def get_poisson_values(k, nodes_degrees):

    qtd_values = len(nodes_degrees)
    poisson = [0] * qtd_values
    for degree in range(1, qtd_values):
        poisson[degree] = ((e ** -k) / sqrt(2*pi*degree)) * (((e * k) / degree) ** degree)

    return poisson


def plot_degree_dist(G, name):
    k = get_average_degree(G)
    degree_freq = nx.degree_histogram(G)
    degrees = range(len(degree_freq))
    degree_distribution_values = degree_distribution(degree_freq, G.number_of_edges())
    poisson_values = get_poisson_values(k, degrees)

    plt.figure(figsize=(12, 8))
    plt.loglog(degrees, degree_distribution_values, 'o', label=name)
    plt.plot(degrees, poisson_values, label="Poisson")
    plt.ylim([10**-6, 1])
    plt.legend()
    plt.xlabel('k')
    plt.ylabel('Pk')


def read_graph_from_file_and_add_nodes(file_name, graph):
    with open(file_name) as f:
        for line in f:
            number_1, number_2 = line.replace('\n', "").split("\t")
            i = int(number_1)
            j = int(number_2)
            graph.add_edge(i, j)


def main():
    graphs_names = ["internet", "collaboration", "protein", "collaboration",
                    "email", "metabolic", "phonecalls", "powergrid", "www", "citation", "actor"]
    for graph_name in graphs_names:
        graph = nx.Graph()
        read_graph_from_file_and_add_nodes("../resources/" + graph_name + ".edgelist.txt", graph)

        print("Number of nodes from network", graph_name, ": ", graph.number_of_nodes())
        print("Degree Assortativity Coefficient from network", graph_name, ": ",
              nx.degree_assortativity_coefficient(graph))
        print("Degree Pearson Correlation Coefficient", graph_name, ": ",
              nx.degree_pearson_correlation_coefficient(graph))
        print("-----------------------------------------------------------------")
        print()
        #plot_degree_dist(graph, graph_name)


if __name__ == '__main__':
    main()
