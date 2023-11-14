def circumcenter_convex_polygon(a,b,c):
    #Намираме средата на всяка отсечка
    midpoint_ab=((a[0]+b[0])/2,(a[1]+b[1])/2)
    midpoint_bc=((b[0]+c[0])/2,(b[1]+c[1])/2)
    #Намираме ъглополовящите
    bisector_ab=-(b[0]-a[0])/(b[1]-a[1]) if b[1]!=a[1] else float('inf')
    bisector_bc=-(c[0]-b[0])/(c[1]-b[1]) if c[1]!=b[1] else float('inf')
    #Проверяваме дали ъглополовящите са равни
    if bisector_ab != bisector_bc:
        #Намираме координатите на центъра на описаната окръжност
        x=(bisector_ab*bisector_bc*(midpoint_bc[1]-midpoint_ab[1])+bisector_ab*(midpoint_bc[0]+midpoint_ab[0])-bisector_bc*(midpoint_ab[0]+midpoint_bc[0]))/(2*(bisector_ab-bisector_bc))
        y=-1*(x-(midpoint_ab[0]+midpoint_bc[0])/2)/bisector_ab+(midpoint_ab[1]+midpoint_bc[1])/2
        return x, y
    else:
        #Точките са колинеарни
        return midpoint_ab

def circumscribed_circle_convex_polygon(polygon):
    circumcenter = circumcenter_convex_polygon(polygon[-1], polygon[0], polygon[1])
    for i in range(1, len(polygon) - 1):
        current_circumcenter = circumcenter_convex_polygon(polygon[i - 1], polygon[i], polygon[i + 1])
        if (current_circumcenter[0]-circumcenter[0])**2+(current_circumcenter[1]-circumcenter[1])**2>0:
            circumcenter = current_circumcenter
    return circumcenter

#Буум
polygon = [(4, 5), (6, 7), (8, 9), (11, 2), (3, 14), (5, 6), (9, 4)]
circumcenter = circumscribed_circle_convex_polygon(polygon)
print("Circumcenter coordinates:", circumcenter)
