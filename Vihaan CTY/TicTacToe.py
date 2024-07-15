def fullprint(gameboard):
    for i in range(len(gameboard)):
        for k in range(len(gameboard[i])):
            if k == len(gameboard[i]) - 1:
                print(gameboard[i][k])
            else:
                print(gameboard[i][k], end=" ")
    print()

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return True
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return True
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return True
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return True
    return False

def tic_tac_toe():
    player = "X"
    gameboard = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    Z = 0
    print("Welcome to Tic-Tac-Toe")
    while True:
        fullprint(gameboard)
        Y = int(input("Which row? (1-3) ")) - 1
        X = int(input("Which column? (1-3) ")) - 1

        if Y < 0 or Y >= 3 or X < 0 or X >= 3:
            print("Cant move there.")
            continue

        if gameboard[Y][X] != 0:
            print("Cant move there.")
            continue

        gameboard[Y][X] = player
        Z += 1

        if check_winner(gameboard):
            fullprint(gameboard)
            print(f"Player {player} wins!!! :)")
            break

        if Z == 9:
            fullprint(gameboard)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()
