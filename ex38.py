ten_things = "Apples oranges crows telephones light sugar"

print("Wait, there are not ten things in that list.Let's fix that")

stuff = ten_things.split(' ')
more_stuff = ["hero", "gundam", "pc", "model", "pills"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"Now, there are {len(stuff)} now")
#                      not len({stuff})


print("There we go:", stuff)

print("Let's do some things with the stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[2:5]))
