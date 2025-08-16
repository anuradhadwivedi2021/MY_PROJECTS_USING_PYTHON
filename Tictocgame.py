# Tic Tac Toe in Python (Console Version)

# 1. Game Board
board = [" " for _ in range(9)]

# 2. Print Board Function
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# 3. Check Winner
def check_winner(player):
    # Winning positions (rows, cols, diagonals)
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# 4. Main Game Loop
def play_game():
    current_player = "X"
    moves = 0
    
    while True:
        print_board()
        move = int(input(f"Player {current_player}, choose position (1-9): ")) - 1
        
        # Check valid move
        if board[move] == " ":
            board[move] = current_player
            moves += 1
        else:
            print("❌ Position already taken, try again.")
            continue
        
        # Check winner
        if check_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins!")
            break
        
        # Check draw
        if moves == 9:
            print_board()
            print("🤝 It's a draw!")
            break
        
        # Switch Player
        current_player = "O" if current_player == "X" else "X"

# Run Game
play_game()