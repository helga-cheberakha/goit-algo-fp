import heapq
import networkx as nx

def get_graph() -> nx.Graph:
    """
    Build a weighted graph.
    """
    G = nx.Graph()
    G.add_edge('A', 'B', weight=5)
    G.add_edge('A', 'C', weight=10)
    G.add_edge('B', 'D', weight=3)
    G.add_edge('C', 'D', weight=2)
    G.add_edge('D', 'E', weight=4)

    return G

def dijkstra(graph: nx.Graph, start: str) -> dict:
    """
    Find shortest distances from the start vertex using a min heap.
    """
    if start not in graph:
        raise ValueError("The start vertex is not in the graph.")

    # Dijkstra algorithm requires non-negative edge weights.
    for _, _, attributes in graph.edges(data=True):
        if attributes["weight"] < 0:
            raise ValueError("Edge weights cannot be negative.")

    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Store pairs of (distance, vertex) in a min heap.
    heap = [(0, start)]
    while heap:
        # Take the vertex with the smallest distance.
        current_distance, current_vertex = heapq.heappop(heap)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes["weight"]
            distance = current_distance + weight

            # Save a shorter distance and queue the neighbor.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


if __name__ == "__main__":
    graph = get_graph()
    start = "A"

    print(f"Найкоротші відстані від вершини {start}:")
    distances = dijkstra(graph, start)
    for vertex, distance in distances.items():
        if distance == float("inf"):
            print(f"{start} → {vertex}: шлях відсутній")
        else:
            print(f"{start} → {vertex}: {distance}")
