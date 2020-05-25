a, b, i = 0, 1, 0
result = [ ]
n = int(input('输入一个大于 0 的整数: '))
while i < n:
    result.append(b)
    a, b = b, a+b
    i += 1
print(result[n-1])
