import heapq
import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        # Give each node a unique ID
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Add nodes and connections to the graph.
    """
    if node is None:
        return graph

    # Add the current node and save its position.
    graph.add_node(node.id, color=node.color, label=node.val)

    if node.left:
        # Connect the left child to its parent.
        graph.add_edge(node.id, node.left.id)

        # Place the left child to the left and one level below.
        l = x - 1 / 2 ** layer
        pos[node.left.id] = (l, y - 1)
        l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)

    if node.right:
        # Connect the right child to its parent.
        graph.add_edge(node.id, node.right.id)

        # Place the right child to the right and one level below.
        r = x + 1 / 2 ** layer
        pos[node.right.id] = (r, y - 1)
        r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

    return graph

def draw_tree(tree_root):
    """
    Draw the tree with values inside its nodes.
    """
    # Create a graph and a dictionary for node positions.
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    # Add all nodes and connections, starting from the root.
    tree = add_edges(tree, tree_root, pos)

     # Get the color, label and displayed value of each node.
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def heap_to_tree(heap, index=0):
    """
    Convert a heap list into a binary tree.
    """
    # Stop when there is no element at this index.
    if index >= len(heap):
        return None

    # Create a node for the current heap element.
    node = Node(heap[index])
    # Build the left subtree from the element at 2 * index + 1.
    node.left = heap_to_tree(heap, 2 * index + 1)
    # Build the right subtree from the element at 2 * index + 2.
    node.right = heap_to_tree(heap, 2 * index + 2)

    # Return the node with its children attached.
    return node

def draw_heap_as_tree(heap):
    """
    Build and draw a tree from an existing heap.
    """
    if not heap:
        print("Купа порожня")
        return

    # Build the tree and drawing it.
    root = heap_to_tree(heap)
    draw_tree(root)


if __name__ == "__main__":
    data = [10, 4, 5, 1, 3, 0, 8, 7, 2]
    # Turn the list into a min-heap.
    # Each parent is less than or equal to its children.
    heapq.heapify(data)

    print("Купа:", data)
    draw_heap_as_tree(data)
