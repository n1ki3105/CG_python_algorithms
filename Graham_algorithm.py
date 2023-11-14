import math

def graham_algorithm(dots):
    def orientation(a, b, c):
        #Намираме ориентацията на abc. Колинеарни точки, ако е 0. По часовниковата стрелка, ако е 1. Обратно на часовниковата стрелка, ако е -1
        val = (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])
        if val == 0:
            return 0
        return 1 if val > 0 else -1
    
    #Намираме точката, най-близо до долният ляв ъгъл
    first_dot = min(dots, key=lambda dot: (dot[1], dot[0]))
    
    def graham_compare(x,y):
        #Сравняваме точките
        z = orientation(first_dot,x,y)
        if x == 0:
            #Ако са колинеарни избираме тази, която е най-близко до първата
            return (x[0]-first_dot[0])**2+(x[1]-first_dot[1])**2-((y[0]-first_dot[0])**2+(y[1]-first_dot[1])**2)
        return x

    #Проверяваме дали точките са повече от 3, за да се получи обвивка
    if len(dots) < 3:
        return dots

    #Подреждаме точките спрямо първата точка
    sorted_dots = sorted(dots, key=lambda dot: (math.atan2(dot[1]-first_dot[1], dot[0]-first_dot[0]), dot))

    #Започваме да чертаем обвивката, като избираме първата точка и следващите 2
    wrap = [first_dot, sorted_dots[0], sorted_dots[1]]

    #Минаваме през всички точки и изчертаваме обвивката
    for i in range(2, len(sorted_dots)):
        while orientation(wrap[-2], wrap[-1], sorted_dots[i]) != -1:
            wrap.pop()
        wrap.append(sorted_dots[i])
    return wrap

#Буум
dots = [(4, 5), (6, 7), (8, 9), (11, 2), (3, 14), (5, 6), (9, 4)]
wrap = graham_algorithm(dots)
print("Wrap coordinates: ", wrap)
