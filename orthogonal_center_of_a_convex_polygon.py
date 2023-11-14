def avg_coordinates(peaks):
    ax=sum(x for x, y in peaks)/len(peaks)
    ay=sum(y for x, y in peaks)/len(peaks)
    return ax, ay

def find_closest_peaks(avg_co, peaks):
    return min(peaks, key=lambda vertex: (vertex[0]-avg_co[0])**2+(vertex[1]-avg_co[1])**2)

def find_orthogonal_center(peaks):
    avg_co=avg_coordinates(peaks)
    closest_vertex = find_closest_peaks(avg_co, peaks)
    orthogonal_center = ((avg_co[0]+closest_vertex[0])/2,(avg_co[1]+closest_vertex[1])/2)
    return orthogonal_center

#Буум
polygon = [(4, 5), (6, 7), (8, 9), (11, 2), (3, 14), (5, 6), (9, 4)]

orthogonal_center = find_orthogonal_center(polygon)
print("Orthogonal center coordinates:", orthogonal_center)
