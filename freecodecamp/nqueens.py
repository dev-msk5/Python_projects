def dfs_n_queens(n: int):

    if n < 1:
        return []
    
    solutions = []
    board = [-1] * n
    columns = set()
    pos_diag = set()
    neg_diag = set()

    def backtrack(r):
        if r == n:
            solutions.append(board[:])
            return

        for c in range(n):
            if c in columns or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            columns.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r] = c

            backtrack(r + 1)

            columns.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)

    backtrack(0)
    return solutions
