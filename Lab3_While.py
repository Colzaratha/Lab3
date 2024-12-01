from math import *
a = 0.5
b = 0.7
x1 = 0
xn = 5
dx = 0.5
x = x1

while x <= xn:
    y = sin(a * x) + 3 * pow(cos(b * (x ** 2) + 1), 2)
    print(y)
    print(x)
    x += dx
    if x == 5:
        y = sin(a * x) + 3 * pow(cos(b * (x ** 2) + 1), 2)
        break

print(x)
print(y)
