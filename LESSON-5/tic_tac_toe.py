import pgzrun

# Constants
WIDTH = 300
HEIGHT = 300
CELL_SIZE = WIDTH // 3

# Game Variables
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
winner = None
game_over = False

def draw():
    """Draws the game board, grid, marks, and winner message."""
    screen.fill((255, 255, 255))

    # Draw grid lines
    for i in range(1, 3):
        screen.draw.line((i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), "black")
        screen.draw.line((0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), "black")

    # Draw X and O
    for row in range(3):
        for col in range(3):
            x, y = col * CELL_SIZE, row * CELL_SIZE
            if board[row][col] == "X":
                draw_x(x, y)
            elif board[row][col] == "O":
                draw_o(x, y)

    # Display winner or draw message
    if game_over:
        message = f"{winner} Wins! Click to Restart" if winner else "It's a Draw! Click to Restart"
        screen.draw.text(message, (50, HEIGHT - 40), fontsize=30, color="red")

def draw_x(x, y):
    """Draws an 'X' at the given cell position."""
    padding = 20
    screen.draw.line((x + padding, y + padding), 
                     (x + CELL_SIZE - padding, y + CELL_SIZE - padding), "blue")
    screen.draw.line((x + CELL_SIZE - padding, y + padding), 
                     (x + padding, y + CELL_SIZE - padding), "blue")

def draw_o(x, y):
    """Draws an 'O' at the given cell position."""
    padding = 20
    screen.draw.circle((x + CELL_SIZE // 2, y + CELL_SIZE // 2), 
                       (CELL_SIZE // 2 - padding), "green")

def check_winner():
    """Checks for a winner or draw and updates the game state."""
    global winner, game_over

    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
            winner, game_over = board[i][0], True
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            winner, game_over = board[0][i], True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        winner, game_over = board[0][0], True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        winner, game_over = board[0][2], True

    # Check for draw (if no empty cells and no winner)
    if not winner and all(board[row][col] != "" for row in range(3) for col in range(3)):
        game_over = True

def on_mouse_down(pos):
    """Handles mouse clicks for placing marks and restarting the game."""
    global current_player, board, winner, game_over

    # Restart game if it's over
    if game_over:
        reset_game()
        return

    col, row = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE

    # Place mark if cell is empty
    if board[row][col] == "":
        board[row][col] = current_player
        check_winner()

        if not game_over:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    """Resets the game board and state for a new round."""
    global board, current_player, winner, game_over
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    winner = None
    game_over = False

pgzrun.go()
