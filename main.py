from get_board import *
"""prints board every time the board state changes"""

vid = cv2.VideoCapture(0)

board = None
past_boards = []

while True:
    _, image = vid.read()

    #change board if the board is consistent for 5 consecutive frames
    temp_board = get(image)
    if (temp_board is not None) and temp_board != board:
        past_boards.append(temp_board)
        if len(past_boards) > 5:
            past_boards.pop(0)
        if past_boards.count(temp_board) == 5:
            board = temp_board
            cv2.imshow('board', cv2.resize(image, (100, 100)))
            print(board_to_text(board))

    cv2.imshow("window", image)
    c = cv2.waitKey(1)
    if c == 'q':
        break
cv2.destroyAllWindows()

