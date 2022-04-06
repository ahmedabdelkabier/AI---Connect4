fourh_W = 30
third_W = 10
twos_W = 3

rows = 6
columns = 7


def h(current_state, card_type):
    _f_counter = 0
    _th_counter = 0
    _t_counter = 0

    # check horizontal win
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
                    elif counter // 3 != 0:
                        _th_counter += counter // 3
                        counter = counter % 3
                    elif counter // 2 != 0:
                        _t_counter += counter // 2
                        counter = counter % 2
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
                    elif counter_c // 3 != 0:
                        _th_counter += counter_c // 3
                        counter_c = counter_c % 3
                    elif counter_c // 2 != 0:
                        _t_counter += counter_c // 2
                        counter_c = counter_c % 2
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
                        elif counter_d1 // 3 != 0:
                            _th_counter += counter_d1 // 3
                            counter_d1 = counter_d1 % 3
                        elif counter_d1 // 2 != 0:
                            _t_counter += counter_d1 // 2
                            counter_d1 = counter_d1 % 2
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
                    if i + j == columns - 1 or j == rows -1:
                        flag = True
                else:
                    flag = True

                if flag:
                    while (True):
                        if counter_d2 // 4 != 0:
                            _f_counter += counter_d2 // 4
                            counter_d2 = counter_d2 % 4
                        elif counter_d2 // 3 != 0:
                            _th_counter += counter_d2 // 3
                            counter_d2 = counter_d2 % 3
                        elif counter_d2 // 2 != 0:
                            _t_counter += counter_d2 // 2
                            counter_d2 = counter_d2 % 2
                        else:
                            break
                    counter_d2 = 0
    return _f_counter * fourh_W + _th_counter * third_W+ _t_counter * twos_W


if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]
    ai_card = 2

    print(h(board, ai_card))
