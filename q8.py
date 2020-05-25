for i in range(1, 10):
    for j in range(1, 10):
        print(i, "x", j, "=", i*j, "\t", end = "")
        if i == j:
            print("")
            break

# 输出 9*9 乘法口诀表。
