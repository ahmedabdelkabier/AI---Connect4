import random
from math import inf as infinety

empty = -1
player_card = 1
AI_card = 2

rows = 6
columns = 7

player = 1
AI_player = 0


def minimax_algorithm(current_state, depth, is_maximizing):
    valid_locations = get_valid_locations(current_state)
    is_game_over = game_over(current_state)

    if depth == 0 or is_game_over:
        if is_game_over:
            if winning(current_state, AI_card):
                return +infinety
            elif winning(current_state, player_card):
                return -infinety
            else:
                return 0

    if is_maximizing:  # AI-player
        max_Eval = -infinety
        col = random.choice(valid_locations)
        for column in valid_locations:
            row = get_row(current_state, col)
            board_copy = current_state.copy()
            add_pice(board_copy, row, column, AI_card)
            new_score = minimax_algorithm(board_copy, depth - 1, False)
            if new_score > max_Eval:
                max_Eval = new_score
                col = column
        return max_Eval
    else:
        min_Eval = +infinety
        col = random.choice(valid_locations)
        for column in valid_locations:
            row = get_row(current_state, col)
            board_copy = current_state.copy()
            add_pice(board_copy, row, col, player_card)  # call GUI function to add card
            new_score = minimax_algorithm(board_copy, depth - 1, True)
            if new_score < min_Eval:
                min_Eval = new_score
                col = column
        return min_Eval


def minimax_algorithm_alpha_beta(current_state, depth, alpha, beta, is_maximizing):
    valid_locations = get_valid_locations(current_state)
    is_game_over = game_over(current_state)

    if depth == 0 or is_game_over:
        if is_game_over:
            if winning(current_state, player_card):
                return +infinety
            elif winning(current_state, AI_card):
                return -infinety
            else:
                return 0

    if is_maximizing:
        max_Eval = -infinety
        col = random.choice(valid_locations)
        for column in valid_locations:
            row = get_row(current_state, col)
            board_copy = current_state.copy()
            add_pice(board_copy, row, column, AI_card)
            new_score = minimax_algorithm(board_copy, depth - 1, False)
            if new_score > max_Eval:
                max_Eval = new_score
                col = column
                alpha = max(alpha, max_Eval)
                if alpha >= beta:
                    break
        return max_Eval

    else:
        min_Eval = +infinety
        col = random.choice(valid_locations)
        for column in valid_locations:
            row = get_row(current_state, col)
            board_copy = current_state.copy()
            add_pice(board_copy, row, col, player_card)
            new_score = minimax_algorithm(board_copy, depth - 1, True)
            if new_score < min_Eval:
                min_Eval = new_score
                col = column
            beta = min(alpha, min_Eval)
            if alpha >= beta:
                break
        return min_Eval


def get_row(current_state, col):
    for row in range(rows):
        if current_state[row][col] == 0:
            return row


def add_pice(current_state, row, col, pice):
    current_state[row][col] = pice


def get_valid_locations(current_state):
    valid_locations = []
    for col in range(columns):
        if is_location_valid(current_state, col):
            valid_locations.append(col)
    return valid_locations


def is_location_valid(current_state, col):
    is_valid = False
    if current_state[columns - 1][col] == 0:
        is_valid = True
    return is_valid


def game_over(current_state):
    return winning(current_state, player_card) or winning(current_state, AI_card) or len(
        get_valid_locations(current_state)) == 0


def winning(current_state, card):
    # check horizontal win
    for col in range(columns - 3):
        for r in range(rows):
            if current_state[r][col] == card and current_state[r][col + 1] == card and current_state[r][
                col + 2] == card and current_state[r][col + 3] == card:
                return True
    # check columns win
    for col in range(columns):
        for r in range(rows - 3):
            if current_state[r][col] == card and current_state[r + 1][col] == card and current_state[r + 2][
                col] == card and current_state[r + 3][col] == card:
                return True

    # check diagonal1
    for col in range(columns - 3):
        for r in range(rows - 3):
            if current_state[r][col] == card and current_state[r + 1][col + 1] == card and current_state[r + 2][
                col + 2] == card and current_state[r + 3][col + 3] == card:
                return True

    # check diagnonal2
    for col in range(columns - 3):
        for r in range(3, rows):
            if current_state[r][col] == card and current_state[r - 1][col + 1] == card and current_state[r - 2][
                col + 2] == card and current_state[r - 3][col + 3] == card:
                return True
