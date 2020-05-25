p = int(input("what?  "))

def flb(n):
    a, b = 0, 1
    while n:
        a, b, n = b, a+b, n-1
        print(a, end = " ")
    return a
#函数中没有return的话默认就是返回none


print(flb(p))
