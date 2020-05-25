print("It is game time!")

number = 10
guess = 23333333
i = 0

while guess != number:
    guess = int(input("what's your number?"))
    i += 1

    if guess > number:
        print("That is too big!")

    elif guess < number:
        print("That is too small.")

    elif guess == number:
        print("You win !")
        if i < 3:
            print("You are genious!")
        else:
            print("You are so normal...")
