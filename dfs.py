def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def dfs(row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                dfs(row + 1)
                board[row] = 0

    result = []
    board = [0] * n  
    dfs(0)
    return result

n = 8
solutions = solve_n_queens(n)
for solution in solutions:
    for row in solution:
        print(" ".join(["Q" if col == row else "." for col in range(n)]))
    print("\n")
