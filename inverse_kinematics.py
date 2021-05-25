import math

def get_angles(position, lengths, cell_size, border):
    y, x = position
    angles = [0] * (len(lengths) + 1)
    angles[0] = math.atan2((y-3.5)*cell_size, border+(x+0.5)*cell_size)
    angles = [math.degrees(i) for i in angles]
    return angles
print(get_angles((7, 7), [], 27.5, 15))