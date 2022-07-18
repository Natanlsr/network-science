import networkx as nx
from matplotlib import pyplot as plt


def format_value(value):
    return round(value, 3)


def count_float_value(value, values):
    limited_value = format_value(value)
    count = 0
    for value_in_list in values:
        limited_value_in_list = format_value(value_in_list)
        if limited_value == limited_value_in_list:
            count += 1
    return count


def get_frequencies(values):
    frequencies = {}
    total = len(values)
    values_float = [float(x) for x in list(values.values())]
    for value in values_float:
        count = format_value(count_float_value(value, values_float) / total)
        if count != 0.000:
            frequencies[format_value(value)] = count
    return frequencies


def plot_histogram(values):
    # plt.figure(figsize=(12, 8))
    # plt.bar(*zip(*values.items()))
    # plt.hist(values, density=True, bins=80)
    # plt.ylabel('Y')
    # plt.xlabel('X')
    print(values)
    plt.bar((list(values.keys())), list(values.values()), align='center')
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
            plot_histogram(get_frequencies(betweenness_centrality))
            plot_histogram(get_frequencies(eigenvector_centrality))

        # print("Degree Assortativity Coefficient from network", graph_name, ": ",
        #       nx.degree_assortativity_coefficient(graph))
        # print("Degree Pearson Correlation Coefficient", graph_name, ": ",
        #       nx.degree_pearson_correlation_coefficient(graph))
        # print("-----------------------------------------------------------------")
        # print()

        # plot_degree_dist(graph, graph_name)


if __name__ == '__main__':
    main()
