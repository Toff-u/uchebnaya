def scal(a,b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def vect(a,b):
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
        ]

def scal_sm(a,b,c):
    cr = vect(b,c)
    return scal(a, cr)

def vect_sm(a,b,c):
    cr = vect(b,c)
    return vect(a, cr)

v_a = [1, 2, 3]
v_b = [4, 5, 6]
v_c = [7, 8, 9]

print("скалярное", scal(v_a, v_b))
print("векторное", vect(v_a, v_b))
print("скалярное смешанное", scal_sm(v_a,v_b,v_c))
print("векторное смешанное", vect_sm(v_a,v_b,v_c))