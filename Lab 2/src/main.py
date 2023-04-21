from graph import plot_graph
from insertion_sort import insertion_sort
from merge_sort import merge_sort

if __name__ == "__main__":
    array = [4, 6, 1, 7, 2, 9, 3]
    print("Array before insertion sort:", array)
    insertion_sort(array)
    print("Array after insertion sort:", array)

    array = [4, 6, 1, 7, 2, 9, 3]
    print("Array before merge sort:", array)
    merge_sort(array, 0, len(array) - 1)
    print("Array after merge sort:", array)
    plot_graph()
