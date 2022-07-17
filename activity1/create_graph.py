def read_undirected_graph_from_file(file_name):
    matrix_from_file, max_value = read_matrix_from_file_and_max_value(file_name)
    matrix_final = create_matrix_with_zeros(max_value)

    populate_matrix(matrix_from_file, matrix_final, True)

    return matrix_final


def read_directed_graph_from_file(file_name):
    matrix_from_file, max_value = read_matrix_from_file_and_max_value(file_name)
    matrix_final = create_matrix_with_zeros(max_value)

    populate_matrix(matrix_from_file, matrix_final, False)

    return matrix_final


def read_matrix_from_file_and_max_value(file_name):
    matrix_from_file = []
    max_value = -1

    # Read matrix from file and get max value (len of matrix)
    with open(file_name) as f:
        for line in f:
            number_1, number_2 = line.replace('\n', "").split(" ")
            numbers = [int(number_1), int(number_2)]
            max_local = max(numbers)
            if max_value < max_local:
                max_value = max_local
            matrix_from_file.append(numbers)

    return matrix_from_file, max_value


def create_matrix_with_zeros(max_value):
    # Create matrix (max_value x max_value) with zeros
    matrix_final = []
    for i in range(max_value):
        matrix_final.append([0] * max_value)
    return matrix_final


def populate_matrix(matrix_from_file, matrix_final, is_undirected):
    # Populate matrix according to matrix from file
    for node in matrix_from_file:
        i = node[0] - 1
        j = node[1] - 1
        matrix_final[i][j] = 1
        if is_undirected:
            matrix_final[j][i] = 1
