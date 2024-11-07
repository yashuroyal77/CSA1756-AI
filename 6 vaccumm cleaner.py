from collections import deque

# Define the grid environment (1 represents a dirty cell, 0 represents a clean cell)
grid = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
]

# Dimensions of the grid
rows = len(grid)
cols = len(grid[0])

# Directions for moving up, down, left, and right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS function to clean all dirty cells starting from the given initial position
def vacuum_cleaner(grid, start):
    queue = deque([start])    # Queue to track cells to visit
    visited = set([start])    # Track visited cells
    steps = 0                 # Count the number of steps taken
    
    while queue:
        x, y = queue.popleft()
        
        # Clean the current cell (set it to 0 if it was dirty)
        if grid[x][y] == 1:
            print(f"Cleaning cell ({x}, {y})")
            grid[x][y] = 0
        
        # Explore neighboring cells
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the new cell is within bounds and not yet visited
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
        
        steps += 1
    
    print(f"Total steps taken to clean: {steps}")

# Starting position of the vacuum cleaner
start_position = (0, 0)

# Run the vacuum cleaner simulation
vacuum_cleaner(grid, start_position)

# Display the final grid state
print("\nFinal grid state:")
for row in grid:
    print(row)
