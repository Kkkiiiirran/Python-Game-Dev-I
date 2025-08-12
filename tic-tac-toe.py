def print_board(board):
    """Print the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, row=0, col=0):
    """
    Check for a winner using recursion.
    - Checks rows and columns by incrementing indices recursively.
    - Stops when a winner is found or all rows/columns are checked.
    """
    # Base case: if we've checked all rows and columns
    if row == 3:
        return None  # No winner found

    # Check current row
    if board[row][0] == board[row][1] == board[row][2] and board[row][0] != " ":
        return board[row][0]

    # Check current column
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
        return board[0][col]

    # Recursively check the next row and column
    return check_winner(board, row + 1, col + 1)


def check_diagonals(board):
    """Check the two diagonals for a winner."""
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None
    

def is_full(board):
    """Check if the board is full (no more moves)."""
    for row in board:
        for cell in row:
            if cell == " ":
                return False  # Found an empty cell, board is not full
    return True  # No empty cells found, board is full
    

def play_game():
    """Main function to play the game."""
    # Initialize the board
    board = []
    for i in range(3):
      row = []
      for j in range(3):
        row.append(" ")
      board.append(row)
      
    ''' or using list comprehension
    board = [[" " for i in range(3)] for j in range(3)]'''

    current_player = "X"

    # Game loop
    while True:
        print_board(board)
        print("It's {}'s turn!".format(current_player))

        # Get player input
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        # Check if the cell is empty
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Cell already taken! Try again.")
            continue

        # Check for a winner
        winner = check_winner(board) or check_diagonals(board)
        if winner:
            print_board(board)
            print("{} wins!".format(winner))
            break

        # Check for a draw
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()