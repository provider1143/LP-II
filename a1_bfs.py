from queue import Queue

# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = Queue()
    queue.put(start)
    visited.add(start)

    while not queue.empty():
        vertex = queue.get()
        print(vertex)  # Process the vertex

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.put(neighbor)
                visited.add(neighbor)


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS traversal:")
bfs(graph, 'A')

