from math import *
a = 0.5
b = 0.7
x1 = 0
xn = 5
dx = 0.5
y = 0
x = x1

for x in range(x1, xn + 1):
    y = sin(a * x) + 3 * pow(cos(b * (x ** 2) + 1), 2)
    print(y)
    print(x)
    if type(x) == float:
        x += dx

print(x)
print(y)