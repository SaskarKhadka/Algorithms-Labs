from item import Item
from bubble_sort import bubble_sort


def powerset(items):
    # Returns all the possible combinations of a set including the empty set
    # It maintains the order of data in all of the subsets
    powerset_size = 2**len(items)
    counter = 0
    j = 0

    for counter in range(0, powerset_size):
        results = []
        for j in range(0, len(items)):
            if ((counter & (1 << j)) > 0):
                results.append(items[j])
        yield results


def zeroone_knapsack_brute_force(items, max_capacity):
    # 0/1 Knapsack Problem using Brute Force

    items_powerset = list(powerset(items))

    # Initially set null set as solution
    solution = items_powerset[0]
    max_value = 0

    # check for all the sets in powerset
    for each_set in items_powerset:
        weight = sum([item.weight for item in each_set])
        value = sum([item.value for item in each_set])
        if weight <= max_capacity and value > max_value:
            solution = each_set
            max_value = value
    return solution, max_value


def fractional_knapsack_brute_force(items, max_capacity):
    # Fractional Knapsack Problem using Brute Force

    # sort the items first based on value/weight ratio
    bubble_sort(items)
    items_powerset = list(powerset(items))

    # initially set null set as solution
    solution = items_powerset[0]
    max_value = 0

    # Check for all sets in powerset
    for each_set in items_powerset:
        max_capacity_temp = max_capacity
        set_max_value = 0
        possible_solution = []
        for item in each_set:
            if (max_capacity_temp == 0):
                break
            elif (item.weight > max_capacity_temp):
                value = item.value * max_capacity_temp/item.weight
                possible_solution.append(
                    Item(item.name, max_capacity_temp, value))
                max_capacity_temp = 0
                set_max_value += value
            else:
                possible_solution.append(item)
                set_max_value += item.value
                max_capacity_temp -= item.weight
        # Check if the current set is the best solution until now
        if set_max_value > max_value:
            solution = possible_solution
            max_value = set_max_value
    return solution, max_value


def fractional_knapsack_greedy(items, max_capacity):
    # Fractional Knapsack Problem using Greedy Approach

    # sort the items first based on value/weight ratio
    bubble_sort(items)

    # Here we don't find the powerset. We simply find the solution from the
    # sample set itself after arranging in descending order of weight/value ratio
    solution = []
    max_value = 0
    for item in items:

        if (max_capacity == 0):
            break
        elif (item.weight > max_capacity):
            value = item.value * max_capacity/item.weight
            solution.append(Item(item.name, max_capacity, value))
            max_capacity = 0
            max_value += value
        else:
            solution.append(item)
            max_value += item.value
            max_capacity -= item.weight
    return solution, max_value


def zeroone_knapsack_dynamic_prog(items, max_capacity):
    # 0/1 Knapsack Problem using Dynmaic Programming

    n = len(items)

    # Memoization table
    table = [[0 for _ in range(max_capacity+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, max_capacity+1):
            if items[i-1].weight <= j:
                table[i][j] = max(table[i-1][j], items[i-1].value +
                                  table[i-1][j-items[i-1].weight])
            else:
                table[i][j] = table[i-1][j]
    return table[n][max_capacity]
