l = []

for i in range(101,200):
    for j in range(2, i-1):
        if i%j == 0:
            break
    else:
        l.append(i)

for k in l:
    print(k, end = " ")

print("\n",len(l), "in total")


# 判断101-200之间有多少个素数，并输出所有素数。