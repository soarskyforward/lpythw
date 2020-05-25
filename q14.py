n = int(input("Input your number: "))
n1 = n
temp = []



while n != 1:
    for i in range(2, n +1):
        if n % i == 0:
            temp.append(str(i))
            n = n // i
            # 'float' object cannot be interpreted as an integer  / change into //
            break


print(n1 , "=","*".join(temp))
