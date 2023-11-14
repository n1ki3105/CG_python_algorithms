def orientation(a, b, c):
    #Намираме ориентацията на abc. Колинеарни точки, ако е 0. По часовниковата стрелка, ако е 1. Обратно на часовниковата стрелка, ако е -1
    val = (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1

def points_orientation(x, y, line_start, line_end):
    orientation1 = orientation(line_start, line_end, x)
    orientation2 = orientation(line_start, line_end, y)
    if orientation1 == 0 or orientation2 == 0:
        return 0
    elif orientation1 == orientation2:
        return 1
    else:
        return -1

#Буум
line_start = (4, 4)
line_end = (50, 66)
dot1 = (2, 2)
dot2 = (1, 1)

result = points_orientation(dot1, dot2, line_start, line_end)

if result == 0:
    print("Points are on the line.")
elif result == 1:
    print("Points are on the same side of the line.")
else:
    print("Points are on different sides of the line.")
