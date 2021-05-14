import cv2
import numpy as np
from time import sleep
from collections import Counter

image = cv2.imread('example.jpg')
size = 100
small = cv2.resize(image, (size, size))
rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

lower_range = np.array([150,0, 0])
upper_range = np.array([255, 120, 120])

mask = cv2.inRange(rgb, lower_range, upper_range)

top, bottom, left, right = [None] * 4
cap = size * 0.4

for index, row in enumerate(mask):
    if Counter(row)[255] >= cap:
        top = index
    elif top is not None:
        break

for index, col in enumerate(mask.transpose()):
    if Counter(col)[255] >= cap:
        left = index
    elif left is not None:
        break

for index, row in enumerate(mask[::-1]):
    if Counter(row)[255] >= cap:
        bottom = size - index - 1
    elif bottom is not None:
        break

for index, col in enumerate(mask.transpose()[::-1]):
    if Counter(col)[255] >= cap:
        right = size - index - 1
    elif right is not None:
        break
small = cv2.rectangle(small, (left, top), (right, bottom), (255, 0, 0))

b_lower_range = np.array([0, 0, 0])
b_upper_range = np.array([50, 50, 50])

black_piece_mask = cv2.inRange(rgb, b_lower_range, b_upper_range)

w_lower_range = np.array([180, 180, 230])
w_upper_range = np.array([[255] * 3])
white_piece_mask = cv2.inRange(rgb, w_lower_range, w_upper_range)

board = np.array([[0] * 8] * 8)
v_range = (bottom - top)/8
h_range = (right - left)/8
cap = v_range * h_range * 0.3
for row in range(8):
    for col in range(8):
        square = black_piece_mask[int(top+v_range*row):int(top+v_range*(row+1)),
                 int(left+h_range*col):int(left+h_range*(col+1))].flatten()
        if Counter(square)[255] > cap:
            board[row, col] = -1
        square = white_piece_mask[int(top + v_range * row):int(top + v_range * (row + 1)),
                 int(left + h_range * col):int(left + h_range * (col + 1))].flatten()
        if Counter(square)[255] > cap:
            board[row, col] = 1

text = '+---' * 8 + '+\n'
for row in board:
    text += '|'
    for col in row:
        text += f' {"O" if col == 1 else "X" if col == -1 else " "} |'
    text += '\n' + '+---' * 8 + '+\n'
text = text[:-1]

print(text)

# cv2.imshow('border', black_piece_mask)
# cv2.imshow('image', small)
#
# c = cv2.waitKey(0)
# if c == 'q':
#     cv2.destroyAllWindows()