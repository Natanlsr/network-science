import random
import networkx as nx
import matplotlib.pyplot as plt
from math import comb, ceil, e, factorial


def random_graph(n, p):
    range_values = range(n)

    random_graph_generated = nx.Graph()
    random_graph_generated.add_nodes_from(range_values)

    for i in range_values:
        for j in range(i + 1, n):
            if random.random() < p:
                random_graph_generated.add_edge(i, j)

    return random_graph_generated


def degree_per_node(random_graph_values):
    number_nodes = random_graph_values.number_of_nodes()
    degree_per_node_array = [0] * number_nodes

    for i in range(number_nodes):
        for j in range(number_nodes):
            if random_graph_values.has_edge(i, j):
                degree_per_node_array[i] += 1

    return degree_per_node_array


def degree_distribution(degrees):
    degrees_distribution = [0] * (max(degrees) + 1)

    for i in range(max(degrees) + 1):
        degrees_distribution[i] = degrees.count(i) / len(degrees)

    return degrees_distribution


def get_binomial_values(p, n, nodes_degrees):
    qtd_values = max(nodes_degrees)
    binomial = [0] * (qtd_values + 1)

    for k in range(qtd_values + 1):
        combination = comb(n, k)
        binomial[k] = combination * (p ** k * ((1 - p) ** ((n - 1) - k)))

    return binomial


def get_poisson_values(k, nodes_degrees):
    qtd_values = max(nodes_degrees)
    poisson = [0] * (qtd_values + 1)

    for degree in range(qtd_values + 1):
        poisson[degree] = ((e ** -k) * (k ** degree)) / factorial(degree)

    return poisson


def get_degrees_values_to_plot(probabilities):
    first_value = next(x for x, val in enumerate(probabilities) if val > 0)
    last_value = next(x for x, val in enumerate(reversed(probabilities)) if val > 0) + len(probabilities)
    value = ceil(len(probabilities) * 0.50)

    increment = value
    decrement = value

    if first_value - value <= 0:
        decrement = 0

    if last_value + value >= len(probabilities):
        increment = len(probabilities) - last_value

    return range(first_value - decrement, last_value + increment)


def plot_degree_distribution(n, p, k, degrees_probabilities, nodes_degrees):
    degrees_to_plot = get_degrees_values_to_plot(degrees_probabilities)
    binomial_values = get_binomial_values(p, n, nodes_degrees)
    poisson_values = get_poisson_values(k, nodes_degrees)

    plt.xlabel('K')
    plt.ylabel('PK')
    plt.title('Degree Distribution Functions')

    plt.plot(
        degrees_to_plot,
        degrees_probabilities[degrees_to_plot[0]:degrees_to_plot[-1]+1],
        label="N=" + str(n)
    )

    plt.plot(
        degrees_to_plot,
        binomial_values[degrees_to_plot[0]:degrees_to_plot[-1] + 1],
        label="Binomial Function"
    )

    plt.plot(
        degrees_to_plot,
        poisson_values[degrees_to_plot[0]:degrees_to_plot[-1] + 1],
        label="Poisson Function"
    )

    plt.legend()
    plt.show()


def main():
    for exponent in range(2, 5):
        n = 10 ** exponent
        k = 50
        p = k / (n - 1)
        print("N: ", n, "\nK: ", k, "\nP: ", p)

        random_graph_generated = random_graph(n, p)
        # nx.draw(random_graph_generated)
        degrees = sum(d for n, d in random_graph_generated.degree())
        print("Average degree, networkx: ", degrees / random_graph_generated.number_of_nodes(), "\n")

        nodes_degrees = degree_per_node(random_graph_generated)
        degrees_sum = sum(nodes_degrees)
        print("Average degree calculated: ", degrees_sum / random_graph_generated.number_of_nodes(), "\n")

        degrees_distribution = degree_distribution(nodes_degrees)

        plot_degree_distribution(n, p, k, degrees_distribution, nodes_degrees)

        # plot_degree_distribution(random_graph, n, p)
        # plt.savefig("random-graph-" + str(exponent-1) + ".png")


if __name__ == '__main__':
    main()
