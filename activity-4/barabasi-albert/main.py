import networkx as nx
import matplotlib.pyplot as plt
import random


def plot_degree_distribution(nodes_degrees, networkx_degress):
    degrees_distribution = degree_distribution(nodes_degrees)
    degree_distribution_networkx = degree_distribution(networkx_degress)

    plt.figure(figsize=(12, 8))
    plt.xlabel('K')
    plt.ylabel('PK')
    plt.title('Degree Distribution Comparison')

    plt.loglog(
        degrees_distribution,
        'o',
        label="Barabasi generated degree distribution"
    )
    plt.loglog(
        degree_distribution_networkx,
        'o',
        label="Barabasi networkx degree distribution"
    )
    plt.ylim([10 ** -6, 1])

    plt.legend()
    plt.show()


def degree_distribution(degrees):
    degrees_distribution = [0] * (max(degrees) + 1)

    for i in range(max(degrees) + 1):
        degrees_distribution[i] = degrees.count(i) / len(degrees)

    return degrees_distribution


def degree_per_node(graph):
    number_nodes = graph.number_of_nodes()
    degree_per_node_array = [0] * number_nodes

    for i in range(number_nodes):
        for j in range(number_nodes):
            if graph.has_edge(i, j):
                degree_per_node_array[i] += 1
                degree_per_node_array[j] += 1

    return degree_per_node_array


def add_neighbors_to_node(graph, node, neighbors):
    for neighbor in neighbors:
        graph.add_edge(node, neighbor)


def random_nodes(nodes, m):
    nodes_selected = []
    for _ in range(m):
        nodes_selected.append(random.choice(nodes))
    return nodes_selected


def create_list_repeated_nodes(graph):
    repeated_nodes = []
    for node, degree in enumerate(degree_per_node(graph)):
        repeated_nodes.extend([node] * degree)
    return repeated_nodes


def barabasi_albert(n, m):
    graph = nx.star_graph(m)
    # The next node will be added in graph, the nx.star_graph generated a graph with m + 1 nodes
    next_node_to_add = m + 1
    # Probability of selecting node with higher degree must be higher -> Preferential attachment
    # For this a list that contains a node n times and n is the degree of the node
    node_repeated_degree = create_list_repeated_nodes(graph)
    print(node_repeated_degree)
    for node in range(next_node_to_add, n):
        random_neighbors = random_nodes(node_repeated_degree, m)
        add_neighbors_to_node(graph, node, random_neighbors)
        node_repeated_degree.extend(random_neighbors)
        node_repeated_degree.extend([node] * m)
        # print(graph)
        # print("repeated nodes: ", node_repeated_degree)
    return graph


def main():
    if __name__ == '__main__':
        n = 20000
        m = 3
        barabasi_generated = barabasi_albert(n, m)
        barabasi_generated_networkx = nx.barabasi_albert_graph(n, m)
        plot_degree_distribution(degree_per_node(barabasi_generated), degree_per_node(barabasi_generated_networkx))


if __name__ == '__main__':
    main()
