# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
from Algorithms import minimax_algorithm
if __name__ == '__main__':
    board = [[0, 1, 2, 2, 1, 2, 2],
             [1, 1, 2, 1, 1, 1, 2],
             [1, 2, 2, 1, 1, 2, 2],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 2, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 2, 2]]
    depth = 5
    AI_start = True
    _val = minimax_algorithm(board , depth , AI_start)
    print(_val)

