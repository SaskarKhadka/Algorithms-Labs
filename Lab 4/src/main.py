from knapsack import zeroone_knapsack_brute_force, zeroone_knapsack_dynamic_prog, fractional_knapsack_brute_force, fractional_knapsack_greedy
from item import get_items
from bubble_sort import bubble_sort

if __name__ == "__main__":
    items = get_items()
    solution, max_value = zeroone_knapsack_brute_force(items, 100)

    print("For 0/1 knapsack")
    for item in solution:
        print(item.name, item.weight, item.value)
    print(f"Max Profit: {max_value}\n")

    items = get_items()
    solution, max_value = fractional_knapsack_brute_force(items, 100)
    print("For Fractional knapsack")
    for item in solution:
        print(item.name, item.weight, item.value)
    print(f"Max Profit: {max_value}\n")

    items = get_items()
    solution, max_value = fractional_knapsack_greedy(items, 100)
    print("For Fractional knapsack greedy")
    for item in solution:
        print(item.name, item.weight, item.value)
    print(f"Max Value: {max_value}\n")

    items = get_items()
    max_value = zeroone_knapsack_dynamic_prog(items, 100)
    print("For 0/1 knapsack dynamic programming")
    print(f"Max Value: {max_value}\n")
