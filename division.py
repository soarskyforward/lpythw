print("Give me two numbers, and I will divide them.")
print("Entere 'q' to quit.")

while True:
    first_number = input("What's your first number?>")
    if first_number == 'q':
        break
    second_number = input("What's your second number?>")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
