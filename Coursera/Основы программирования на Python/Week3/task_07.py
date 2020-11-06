a, b, c = float(input()), float(input()), float(input())
D = b**2 - 4 * a * c
x1 = (-b + D**0.5) / (2 * a)
x2 = (-b - D**0.5) / (2 * a)
if D == 0:
    print(x1)
elif D > 0:
    print(x1, x2) if x1 < x2 else print(x2, x1)
