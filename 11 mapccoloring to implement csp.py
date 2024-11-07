# Function to check if it's safe to color a region with a given color
def is_safe(region, color, assignment, graph):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking function to assign colors to regions
def map_coloring(graph, colors, assignment, regions):
    if len(assignment) == len(regions):
        return assignment  # All regions are colored

    # Select the next region to color
    unassigned_regions = [r for r in regions if r not in assignment]
    region = unassigned_regions[0]

    # Try each color for the region
    for color in colors:
        if is_safe(region, color, assignment, graph):
            assignment[region] = color
            result = map_coloring(graph, colors, assignment, regions)
            if result:
                return result
            # If no valid assignment, backtrack
            del assignment[region]
    
    return None  # No valid coloring found

# Example graph (map with regions) as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

regions = ['A', 'B', 'C', 'D']
colors = ['Red', 'Green', 'Blue']  # Colors to assign

# Map coloring CSP solver
assignment = {}
result = map_coloring(graph, colors, assignment, regions)

if result:
    print("Coloring of the map:", result)
else:
    print("No valid coloring found")
