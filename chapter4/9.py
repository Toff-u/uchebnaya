a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))
if (a>b and a>c):
    m = a
if (a<b and b>c):
    m = b
if (c>b and a<c):
    m = c
print(f"m = {m}")
