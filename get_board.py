import cv2
import numpy as np
from time import sleep
from collections import Counter

def get(file):
    """gets the board state given filename or image"""

    #load image and resize it so it is easier to work with
    image = cv2.imread(file) if type(file) == str else file
    size = 100
    small = cv2.resize(image, (size, size))
    rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

    #mask for the boarder
    lower_range = np.array([150,0, 0])
    upper_range = np.array([255, 120, 120])
    mask = cv2.inRange(rgb, lower_range, upper_range)

    #find the rectangle of board
    boundaries = [None] * 4
    cap = size * 0.4
    for index, side in enumerate([mask, mask.transpose(), mask[::-1], mask.transpose()[::-1]]):
        for index2, row in enumerate(side):
            if Counter(row)[255] >= cap:
                boundaries[index] = size - index2 if index >= 2 else index2
            elif boundaries[index] is not None:
                break
        else:
            return None
    top, left, bottom, right = boundaries

    if abs(top - bottom) < 10 or abs(left - right) < 10:
        return None

    #mask for white and black pieces
    b_lower_range = np.array([0]*3)
    b_upper_range = np.array([60]*3)
    black_piece_mask = cv2.inRange(rgb, b_lower_range, b_upper_range)
    w_lower_range = np.array([180]*3)
    w_upper_range = np.array([[255] * 3])
    white_piece_mask = cv2.inRange(rgb, w_lower_range, w_upper_range)

    #detect the piece in each cell
    board = np.zeros((8, 8))
    v_range = (bottom - top)/8
    h_range = (right - left)/8
    cap = v_range * h_range * 0.2
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                continue
            square = black_piece_mask[int(top+v_range*row):int(top+v_range*(row+1)),
                     int(left+h_range*col):int(left+h_range*(col+1))].flatten()
            if Counter(square)[255] > cap:
                board[row, col] = -1
            square = white_piece_mask[int(top + v_range * row):int(top + v_range * (row + 1)),
                     int(left + h_range * col):int(left + h_range * (col + 1))].flatten()
            if Counter(square)[255] > cap:
                board[row, col] = 1
    return board.tolist()

def board_to_text(board):
    """returns a string that represents the board given"""

    text = '+---' * 8 + '+\n'
    for row in board:
        text += '|'
        for col in row:
            text += f' {"O" if col == 1 else "X" if col == -1 else " "} |'
        text += '\n' + '+---' * 8 + '+\n'
    text = text[:-1]
    return text
