//ENJOY//

def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()


def has_winner(board, marker):
    for row in board:
        if all(cell == marker for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == marker for row in range(3)):
            return True

    if all(board[index][index] == marker for index in range(3)):
        return True

    if all(board[index][2 - index] == marker for index in range(3)):
        return True

    return False


def get_player_name(player_number):
    while True:
        name = input(f"Enter player {player_number}'s name: ").strip()
        if name:
            return name

        print("Name cannot be blank.")


def get_move(board, player_name):
    while True:
        try:
            row = int(input(f"{player_name}, enter row (1-3): ")) - 1
            col = int(input(f"{player_name}, enter column (1-3): ")) - 1
        except ValueError:
            print("Please enter numbers only.")
            continue

        if row not in range(3) or col not in range(3):
            print("Row and column must both be between 1 and 3.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken. Try again.")
            continue

        return row, col


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    markers = {1: "X", 2: "O"}
    names = {
        1: get_player_name(1),
        2: get_player_name(2),
    }
    current_player = 1

    for _ in range(9):
        print_board(board)
        row, col = get_move(board, names[current_player])
        board[row][col] = markers[current_player]

        if has_winner(board, markers[current_player]):
            print_board(board)
            print(f"{names[current_player]} wins")
            return

        current_player = 2 if current_player == 1 else 1

    print_board(board)
    print("It's a draw")


if __name__ == "__main__":
    play_game()
