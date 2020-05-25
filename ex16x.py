from sys import argv

script, filename = argv

print(f"Hi, we're going to open the {filename}")
print("If you want to erase the file, hit enter.\nIf you don't want do that , hit ctrl+c.")

input("?")

target = open(filename, 'w')

print("Truncating the file ...")

target.truncate()
#there're nothing in the ()....

print("It is the time, please tell me three lines of your mind")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

nl = '\n'
target.write(line1 + nl + line2 + nl +line3)

print("Alright, goodbye...")
