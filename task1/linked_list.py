from merge_sort import merge_sort, merge
from node import Node

class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def insert_at_end(self, data: int) -> None:
        """
        Add a node to the end of the list.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def reverse(self) -> None:
        """
        Reverse the links between nodes.
        """
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def sort(self) -> None:
        """
        Sort the list using merge sort.
        """
        self.head = merge_sort(self.head)

    def print_list(self) -> None:
        """
        Print the values separated by arrows.
        """
        items = []
        current = self.head

        while current is not None:
            items.append(str(current.data))
            current = current.next

        print(" -> ".join(items))

def merge_sorted_lists(first: LinkedList, second: LinkedList) -> LinkedList:
    """
    Merge two sorted lists and empty the original lists.
    """
    if first is second:
        raise ValueError("Cannot merge a list with itself.")

    merged = LinkedList()
    merged.head = merge(first.head, second.head)

    # The nodes now belong to the merged list.
    first.head = None
    second.head = None

    return merged
