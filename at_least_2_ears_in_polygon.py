def angle(a,b,c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    def orientation(a, b, c):
        #Намираме ориентацията на abc. Колинеарни точки, ако е 0. По часовниковата стрелка, ако е 1. Обратно на часовниковата стрелка, ако е -1
        val = (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])
        if val == 0:
            return 0
        return 1 if val > 0 else -1
    
def dot_inside_triangle(dot, v1, v2, v3):
    x, y = dot
    x1, y1 = v1
    x2, y2 = v2
    x3, y3 = v3
    #Барицентрични координати (a,b,c - ъгли)
    z=(y2-y3)*(x1-x3)+(x3-x2)*(y1-y3)
    a=((y2-y3)*(x-x3)+(x3-x2)*(y-y3))/z
    b=((y3-y1)*(x-x3)+(x1-x3)*(y-y3))/z
    c=1-a-b
    #Проверяваме дали точката е в триъгълникът
    return 0<=a<=1 and 0<=b<=1 and 0<=c<=1

def ear(polygon, i):
    a = polygon[(i - 1) % len(polygon)]
    b = polygon[i]
    c = polygon[(i + 1) % len(polygon)]
    #Проверяваме дали ъгълът е изпъкнал
    if angle(a, b, c) != -1:
        #Проверяваме дали други върхове са в триъгълникът abc
        for j in range(len(polygon)):
            if j != i and j != (i - 1) % len(polygon) and j != (i + 1) % len(polygon):
                dot = polygon[j]
                if dot_inside_triangle(dot, a, b, c):
                    return False
        return True
    return False

def ears(polygon):
    ears = []
    while len(polygon) > 3:
        for i in range(len(polygon)):
            if ear(polygon, i):
                ears.append((polygon[(i - 1) % len(polygon)], polygon[i], polygon[(i + 1) % len(polygon)]))
                polygon.pop(i)
                break
    return ears

#Буум
polygon = [(4, 5), (6, 7), (8, 9), (11, 2)]
ear_triangles = ears(polygon)

print("Ears coordinates: ")
for ear in ear_triangles:
    print(ear)
