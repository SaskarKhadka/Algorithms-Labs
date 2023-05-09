# sorts items by their value/weight ratio
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j].value/arr[j].weight < arr[j+1].value/arr[j+1].weight:
                arr[j], arr[j+1] = arr[j+1], arr[j]
