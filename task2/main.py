import sys

from pythagoras_tree import draw_pythagoras_tree

def main() -> None:
    # Check whether the Pythagoras tree depth is given.
    if len(sys.argv) <= 1:
        print('Please enter the Pythagoras tree depth as a positive integer: <depth>')
        return

    # Validate the user input, it should be a positive integer.
    try:
        depth = int(sys.argv[1])
    except ValueError:
        return print("Please enter a whole number.")

    if depth <= 0:
        print("Depth must be greater than zero.")
        return

    draw_pythagoras_tree(depth)

if __name__ == "__main__":
    main()
