from graph import plot_graph
from search import linear_search, binary_search

if __name__ == "__main__":
    # 1
    print(f"Index of 2 in given list is {linear_search([1, 5, 3, 2, 7], 2)}")
    print(
        f"Index of 5 in given list is {binary_search([1, 2, 3, 4, 5, 6, 7], 5)}")

    # 3
    plot_graph()
