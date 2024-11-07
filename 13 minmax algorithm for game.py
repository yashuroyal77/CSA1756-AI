import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for i in range(3):
        print(' | '.join(board[i]))
        if i < 2:
            print("---------")

# Function to check if a player has won
def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    return all([cell != ' ' for row in board for cell in row])

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    # Maximizing for AI ('O') and minimizing for player ('X')
    if check_winner(board, 'O'):
        return 10 - depth  # AI wins
    if check_winner(board, 'X'):
        return depth - 10  # Player wins
    if is_board_full(board):
        return 0  # Draw
    
    if is_maximizing:  # Maximizing for AI ('O')
        max_eval = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  # Beta cutoff
        return max_eval
    else:  # Minimizing for player ('X')
        min_eval = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  # Alpha cutoff
        return min_eval

# Function to find the best move for the AI (O)
def find_best_move(board):
    best_move = (-1, -1)
    best_value = -math.inf

    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                move_value = minimax(board, 0, False, -math.inf, math.inf)
                board[row][col] = ' '
                if move_value > best_value:
                    best_value = move_value
                    best_move = (row, col)

    return best_move

# Function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # Player 'X' is the human, 'O' is the AI

    while True:
        print_board(board)
        if current_player == 'X':
            print("Player X's turn")
            row, col = map(int, input("Enter row and column (0-2) separated by a space: ").split())
            if board[row][col] != ' ':
                print("Cell already taken, try again.")
                continue
            board[row][col] = 'X'
        else:
            print("AI's Turn (Player O)")
            row, col = find_best_move(board)
            print(f"AI places O at ({row}, {col})")
            board[row][col] = 'O'

        if check_winner(board, 'X'):
            print_board(board)
            print("Player X wins!")
            break
        elif check_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'  # Switch turn

# Start the game
play_game()
