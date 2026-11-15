def greedy_algorithm(items: dict, budget: int) -> list:
    """
    Select dishes with the highest calories-to-cost ratio
    first.
    """
    if budget < 0:
        raise ValueError("Budget cannot be negative.")

    # Sort dishes by calories per cost.
    sorted_items = sorted(items.items(), key=get_ratio, reverse=True)

    result = []
    for name, item in sorted_items:
        # Skip dishes that cost more than the remaining budget.
        if item["cost"] > budget:
            continue

        result.append(name)
        budget -= item["cost"]

    return result

def get_ratio(item: tuple) -> float:
    """
    Return the calories-to-cost ratio.
    """
    name, details = item
    return details["calories"] / details["cost"]
