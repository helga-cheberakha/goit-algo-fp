from node import Node

def merge_sort(head: Node | None) -> Node | None:
    """
    Sort the nodes and return the new head.
    """
    if head is None or head.next is None:
        return head

    # Find the midpoint and split the list
    # into two halves.
    slow, fast = head, head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    right_half = slow.next
    slow.next = None

    left_half = merge_sort(head)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)

def merge(left: Node | None, right: Node | None) -> Node | None:
    """
    Merge two sorted lists into one sorted list.
    """
    dummy = Node(0)
    current = dummy

    while left is not None and right is not None:
        if left.data <= right.data:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next

        current = current.next

    # Attach the remaining nodes.
    current.next = left if left is not None else right
    return dummy.next
