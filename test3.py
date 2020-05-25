for n in range(2, 1000):
    for x in range(2, n):
        if n % x == 0:
            print(n, "是合数")
            break
    else:
        print(n, "是质数")
