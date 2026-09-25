"""Checkmate"""
def checkmate(board):
    """Check function"""
    if isinstance(board, str) and board != "":
        board_list = board.splitlines() #board.split('\n')

        # Check if Square
        size_row = len(board_list)
        for r in board_list:
            r = r.strip()
            if len(r) != size_row:
                print("Error!")
                return

        board_size = size_row # Because board is always square so we can use board_size for both row and col
        is_checked = False

        # King count check
        king_count = 0
        for r in board_list:
            king_count += r.count("K")

        if (king_count == 1):
            for r in range(board_size):
                for c in range(board_size):
                    if board_list[r][c] == "R":
                        is_checked = is_rook_checking(board_list, r, c, board_size)
                    elif board_list[r][c] == "B":
                        is_checked = is_bishop_checking(board_list, r, c, board_size)
                    elif board_list[r][c] == "Q":
                        is_checked = is_queen_checking(board_list, r, c, board_size)
                    elif board_list[r][c] == "P":
                        is_checked = is_pawn_checking(board_list, r, c, board_size)
                    if is_checked:
                        print("Success")
                        return
            print("Failed")
        else:
            print("Error!")
    else:
        print("Error!")


def is_rook_checking(board, row, col, board_size):
    """Check if rook can check the king"""
    # to N
    if check_after_move_to(board, row, col, -1, 0, board_size):
        return True

    # to S
    if check_after_move_to(board, row, col, 1, 0, board_size):
        return True

    # to W
    if check_after_move_to(board, row, col, 0, -1, board_size):
        return True
    
    # to E
    if check_after_move_to(board, row, col, 0, 1, board_size):
        return True
    
    return False


def is_bishop_checking(board, row, col, board_size):
    """Check if bishop can check the king"""
    #to NW
    if check_after_move_to(board, row, col, -1, -1, board_size):
        return True

    #to NE
    if check_after_move_to(board, row, col, -1, 1, board_size):
        return True

    #to SW
    r, c = row + 1, col - 1
    if check_after_move_to(board, row, col, 1, -1, board_size):
        return True

    #to SE
    r, c = row + 1, col + 1
    if check_after_move_to(board, row, col, 1, 1, board_size):
        return True

    return False


def is_queen_checking(board, row, col, board_size):
    """Check if queen can check the king"""
    if is_rook_checking(board, row, col, board_size) or is_bishop_checking(board, row, col, board_size):
        return True
    return False

def is_pawn_checking(board, row, col, board_size):
    """Check if pawn can check the king"""
    if row - 1 >= 0:
        if col - 1 >= 0 and board[row - 1][col - 1] == "K":
            return True
        if col + 1 < board_size and board[row - 1][col + 1] == "K":
            return True
    return False


def check_after_move_to(board, start_r, start_c, step_r, step_c, board_size):
    """Return if check after move to various direction"""
    r, c = start_r + step_r, start_c + step_c
    while (r in range(0, board_size) and c in range(0, board_size)):
        if board[r][c] == "K":
            return True
        elif board[r][c] in ["R", "B", "Q", "P"]:
            break
        r += step_r
        c += step_c
    return False