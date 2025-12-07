def dfs(adj_matrix, node):
    visited = set()
    order = []

    def _dfs(n):
        visited.add(n)
        order.append(n)
        # iterate neighbors in descending index order
        for index in range(len(adj_matrix[n]) - 1, -1, -1):
            if adj_matrix[n][index] == 1 and index not in visited:
                _dfs(index)

    _dfs(node)
    return order

print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))
# print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 3))
