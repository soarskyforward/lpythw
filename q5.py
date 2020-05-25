l = []

for i in range(3):
    #变量也可由用户决定input
    x = int(input("Your number:"))
    l.append(x)

l.sort()

for val in l:
    print(val, end = ' ')

#想要在一行打印就输入end = ' '就行了
