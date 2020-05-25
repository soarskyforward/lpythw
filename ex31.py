from sys import argv
script, filename = argv

print("""You are a hero, maybe you should save the world or destroy everything.
Make you decision, remember, follow your heart.""")

decision_1 = input("1 : save world\n2 : destroy world\n")

if decision_1 == "1":
    print("Now, let's sailing!")
if decision_1 == "2":
    print("Alright, you are a devil.Let's change the world!")

file = open(filename)
print(file.read())

print("1: kill youself\n2: go hell the world!\n")
decision_2 = input("???\n")

if decision_2 == "1":
    print("HAHA, you are a really hero, but nothing change...")
elif decision_2 == "2":
    print("This is ten size chaos!!!")
