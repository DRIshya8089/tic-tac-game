import math

def print_board(b):
    """Print the board with current marks or position numbers (1-9)."""
    for i in range(3):
        row = []
        for j in range(3):
            idx = i * 3 + j
            row.append(b[idx] if b[idx] != ' ' else str(idx + 1))
        print(' ' + ' | '.join(row))
        if i < 2:
            print('---+---+---')

def check_win(b, player):
    """Check if the given player has won."""
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    return any(b[i] == player and b[j] == player and b[k] == player for i,j,k in wins)

def get_moves(b):
    """Return list of available move indices."""
    return [i for i, cell in enumerate(b) if cell == ' ']

def minimax(b, depth, maximizing, ai, human):
    """Minimax algorithm for unbeatable AI."""
    if check_win(b, ai): return 10 - depth
    if check_win(b, human): return depth - 10
    if ' ' not in b: return 0

    if maximizing:
        best = -math.inf
        for move in get_moves(b):
            b[move] = ai
            score = minimax(b, depth + 1, False, ai, human)
            b[move] = ' '
            best = max(best, score)
        return best
    else:
        best = math.inf
        for move in get_moves(b):
            b[move] = human
            score = minimax(b, depth + 1, True, ai, human)
            b[move] = ' '
            best = min(best, score)
        return best

def best_move(b, ai, human):
    """Get the best move for the AI."""
    best_val, move = -math.inf, None
    for m in get_moves(b):
        b[m] = ai
        val = minimax(b, 0, False, ai, human)
        b[m] = ' '
        if val > best_val:
            best_val, move = val, m
    return move

def play():
    """Main game loop."""
    board = [' '] * 9
    human, ai = 'O', 'X'

    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O'. AI is 'X'. Enter positions as numbers 1–9.")
    
    while True:
        print_board(board)

        # Human move
        try:
            mv = int(input("Your move (1-9): ")) - 1
            if mv < 0 or mv > 8 or board[mv] != ' ':
                print("This place is already taken. Try with another.")
                continue
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue
        board[mv] = human

        if check_win(board, human):
            print_board(board)
            print("🎉 You win!")
            break
        if ' ' not in board:
            print_board(board)
            print("It's a draw.")
            break

        # AI move
        ai_mv = best_move(board, ai, human)
        board[ai_mv] = ai
        print(f"AI chooses position {ai_mv + 1}")

        if check_win(board, ai):
            print_board(board)
            print("💻 AI wins!")
            break
        if ' ' not in board:
            print_board(board)
            print("It's a draw.")
            break

if __name__ == "__main__":
    play()
