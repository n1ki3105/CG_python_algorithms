def dot_on_line(x, y, x1, y1, x2, y2):
    cross_product = (y - y1) * (x2 - x1) - (x - x1) * (y2 - y1)
    epsilon = 1e-10
    return abs(cross_product) < epsilon

def dot_on_contour(dot, polygon):
    x, y = dot
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]
        #Проверяваме дали точката е на контура
        if dot_on_line(x, y, x1, y1, x2, y2):
            return True
    return False

#Буум
polygon = [(4, 5), (6, 7), (8, 9), (11, 2), (3, 14), (5, 6), (9, 4)]
dots = [(4, 5), (5, 7), (55, 44)]

for i in range(0, len(dots)):
    if dot_on_contour(dots[i], polygon):
        print(f"Dot {dots[i]} is on the countour.")
    else:
        print(f"Dot {dots[i]} is not on the countour.")
