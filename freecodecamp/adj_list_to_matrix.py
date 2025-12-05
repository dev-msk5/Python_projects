def adjacency_list_to_matrix(adj_dict : dict):
    n = len(adj_dict)
    matrix = []
    for row in adj_dict.values():
        row_list = [0] * n
        for item in row:
            for i in range(n):
                if i == item:
                    row_list[i] = 1
        print(row_list)
        matrix.append(row_list)
    return matrix

adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})