# Searches for the target in an unsorted array
# Returns index of the target if it exists in the data else returns -1
def linear_search(data, target):
    for index, each in enumerate(data):
        if each == target:
            return index
    return -1


# Searches for the target in a binary search tree (sorted array)
# Returns index of the target if it exists in the data else returns -1
def binary_search(data, target):
    low = 0
    high = len(data) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if data[mid] < target:
            low = mid + 1
        elif data[mid] > target:
            high = mid - 1
        else:
            return mid

    return -1
