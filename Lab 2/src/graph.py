from matplotlib import pyplot as plt
import time
from insertion_sort import insertion_sort
from merge_sort import merge_sort
import numpy as np
import matplotlib.ticker as ticker


def graph_data(best_case, is_insertion):
    data = {
        "input_size": [],
        "exec_time": [],
    }
    for value in range(1000, 10000, 1000):
        input = np.arange(
            1, value + 1) if best_case else np.arange(value, 0, -1)
        data["input_size"].append(len(input))
        start_time = time.time()
        insertion_sort(input) if is_insertion else merge_sort(
            input, 0, len(input)-1)
        data["exec_time"].append((time.time() - start_time) * 1000)

    return data


def plot(ax, best_case, is_insertion):
    title = "Ascending Data" if best_case else "Descending Data"
    title += " Insertion Sort" if is_insertion else " Merge Sort"
    data = graph_data(best_case, is_insertion)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%d ms'))
    ax.plot(data["input_size"],
            data["exec_time"])
    ax.set_title(title)


def plot_graph():
    fig, axes = plt.subplots(2, 2)
    plot(axes[0, 0], best_case=True, is_insertion=True)
    plot(axes[0, 1], best_case=False, is_insertion=True)
    plot(axes[1, 0], best_case=True, is_insertion=False)
    plot(axes[1, 1], best_case=False, is_insertion=False)
    plt.tight_layout()
    plt.show()
