"""
This module contain functions which are cheking whether the given board
fits the rules.
Git repository: https://github.com/msharsh/puzzle.git
"""
def check_rows(board: list) -> bool:
    """
    Checks if there are identical numbers in every row in the board.
Returns True if not, else False.
    >>> check_rows(["**** ****","***1 ****","**  3****","* 4 1****",\
        "     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    True
    """
    for i in range(len(board)):
        row_temp = []
        for j in range(len(board[i])):
            if board[i][j] != '*' and board[i][j] != ' ':
                if board[i][j] in row_temp:
                    return False
                else:
                    row_temp.append(board[i][j])
    return True


def check_columns(board: list) -> bool:
    """
    Checks if there are identical numbers in every column in the board.
Returns True if not, else False.
    >>> check_columns(["**** ****","***1 ****","**  3****","* 4 1****",\
        "     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    False
    """
    for i in range(len(board[0])):
        column_temp = []
        for j in range(len(board)):
            if board[j][i] != '*' and board[j][i] != ' ':
                if board[j][i] in column_temp:
                    return False
                else:
                    column_temp.append(board[j][i])
    return True


def check_color(board: list) -> bool:
    """
    Checks if there are identical numbers in every color row in the board.
Returns True if not, else False.
    >>> check_color(["**** ****","***1 ****","**  3****","* 4 1****",\
        "     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    True
    """
    starting_row = 0
    starting_column = 4
    for i in range(5):
        i = starting_row
        j = starting_column
        color_temp = []
        while i + j != 8:
            if board[i][j] != ' ':
                if board[i][j] in color_temp:
                    return False
                else:
                    color_temp.append(board[i][j])
            i += 1
        while i + j != 13:
            if board[i][j] != ' ':
                if board[i][j] in color_temp:
                    return False
                else:
                    color_temp.append(board[i][j])
            j += 1
        starting_row += 1
        starting_column -= 1
    return True


def validate_board(board: list) -> bool:
    """
    Checks if board fits the rules. If fits returns True, else False.
    >>> validate_board(["**** ****","***1 ****","**  3****","* 4 1****",\
        "     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    False
    """
    if check_rows(board) and\
        check_columns(board) and\
            check_color(board):
        return True
    return False
