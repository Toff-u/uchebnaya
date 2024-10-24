import sys
sys.set_int_max_str_digits(100000)

def tetr(tet,ch):
    s = 1
    for i in range(tet):
        s = ch ** s
    return len(str(s))
print(tetr(3,5))
print(tetr(5,2))