def dynamic_programming(items: dict, budget: int) -> list[str]:
    """
    Find the highest total calories within the budget.
    """
    if budget < 0:
        raise ValueError("Budget cannot be negative.")

    dishes = list(items.items())
    count = len(dishes)

    # Store the maximum calories for the first i dishes
    # and each available budget.
    max_calories = [[0] * (budget + 1) for _ in range(count + 1)]

    for i in range(1, count + 1):
        name, item = dishes[i - 1]
        cost = item["cost"]
        calories = item["calories"]

        for current_budget in range(budget + 1):
            # Start with the best result without the current dish.
            max_calories[i][current_budget] = max_calories[i - 1][current_budget]

            if cost > current_budget:
                continue

            # Add this dish to the best combination of previous dishes
            # that fits within the remaining budget.
            calories_with_item = (calories + max_calories[i - 1][current_budget - cost])

            # Keep the option with more calories.
            if calories_with_item > max_calories[i][current_budget]:
                max_calories[i][current_budget] = calories_with_item

    result = []
    remaining_budget = budget

    # Find the selected dishes in the table.
    for i in range(count, 0, -1):
        # If the result did not change, this dish was not selected.
        if max_calories[i][remaining_budget] == max_calories[i - 1][remaining_budget]:
            continue

        name, item = dishes[i - 1]
        result.append(name)
        remaining_budget -= item["cost"]

    # Return dishes in their original order.
    result.reverse()
    return result
