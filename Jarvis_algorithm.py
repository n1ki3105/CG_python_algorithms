def jarvis_algorithm(dots):
    def orientation(a, b, c):
        #Намираме ориентацията на abc. Колинеарни точки, ако е 0. По часовниковата стрелка, ако е 1. Обратно на часовниковата стрелка, ако е -1
        val = (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])
        if val == 0:
            return 0
        return 1 if val > 0 else -1

    #Намираме точката, най-близо до долният ляв ъгъл
    first_dot = min(dots, key=lambda dot: (dot[1], dot[0]))

    #Започваме да чертаем обвивката, като избираме първата точка
    wrap = [first_dot]

    while True:
        #Избираме точката, с най-малък ъгъл
        last_point = dots[0]
        for point in dots[1:]:
            if point == wrap[-1]:
                continue
            if (last_point == wrap[-1]) or (orientation(wrap[-1], last_point, point) == -1):
                last_point = point
        #Ако последната точка е равна на първата точка, приключваме алгоритъма
        if last_point == first_dot:
            break
        #Добавяме последната точка в обвивката
        wrap.append(last_point)
    return wrap

#Буум
dots = [(4, 5), (6, 7), (8, 9), (11, 2), (3, 14), (5, 6), (9, 4)]
wrap = jarvis_algorithm(dots)
print("Wrap coordinates: ", wrap)
