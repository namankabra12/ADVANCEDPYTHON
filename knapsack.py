def solve_top_down(index, remaining_capacity, weights, values, memo):
    if index == len(weights) or remaining_capacity == 0:
        return 0

    key = (index, remaining_capacity)
    if key in memo:
        return memo[key]

    value_without_item = solve_top_down(index + 1, remaining_capacity, weights, values, memo)

    value_with_item = 0
    if weights[index] <= remaining_capacity:
        value_with_item = values[index] + solve_top_down(
            index + 1, remaining_capacity - weights[index], weights, values, memo
        )

    best = max(value_without_item, value_with_item)

    memo[key] = best
    return best


def knapsack_top_down(weights, values, capacity):
    memo = {}
    return solve_top_down(0, capacity, weights, values, memo)


def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    table = []
    for i in range(n + 1):
        row = [0] * (capacity + 1)
        table.append(row)

    for i in range(1, n + 1):
        current_weight = weights[i - 1]
        current_value = values[i - 1]

        for w in range(capacity + 1):
            table[i][w] = table[i - 1][w]

            if current_weight <= w:
                value_if_taken = current_value + table[i - 1][w - current_weight]
                if value_if_taken > table[i][w]:
                    table[i][w] = value_if_taken

    return table[n][capacity]


def main():
    n = int(input("How many items do you have? "))

    weights = []
    values = []

    for i in range(n):
        w = int(input("Enter weight of item " + str(i + 1) + ": "))
        v = int(input("Enter value of item " + str(i + 1) + ": "))
        weights.append(w)
        values.append(v)

    capacity = int(input("Enter the knapsack capacity: "))

    result1 = knapsack_top_down(weights, values, capacity)
    result2 = knapsack_bottom_up(weights, values, capacity)

    print("\nMax value (top-down method):", result1)
    print("Max value (bottom-up method):", result2)


main()