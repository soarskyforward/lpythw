the_count = [1, 2, 3, 4]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = ['apple', 'pen', 'applepen']

for fruit in fruits:
    print(f"This is the {fruit}")

for number in the_count:
    print("This is count {}".format(number))

for i in change:
    print(f"I got a {i}")

element = []
for i in range(0, 6):
    print(f"Add {i} to the new list.")
    element.append(i)

for i in element:
    print(f"Element is {i}")
