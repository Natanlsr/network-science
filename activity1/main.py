from create_graph import read_undirected_graph_from_file, read_directed_graph_from_file
from graph_operations import degree_per_node, average_degree_sum, plot_degree_distribution


def main():

    # Undirected Graph
    undirected_matrix = read_undirected_graph_from_file('./resources/input.txt')
    print("UNDIRECTED GRAPH:", undirected_matrix)

    undirected_degree_array = degree_per_node(undirected_matrix)
    print("UNDIRECTED GRAPH - DEGREES:", undirected_degree_array)

    undirected_average_degree_value_sum = average_degree_sum(undirected_degree_array)
    print("UNDIRECTED GRAPH - AVERAGE DEGREE BY SUM:", undirected_average_degree_value_sum)

    plot_degree_distribution(undirected_degree_array, "undirected_graph").show()

    print("\n-------------------------------------------------\n")

    # Directed Graph
    directed_matrix = read_directed_graph_from_file('./resources/input.txt')
    print("DIRECTED GRAPH:", directed_matrix)

    directed_out_degree_array = degree_per_node(directed_matrix)
    print("DIRECTED GRAPH - OUT DEGREES:", directed_out_degree_array)

    directed_in_degree_array = degree_per_node(directed_matrix, True)
    print("DIRECTED GRAPH - IN DEGREES:", directed_in_degree_array)

    directed_average_degree_value_sum = average_degree_sum(directed_out_degree_array)
    print("DIRECTED GRAPH - AVERAGE DEGREE BY SUM:", directed_average_degree_value_sum)

    plot_degree_distribution(directed_out_degree_array, "directed_graph_out_degree").show()
    plot_degree_distribution(directed_in_degree_array, "directed_graph_in_degree").show()


if __name__ == '__main__':
    main()
