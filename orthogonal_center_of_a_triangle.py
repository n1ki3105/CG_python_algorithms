def orthocenter(a,b,c):
    slope_ab=-1/((b[1]-a[1])/(b[0]-a[0])) if b[0]!=a[0] else float('inf')
    slope_bc=-1/((c[1]-b[1])/(c[0]-b[0])) if c[0]!=b[0] else float('inf')
    slope_ca=-1/((a[1]-c[1])/(a[0]-c[0])) if a[0]!=c[0] else float('inf')

    mid_ab=((a[0]+b[0])/2,(a[1]+b[1])/2)
    mid_bc=((b[0]+c[0])/2,(b[1]+c[1])/2)
    mid_ca=((c[0]+a[0])/2,(c[1]+a[1])/2)

    #Намираме височините
    intercept_ab=mid_ab[1]-slope_ab*mid_ab[0] if slope_ab!=float('inf') else float('inf')
    intercept_bc=mid_bc[1]-slope_bc*mid_bc[0] if slope_bc!=float('inf') else float('inf')
    intercept_ca=mid_ca[1]-slope_ca*mid_ca[0] if slope_ca!=float('inf') else float('inf')

    #Намираме координатите на ортоцентърът
    x=(intercept_ab-intercept_bc)/(slope_bc-slope_ab) if slope_ab!=slope_bc else float('inf')
    y=slope_ab*x+intercept_ab if slope_ab!=float('inf') else intercept_bc
    return x, y

# Example usage
point_a = (44, 35)
point_b = (67, 88)
point_c = (44, 55)

orthocenter = orthocenter(point_a, point_b, point_c)
print("Orthocenter coordinates: ", orthocenter)
