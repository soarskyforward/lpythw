file_name = 'programming.txt'

with open(file_name, 'a') as file_object:
    file_object.write("I love you.\n")

file = open(file_name)
print(file.read())
