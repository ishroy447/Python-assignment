def print_board(board):
    """
    Print a 3x3 Tic-Tac-Toe board.
    board: List of lists representing the board (3x3)
    """
    print("\n")
    for i in range(3):
        print(" " + " | ".join(str(cell) for cell in board[i]))
        if i < 2:
            print("-----------")
    print("\n")

def create_empty_board():
    """Create an empty Tic-Tac-Toe board with numbers 1-9."""
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def create_custom_board():
    """Create a Tic-Tac-Toe board with X and O in some positions."""
    return [['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['X', 'O', 'X']]

# Example usage
if __name__ == "__main__":
    # Print empty board with numbers
    print("Empty board with numbers:")
    empty_board = create_empty_board()
    print_board(empty_board)
    
    # Print board with X's and O's
    print("Board with X's and O's:")
    custom_board = create_custom_board()
    print_board(custom_board) 