import matplotlib.pyplot as plt
import time
from search import linear_search, binary_search
import numpy as np


# Generates random input and calculates the corresponding execution
# time for linear and binary search algorithms
def search_data(bestCase: bool):
    data = {
        "linear_input_size": [],
        "linear_exec_time": [],
        "binary_input_size": [],
        "binary_exec_time": [],
    }
    for size in range(10000, 100000, 10000):
        test_data = np.arange(size+1)

        # For linear search, best case = first data and worst case = invalid data
        data["linear_input_size"].append(size)
        start_time = time.time()
        result = linear_search(test_data, 0 if bestCase else size + 1)
        data["linear_exec_time"].append((time.time() - start_time) * 1000)

        # For binary search, best case = middle data and worst case = invalid data
        data["binary_input_size"].append(size)
        start_time = time.time()
        result = binary_search(
            test_data, (len(test_data) - 1) // 2 if bestCase else size + 1)
        data["binary_exec_time"].append((time.time() - start_time) * 1000)

    return data


# Plots input size vs. execution time for best case and worst cases
def plot(ax, bestCase):
    title = "Best Case" if bestCase else "Worst Case"
    data = search_data(bestCase)

    ax.plot(data["binary_input_size"],
            data["binary_exec_time"], label="Binary Search")

    ax.plot(data["linear_input_size"],
            data["linear_exec_time"], label="Linear Search", alpha=0.7, linestyle="dashed")

    ax.set_xlabel("Input Size")
    ax.set_ylabel("Execution Time")

    ax.set_title(title)
    ax.legend()


def plot_graph():
    fig, (ax1, ax2) = plt.subplots(2)
    plot(ax1, bestCase=True)
    plot(ax2, bestCase=False)
    fig.tight_layout()
    plt.show()
