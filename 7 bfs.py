from collections import deque

# BFS function to traverse the graph from a given start node
def bfs(graph, start_node):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start_node])  # Queue to handle the BFS order

    # Loop through the queue until it's empty
    while queue:
        # Dequeue a node from the front
        node = queue.popleft()
        
        # If the node has not been visited yet
        if node not in visited:
            print(node, end=" ")  # Print the node (or perform any other operation)
            visited.add(node)  # Mark the node as visited
            
            # Enqueue all unvisited neighbors of the node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Run BFS from the starting node 'A'
print("BFS Traversal starting from node A:")
bfs(graph, 'A')
