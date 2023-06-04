def heapify(arr, n, i):
    # Find smallest among root and children
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[smallest][1] > arr[l][1]:
        smallest = l

    if r < n and arr[smallest][1] > arr[r][1]:
        smallest = r

    # If root is not smallest, swap with smallest and continue heapifying
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


def build_max_heap(arr):
    # Build max heap
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)


def heapSort(arr):
    n = len(arr)

    build_max_heap(arr)

    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heapify(arr, i, 0)


def insert(arr, a):
    # n = len(arr)
    arr.append(a)
    build_max_heap(arr)


def pop(arr):
    arr[0], arr[len(arr)-1] = arr[len(arr)-1], arr[0]
    deleted = arr.pop()
    build_max_heap(arr)
    return deleted


def delete(arr, a):
    n = len(arr)
    i = 0
    for i in range(0, n):
        if a == arr[i]:
            break

    arr[i], arr[n-1] = arr[n-1], arr[i]

    arr.pop()

    build_max_heap(arr)


# arr = [(23, 21), (43, 56), (65, 78), (94, 3), (5, 8)]
# heapSort(arr)
# # build_max_heap(arr, len(arr))
# print(arr)
# print(pop(arr))
# # insert(arr, 93)
# # # heapSort(arr)
# print(arr)
# # delete(arr, 78)
# # print(arr)
