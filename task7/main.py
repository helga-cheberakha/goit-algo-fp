import random


def monte_carlo_dice(num_experiments: int, seed: int | None = None) -> dict:
    """
    Estimate the probability of each sum when rolling two dice.
    """
    rng = random.Random(seed)

    # Store the number of rolls for each possible sum.
    counts = {total: 0 for total in range(2, 13)}

    for _ in range(num_experiments):
        # Roll two dice and add their values.
        first_die = rng.randint(1, 6)
        second_die = rng.randint(1, 6)
        total = first_die + second_die

        counts[total] += 1

    # Divide each count by the total number of rolls.
    probabilities = {}
    for total, count in counts.items():
        probabilities[total] = count / num_experiments

    return probabilities


def main() -> None:
    """
    Compare Monte Carlo probabilities with analytical probabilities.
    """
    num_experiments = 100000
    probabilities = monte_carlo_dice(num_experiments, seed=42)

    # Two dice have 36 equally likely combinations.
    analytical_probabilities = {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36,
    }

    print(f"Кількість кидків двох кубиків: {num_experiments}")
    print()
    print(f"| {'Сума': <4} | {'Монте-Карло, %': <14} | {'Аналітична, %': <13} | {'Відхилення': <16}")
    print(f":{'-'*5} | :{'-'*13} | :{'-'*12} | :{'-'*15}")

    for total, probability in probabilities.items():
        analytical_probability = analytical_probabilities[total]

        # Convert probabilities to percentages.
        simulated_percent = probability * 100
        analytical_percent = analytical_probability * 100

        # Compare percentages in percentage points.
        difference = abs(simulated_percent - analytical_percent)

        print(f"| {total:4} | {simulated_percent:14.2f} | {analytical_percent:13.2f} | {difference:16.4f}")


if __name__ == "__main__":
    main()
