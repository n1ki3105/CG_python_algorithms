def orientation(a, b, c):
    #Намираме ориентацията на abc. Колинеарни точки, ако е 0. По часовниковата стрелка, ако е 1. Обратно на часовниковата стрелка, ако е -1
    val = (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1

def convex_peak(a,b,c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    result = orientation(a,b,c)
    if result == 1:
        return True
    elif result == -1:
        return False
    else:
        return True

#Буум
polygon = [(4, 5), (6, 7), (8, 9), (11, 2), (3, 14), (5, 6), (9, 4)]

#Проверяваме за всеки връх
for i in range(len(polygon)):
    a = polygon[(i - 1) % len(polygon)]
    b = polygon[i]
    c = polygon[(i + 1) % len(polygon)]
    if convex_peak(a,b,c):
        print(f"Peak {b} is convex.")
    else:
        print(f"Peak {b} is concave.")
