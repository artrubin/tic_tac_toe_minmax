import os
import time
from helpers_minmax_dl import draw_board, check_for_win, check_turn, minimax, get_player_move

# Initialize the game board for a 5x5 Tic-Tac-Toe game
spots = {i: str(i) for i in range(1, 26)}
playing, complete = True, False
turn = 0  # Keeps track of the current turn
computer_moves = 0  # Counter for computer moves
player_moves = 0  # Counter for player moves
computer_time_spent = 0  # Time spent by computer
player_time_spent = 0  # Time spent by player

while playing:
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')  # Clearing the console screen, "nt" for windows, "clear" for Linux
    draw_board(spots)  # Display the current state of the game board

    current_player = check_turn(turn)  # Determine whose turn it is
    print(f"Player {current_player}'s turn: Pick your spot or press q to quit")

    start_time = time.time()  # Start timing

    if current_player == 'X':  # Player's turn
        choice = get_player_move(spots, 25) # Adjusted max spot for 5x5 board
        if choice == 'q':
            playing = False
        else:
            spots[choice] = 'X'
            turn += 1
            player_moves += 1  # Increment the player's move counter
            end_time = time.time()  # End timing
            player_time_spent += end_time - start_time  # Accumulate player time

    else:  # Computer's turn
        result = minimax(spots, 'O')
        choice = result['index']
        spots[choice] = 'O'
        computer_moves += 1  # Increment the computer's move counter
        turn += 1
        end_time = time.time()  # End timing
        computer_time_spent += end_time - start_time  # Accumulate computers time

    # Check if the game has ended
    if check_for_win(spots, 'X', 5) or check_for_win(spots, 'O', 5) or turn == 25:
        playing, complete = False, True

os.system('cls' if os.name == 'nt' else 'clear')  # clearing the console screen, "nt" for windows, "clear" for Linux
draw_board(spots)  # Display the current state of the game board

if complete:  # Announce the result
    if check_for_win(spots, 'X', 5):
        print(f"Player Wins in {player_moves} moves!")
        print(f"Total time spent by computer: {computer_time_spent:.2f} seconds.")
        print(f"Total time spent by player: {player_time_spent:.2f} seconds.")

    elif check_for_win(spots, 'O', 5):
        print(f"Computer Wins in {computer_moves} moves!")
        print(f"Total time spent by computer: {computer_time_spent:.2f} seconds.")
        print(f"Total time spent by player: {player_time_spent:.2f} seconds.")

    else:
        print("It's a Tie!")
        print(f"Total time spent by computer: {computer_time_spent:.2f} seconds.")
        print(f"Total time spent by player: {player_time_spent:.2f} seconds.")
else:
    print("Game Over")

print("Thanks for playing!")
