def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col, n):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens(board, row, n):
    # Base case: if all queens are placed, we have a solution
    if row == n:
        print_board(board)
        return True

    solution_found = False
    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'  # Place queen
            solution_found |= solve_n_queens(board, row + 1, n)  # Recurse
            board[row][col] = '.'  # Backtrack by removing queen

    return solution_found

def solve_8_queens():
    n = 8
    board = [['.' for _ in range(n)] for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists.")

# Example usage
solve_8_queens()
