for n in range (100, 1000):
    i = n // 100
    j = (n - i * 100) //10
    k = n - i * 100 - j * 10
    if n == i **3 + j ** 3 + k ** 3:
        print(n)


for n in range(100, 1000):
    s = str(n)
    if int(s[0]) ** 3 + int(s[1]) **3 + int(s[2])**3 == n:
        print(n)

# pow() 方法返回 xy（x的y次方） 的值。

for x in range(1, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            s1 = x *100 + y *10 + z *1
            s2 = pow(x, 3) + pow(y, 3) + pow(z, 3)
            if s1 == s2:
                print(s1)
