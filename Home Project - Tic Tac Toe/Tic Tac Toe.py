import random

def print_board(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("------------")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("------------")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")


def win_check(board, s):
    for i in range(3):
        if board[i][0] == s and board[i][1] == s and board[i][2] == s: return True
        if board[0][i] == s and board[1][i] == s and board[2][i] == s: return True
    if board[0][0] == s and board[1][1] == s and board[2][2] == s: return True
    if board[0][2] == s and board[1][1] == s and board[2][0] == s: return True
    return False


def player_move(current_name, current_symbol, board, is_computer):
    while True:
        try:
            if is_computer:
                pick = str(random.randint(1, 9))
            else:
                pick = input(f"{current_name} ({current_symbol}), pick a square (1-9): ")

            row, col = -1, -1
            if pick == "1":
                row, col = 0, 0
            elif pick == "2":
                row, col = 0, 1
            elif pick == "3":
                row, col = 0, 2
            elif pick == "4":
                row, col = 1, 0
            elif pick == "5":
                row, col = 1, 1
            elif pick == "6":
                row, col = 1, 2
            elif pick == "7":
                row, col = 2, 0
            elif pick == "8":
                row, col = 2, 1
            elif pick == "9":
                row, col = 2, 2

            if row != -1 and board[row][col] == " ":
                if is_computer:
                    print(f"Computer chose square {pick}")
                return row, col
            else:
                if not is_computer:
                    print("Invalid move or spot taken. Try again.")
        except Exception:
            print("An error occurred. Please try again.")


def play_game():
    mode = input("Select Mode: (1) Player vs Player | (2) Player vs Computer: ")
    while mode not in ("1", "2"):
        print("Invalid mode. Please try again.")
        mode = input("Select Mode: (1) Player vs Player | (2) Player vs Computer: ")
    vs_computer = (mode == "2")
    player_1_name = input("Enter Player 1 name: ")
    if vs_computer:
        player_2_name = "Computer"
    else:
        player_2_name = input("Enter Player 2 name: ")

    player_1_symbol = input(player_1_name + ", choose X or O (or press anything else for random): ").upper()
    if player_1_symbol not in ["X", "O"]:
        player_1_symbol = random.choice(["X", "O"])
    player_2_symbol = "O" if player_1_symbol == "X" else "X"
    print(f"{player_1_name} is {player_1_symbol}")
    print(f"{player_2_name} is {player_2_symbol}")

    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    current_name, current_symbol = player_1_name, player_1_symbol
    moves_count = 0

    while moves_count < 9:
        print_board(board)
        is_comp_turn = (vs_computer and current_name == "Computer")
        row, col = player_move(current_name, current_symbol, board, is_comp_turn)
        board[row][col] = current_symbol
        moves_count += 1
        if win_check(board, current_symbol):
            print_board(board)
            print(f"The winner is {current_name}")
            return
        if current_name == player_1_name:
            current_name, current_symbol = player_2_name, player_2_symbol
        else:
            current_name, current_symbol = player_1_name, player_1_symbol

    print_board(board)
    print("The game is a tie!")

if __name__ == '__main__':
    while True:
        play_game()
        play_again = input("Play again? (y/n):").lower()
        if play_again != 'y' and play_again != 'yes':
            print("Goodbye.")
            break