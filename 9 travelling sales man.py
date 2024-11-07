from itertools import permutations

# Define the graph as an adjacency matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
n = len(graph)

# Function to calculate the minimum path
def traveling_salesman(graph, start=0):
    # Generate all permutations of cities, excluding the start city
    cities = list(range(n))
    cities.remove(start)
    
    # Initialize minimum path length
    min_path = float('inf')
    best_route = None
    
    # Check each possible path
    for perm in permutations(cities):
        current_path_weight = 0
        current_route = [start] + list(perm) + [start]
        
        # Calculate the path cost
        for i in range(len(current_route) - 1):
            current_path_weight += graph[current_route[i]][current_route[i + 1]]
        
        # Update minimum path if the current one is shorter
        if current_path_weight < min_path:
            min_path = current_path_weight
            best_route = current_route
    
    return min_path, best_route

# Run the TSP algorithm and display results
min_cost, route = traveling_salesman(graph)
print(f"Minimum Cost: {min_cost}")
print(f"Route: {route}")
