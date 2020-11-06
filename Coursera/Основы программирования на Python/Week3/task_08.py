a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
if a != 0:
    y = (a * f - c * e) / (a * d - c * b)
    x = (e - b * y) / a
elif a == 0:
    y = e / b
    x = (f - d * y) / c
print(x, y)
