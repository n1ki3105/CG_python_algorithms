def andrews_algorithm(dots):
    def orientation(a, b, c):
        #Намираме ориентацията на abc. Колинеарни точки, ако е 0. По часовниковата стрелка, ако е 1. Обратно на часовниковата стрелка, ако е -1
        val = (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])
        if val == 0:
            return 0
        return 1 if val > 0 else -1

    #Подреждаме точките
    sorted_dots = sorted(dots)

    #Дефинираме горна и долна обвивка
    up_wrap = []
    down_wrap = []
    
    #Горна обвивка
    for dot in reversed(sorted_dots):
        while len(up_wrap) >= 2 and orientation(up_wrap[-2], up_wrap[-1], dot) != -1:
            up_wrap.pop()
        up_wrap.append(dot)

    #Долна обвивка
    for dot in sorted_dots:
        while len(down_wrap) >= 2 and orientation(down_wrap[-2], down_wrap[-1], dot) != -1:
            down_wrap.pop()
        down_wrap.append(dot)

    #Цялостна обвивка
    wrap = up_wrap[:-1] + down_wrap[:-1]
    return wrap

#Буум
dots = [(4, 5), (6, 7), (8, 9), (11, 2), (3, 14), (5, 6), (9, 4)]
wrap = andrews_algorithm(dots)
print("Wrap coordinates: ", wrap)
