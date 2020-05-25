
n = int(input("Your number>"))

def flb(n):
    a, b = 0, 1
    while n:
        a, b, n = b, a+b, n-1
        print(a , end = " ")
    return a

flb(n)
