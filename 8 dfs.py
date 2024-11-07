# DFS function to recursively traverse the graph from a given start node
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()  # Initialize visited set if not provided
    
    # Mark the current node as visited and print it
    print(node, end=" ")
    visited.add(node)

    # Recur for all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Run DFS starting from node 'A'
print("DFS Traversal starting from node A:")
dfs(graph, 'A')
