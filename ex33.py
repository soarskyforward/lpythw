i = 0
number = []

while i < 6:
    print(f"At the top is {i}")
    number.append(i)

    i += 1
    print("Numbers now:", number)
    print(f"At the bottom is {i}")

print("The numbers:")

for num in number:
    print(num)
