from greedy_algorithm import greedy_algorithm
from dynamic_programming import dynamic_programming


def print_result(title: str, selected_items: list, items: dict) -> None:
    """
    Print selected dishes, their total cost and total calories.
    """
    total_cost = sum(items[name]["cost"] for name in selected_items)
    total_calories = sum(items[name]["calories"] for name in selected_items)

    print(f"{title}: {selected_items}")
    print(f"Total cost: {total_cost}")
    print(f"Total calories: {total_calories}")
    print()


def main() -> None:
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    budget = 100
    print(f"Budget: {budget}")
    print()

    greedy_result = greedy_algorithm(items, budget)
    print_result("Greedy algorithm", greedy_result, items)

    dynamic_result = dynamic_programming(items, budget)
    print_result("Dynamic programming algorithm", dynamic_result, items)


if __name__ == "__main__":
    main()
