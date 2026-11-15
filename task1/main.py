import random

from linked_list import LinkedList, merge_sorted_lists

if __name__ == "__main__":
    # Build a linked list.
    linked_list = LinkedList()
    for value in random.sample(range(1, 21), 6):
        linked_list.insert_at_end(value)

    print("Однозв'язний список:")
    linked_list.print_list()

    print()
    print("Однозв'язний список після реверсування:")
    linked_list.reverse()
    linked_list.print_list()

    print()
    print("Відсортований однозв'язний список:")
    linked_list.sort()
    linked_list.print_list()

    # Build an extra linked list.
    extra_linked_list = LinkedList()
    for value in random.sample(range(1, 21), 6):
        extra_linked_list.insert_at_end(value)

    print()
    print("Другий відсортований однозв'язний список:")
    extra_linked_list.sort()
    extra_linked_list.print_list()

    print()
    print("Об’єднаний відсортований список:")
    merged_linked_list = merge_sorted_lists(linked_list, extra_linked_list)
    merged_linked_list.print_list()
