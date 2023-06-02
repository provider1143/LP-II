import sys

# Function to find the vertex with the minimum distance value
def find_min_distance(distances, visited):
    min_distance = sys.maxsize
    min_vertex = None

    for v in range(len(distances)):
        if distances[v] < min_distance and not visited[v]:
            min_distance = distances[v]
            min_vertex = v

    return min_vertex

# Function to print the shortest path from the source to the target
def print_path(parents, target):
    if parents[target] != -1:
        print_path(parents, parents[target])
    print(target, end=' ')

# Function to perform Greedy search algorithm for Single-Source Shortest Path problem
def greedy_shortest_path(graph, source, target):
    num_vertices = len(graph)

    # Initialize distances and visited arrays
    distances = [sys.maxsize] * num_vertices
    parents = [-1] * num_vertices
    visited = [False] * num_vertices

    # Distance of source vertex from itself is 0
    distances[source] = 0

    # Find shortest path for all vertices
    for _ in range(num_vertices):
        # Find the vertex with the minimum distance value
        current_vertex = find_min_distance(distances, visited)

        # Mark the current vertex as visited
        visited[current_vertex] = True

        # Update distances and parents for adjacent vertices
        for v in range(num_vertices):
            if (
                graph[current_vertex][v] > 0
                and not visited[v]
                and distances[current_vertex] + graph[current_vertex][v] < distances[v]
            ):
                distances[v] = distances[current_vertex] + graph[current_vertex][v]
                parents[v] = current_vertex

    # Print the shortest path from source to target
    print("Shortest path from", source, "to", target, ":")
    print_path(parents, target)
    print("\nShortest distance:", distances[target])


# Example usage:
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

source_vertex = 0
target_vertex = 4

greedy_shortest_path(graph, source_vertex, target_vertex)