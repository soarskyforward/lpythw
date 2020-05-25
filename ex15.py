from sys import argv

script, filename = argv

print("Alright, let's be fun!")

txt = open(filename)
print(f"Here are your file {filename}.")
print(txt.read())

print("Type your file again please.")
file_again = input()

txt_again = open(file_again)
print(txt_again.read())
