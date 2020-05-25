def secret_formula(started):
    apple = started * 500
    banana = apple / 1000
    cat = banana / 100
    return apple, banana, cat

start_point = 1000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of {}".format(start_point))
print(f"We have {beans}beans, {jars}jars and {crates}crates!")

formula = secret_formula(start_point)
print("WE have {}beans, {}jars and {}crates!".format(*formula))
