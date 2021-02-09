"""
This module contain functions which are cheking whether the given board
fits the rules.
Git repository: https://github.com/msharsh/puzzle.git
"""
board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  2  ****"
]

def check_rows(board: list) -> bool:
    """
    Checks if there are identical numbers in every row in the board.
Returns True if not, else False.
    """
    for row in board:
        row_temp = []
        for i in range(len(row)):
            print(row_temp)
            if row[i] != '*' and row[i] != ' ':
                if row[i] in row_temp:
                    return False
                else:
                    row_temp.append(row[i])
    return True


def check_columns(board: list) -> bool:
    """
    Checks if there are identical numbers in every column in the board.
Returns True if not, else False.
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
    """
    pass


def validate_board(board: list) -> bool:
    """
    Checks if board fits the rules. If fits returns True, else False.
    """
    pass
print(check_rows(board))
print(check_columns(board))