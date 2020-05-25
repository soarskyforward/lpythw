def rabbit(n):
    f1 = 1
    f2 = 1
    while n:
        f1, f2, n = f2, f1 + f2, n-1
        print(f1, end = " ")
    return f1

print(rabbit(100))


"""古典问题：有一对兔子，
从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？ """
