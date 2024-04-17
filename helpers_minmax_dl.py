import random

def draw_board(spots):
    # Function to print the 5x5 game board
    for row in range(1, 26, 5):
        # Use formatted strings to maintain alignment
        print("|" + "|".join(f" {spots[i]:^3} " for i in range(row, row + 5)) + "|")

def check_turn(turn):
    # Determine whose turn it is
    return 'O' if turn % 2 == 0 else 'X'

def check_for_win(spots, player, size=5):
    # Check all possible win conditions for the player on a 5x5 board
    win_conditions = [[i + j for j in range(size)] for i in range(1, 22, 5)] + \
                     [[i + j * 5 for j in range(size)] for i in range(1, 6)] + \
                     [[i for i in range(1, 26, 6)], [i for i in range(5, 22, 4)]]
    return any(all(spots[i] == player for i in condition) for condition in win_conditions)

def get_player_move(spots, max_spot):
    while True:
        choice = input(f"Enter your move (1-{max_spot}) or 'q' to quit: ")
        if choice.lower() == 'q':
            return 'q'  # Returning 'q' to indicate quit
        try:
            choice = int(choice)
            if 1 <= choice <= max_spot and spots[choice] not in ['X', 'O']:
                return choice
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")


def minimax(spots, player, depth=0, is_maximizing_player=True, max_depth=3):
    # Terminal states check
    if check_for_win(spots, 'X', 5):
        return {'score': -10 + depth}
    elif check_for_win(spots, 'O', 5):
        return {'score': 10 - depth}
    elif all(value in ['X', 'O'] for value in spots.values()) or depth == max_depth:
        return {'score': 0}

    best_score = -float('inf') if is_maximizing_player else float('inf')
    best_move = None
    for i in range(1, 26):
        if spots[i] not in ['X', 'O']:
            spots[i] = 'O' if is_maximizing_player else 'X'
            score = minimax(spots, 'X' if is_maximizing_player else 'O', depth + 1, not is_maximizing_player, max_depth)['score']
            spots[i] = str(i)  # Reset spot

            if is_maximizing_player and score > best_score or not is_maximizing_player and score < best_score:
                best_score, best_move = score, i

    if best_move is None:  # Fallback to the first available spot if no move found
        for i in range(1, 26):
            if spots[i] not in ['X', 'O']:
                best_move = i
                break

    return {'score': best_score, 'index': best_move}
