import math

print("let's do the ax*2+bx+c=0")
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4 * a * c))/(2*a)
    x2 = (-b - math.sqrt(b**2 - 4 * a * c))/(2*a)
    print("x1:", x1, "x2:", x2)
    return x1, x2

quadratic(a,b,c)
