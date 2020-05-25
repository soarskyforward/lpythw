import random

a = 0
while True:
    x = random.choice(range(100))
    y = random.choice(range(100))
    a += 1

    if x > y:
        print("x, '>', y")
    elif x < y:
        print("x, '<', y")
    else:
        print(f"they are similar{x},ttotal cal {a} times.")
        break
