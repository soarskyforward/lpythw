def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if smallest > arr[i]:
            smallest_index = i
            smallest = arr[i]
    return smallest_index

def selectionsort(arr):
    newarr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr

print(selectionsort([3,76,56,34,3,23]))

# 选择排序     O（n*2）
