import math

def equation(a, b, c, j):
    return b + a * math.sqrt(1-(c * math.sin(j) / a)**2) + c * math.cos(j)

def get_angles(position, lengths, cell_size, border):
    y, x = position
    a, b, c = lengths
    bottom = math.atan2((y-3.5)*cell_size, border+(x+0.5)*cell_size)

    distance = math.sqrt(((y-3.5)*cell_size)**2 + (border+(x+0.5)*cell_size)**2)
    j = 0
    while abs(equation(a, b, c, j) - distance) > 1:
        j += 0.01
    k = math.asin(c * math.sin(j) / a)
    bottom, j, k = [(math.degrees(i)+180) % 360 - 180 for i in [bottom, j, k]]

    return [bottom, j, 180 - j, 180 - k]
a, b, c = 168, 95, 109
border = 15
cell_size = 27.5
y, x = 4, 7
angles = get_angles((y, x), [a, b, c], cell_size, border)
print(angles)

print(math.cos(math.radians(angles[1])) * c + b + math.cos(math.radians(180-angles[-1])) * a)
print(math.sqrt(((y-3.5)*cell_size)**2 + (border+(x+0.5)*cell_size)**2))