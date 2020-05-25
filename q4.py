p = [31,28,31,30,31,30,31,31,30,31,30,31] # 平年
w = [31,29,31,30,31,30,31,31,30,31,30,31] # 闰年

year = int(input("Year:"))
month = int(input("month:"))

if month > 12:
    print("Wrong!")

day = int(input("Day:"))

if month == 1 and 3 and 5 and 7 and 8 and 10 and 12:
    if day > 31:
        print("Wrong!")
elif month == 2:
    if day > 29:
        print("Wrong!")
else:
    if day > 30:
        print("Wrong day!")

sum = day

if year % 4 == 0:
    for i in range(0, month - 1):
        sum += w[i]
elif year % 4 != 0 :
    for i in range(0, month - 1):
        sum = sum + p[i]
else:
    print("Please type the corret date.")

print("It is the", sum, "th day.")
