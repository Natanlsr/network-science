import matplotlib.pyplot as plt


def degree_per_node(matrix, is_undirected_out=False):
    matrix_len = len(matrix)
    degree_per_node_array = [0] * matrix_len

    for i in range(matrix_len):
        for j in range(matrix_len):
            if is_undirected_out:
                degree_per_node_array[j] += matrix[i][j]
            else:
                degree_per_node_array[i] += matrix[i][j]

    return degree_per_node_array


def average_degree_sum(degrees):
    matrix_len = len(degrees)
    sum_degree_value = 0
    average_degree_value = 0

    for degree in degrees:
        average_degree_value += degree

    if matrix_len != 0:
        sum_degree_value = average_degree_value / matrix_len

    return sum_degree_value


def plot_degree_distribution(degrees, file_name):
    len_degrees = len(degrees)
    left = list(range((max(degrees) + 2)))
    p = [0] * (max(degrees) + 2)

    for i in left:
        p[i] = degrees.count(i) / len_degrees

    plt.xlabel('K')
    plt.ylabel('PK')
    plt.title('Degree Distribution: ' + file_name.replace('_', " "))

    plt.bar(left, p, width=0.8, color=['green'])
    plt.savefig(file_name + ".png")

    return plt
