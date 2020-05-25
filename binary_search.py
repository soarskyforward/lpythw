def binary_search(list,item):
    low = 0
    high = len(list)-1
    n = 0
    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        print(guess)
        n += 1
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        else:
            return 'Guess frequency:' + str(n), list[mid]
    return None

my_list = [x for x in range(100)]

print(binary_search(my_list, 1))

print(binary_search(my_list, 49))


#二分法    O(log n)
