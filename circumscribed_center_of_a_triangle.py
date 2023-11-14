def circumcenter(a,b,c):
    #Намираме медианите на триъгълникът
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

#Буум
a = (4, 5)
b = (7, 8)
c = (9, 11)

circumcenter_point = circumcenter(a,b,c)
print("Circumcenter coordinates: ", circumcenter_point)
