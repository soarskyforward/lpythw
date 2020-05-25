from sys import argv

script, filename = argv

print(f"We are going to erase the {filename}")
print("If you don't want do that, hit ctrl-C")
print("If you want do that , hit ENTER.")

input("?")

print("Opening the file...")

target = open(filename, 'w')

print("Truncating the file. Good bye")

target.truncate()

print("Now I want to ask for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

nl = '\n'
target.write(line1 + nl + line2 + nl + line3)
target = open(filename)
print(target.read())

print("It's the last time, my friend, goodbye.")
target.close()
