from copy import deepcopy
import random
from math import inf as infinety
from Heuristic import h

empty = -1
player_card = 1
AI_card = 2

rows = 6
columns = 7

player = 1
AI_player = 0


def minimax_algorithm(current_state, depth, is_maximizing):
    valid_locations = get_valid_locations(current_state)

    #is_game_over = game_over(current_state)

    if depth == 0 and len(valid_locations) != 0:
        return h(current_state , AI_card),None
    if len(valid_locations) == 0:
        AI_score = winning(current_state , AI_card)
        Humman_score = winning(current_state , player_card)
        if(AI_score > Humman_score):
            return +infinety,None
        elif(AI_score < Humman_score):
            return -infinety,None
        else:
            return 0,None

    if is_maximizing:  # AI-player
        max_Eval = -infinety
        col = random.choice(valid_locations)
        for column in valid_locations:
 
            row = get_row(current_state, column)
            board_copy = deepcopy(current_state)
            add_pice(board_copy, row, column, AI_card)
            new_score ,c = minimax_algorithm(board_copy, depth - 1, False)
            if new_score > max_Eval:
                max_Eval = new_score
                col = column
        return max_Eval,col

    else:
        min_Eval = +infinety
        col = random.choice(valid_locations)
        for column in valid_locations:
 
            row = get_row(current_state, column)
            board_copy = deepcopy(current_state)
            add_pice(board_copy, row, column, player_card)  # call GUI function to add card
            new_score,c = minimax_algorithm(board_copy, depth - 1, True)
            if new_score < min_Eval:
                min_Eval = new_score
                col = column
        return min_Eval,col



def minimax_algorithm_alpha_beta(current_state, depth, alpha, beta, is_maximizing):
    valid_locations = get_valid_locations(current_state)
 
    # is_game_over = game_over(current_state)

    if depth == 0 and len(valid_locations) != 0:
        return h(current_state, AI_card), None
    if len(valid_locations) == 0:
        AI_score = winning(current_state, AI_card)
        Humman_score = winning(current_state, player_card)
        if (AI_score > Humman_score):
            return +infinety, None
        elif (AI_score < Humman_score):
            return -infinety, None
        else:
            return 0, None
    if is_maximizing:  # AI-player
        max_Eval = -infinety
        col = random.choice(valid_locations)
        for column in valid_locations:
            row = get_row(current_state, column)
            board_copy = deepcopy(current_state)
            add_pice(board_copy, row, column, AI_card)
            new_score, c = minimax_algorithm(board_copy, depth - 1, False)

            if new_score > max_Eval:
                max_Eval = new_score
                col = column
                alpha = max(alpha, max_Eval)
                if alpha >= beta:
                    break
 
        return max_Eval,col

    else:
        min_Eval = +infinety
        col = random.choice(valid_locations)
        for column in valid_locations:
 
            row = get_row(current_state, column)
            board_copy = deepcopy(current_state)
            add_pice(board_copy, row, column, player_card)  # call GUI function to add card
            new_score, c = minimax_algorithm(board_copy, depth - 1, True)

            if new_score < min_Eval:
                min_Eval = new_score
                col = column
            beta = min(alpha, min_Eval)
            if alpha >= beta:
                break
 
        return min_Eval,col


def get_row(current_state, col):
    for row in range(rows-1,-1,-1):

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
    
    if current_state[0][col] == 0:

        is_valid = True
    return is_valid


def game_over(current_state):
    return winning(current_state, player_card) or winning(current_state, AI_card) or len(
        get_valid_locations(current_state)) == 0



def winning(current_state, card_type):
    _f_counter = 0
    for row in range(rows):
        counter = 0
        for col in range(columns):
            if current_state[row][col] == card_type and col < columns - 1:
                counter += 1
            else:
                if current_state[row][col] == card_type:
                    counter += 1
                while (True):
                    if counter // 4 != 0:
                        _f_counter += counter // 4
                        counter = counter % 4
                    else:
                        break
                counter = 0

    # check columns win
    for col in range(columns):
        counter_c = 0
        for r in range(rows):
            if current_state[r][col] == card_type and r < rows - 1:
                counter_c += 1
            else:
                if current_state[r][col] == card_type:
                    counter_c += 1
                while (True):
                    if counter_c // 4 != 0:
                        _f_counter += counter_c // 4
                        counter_c = counter_c % 4
                    else:
                        break
                counter_c = 0

    # check diagonal1 /
    for i in range((rows + columns) - 1):
        counter_d1 = 0
        for j in range(i + 1):
            k = i - j
            flag = False
            if k < rows and j < columns:
                if current_state[k][j] == card_type:
                    counter_d1 += 1
                    if (j == columns - 1) or k == 0:
                        flag = True
                else:
                    flag = True

                if flag:
                    while True:
                        if counter_d1 // 4 != 0:
                            _f_counter += counter_d1 // 4
                            counter_d1 = counter_d1 % 4
                        else:
                            break
                    counter_d1 = 0

    # check diagnonal2 \ upwards
    for i in range(1 - rows, columns):
        counter_d2 = 0
        for j in range(rows):
            flag = False
            if (i + j) >= 0 and (i + j) < columns:
                if current_state[j][i + j] == card_type:
                    counter_d2 += 1
                    if i + j == columns - 1 or j == rows - 1:
                        flag = True
                else:
                    flag = True

                if flag:
                    while (True):
                        if counter_d2 // 4 != 0:
                            _f_counter += counter_d2 // 4
                            counter_d2 = counter_d2 % 4
                        else:
                            break
                    counter_d2 = 0
    return _f_counter
