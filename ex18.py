#Function time
def print_two(*argv):
    argv1, argv2 = argv
    print(f"argv1: {argv1}, argv2: {argv2}.")

def print_two_again(arg1, argv2):
    print(f"argv1: {arg1}, argv2: {argv2}.")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin")

print_two(1, 2)
print_two_again("wei", "chong")
print_one("first")
print_none()

#run = use = call
