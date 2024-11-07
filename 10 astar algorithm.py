import heapq

# Define a class to represent the grid nodes
class Node:
    def __init__(self, x, y, cost=0, heuristic=0):
        self.x = x
        self.y = y
        self.cost = cost  # g(n): cost from start to this node
        self.heuristic = heuristic  # h(n): heuristic cost to goal
        self.total_cost = cost + heuristic  # f(n) = g(n) + h(n)
    
    # For priority queue ordering based on total_cost
    def __lt__(self, other):
        return self.total_cost < other.total_cost

# Calculate the Manhattan distance heuristic
def heuristic(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# A* algorithm
def a_star(grid, start, goal):
    start_node = Node(start[0], start[1], 0, heuristic(start[0], start[1], goal[0], goal[1]))
    open_list = []
    heapq.heappush(open_list, start_node)
    
    # Track visited nodes and shortest path to each node
    visited = set()
    parent = {start: None}
    cost_so_far = {start: 0}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    
    while open_list:
        current = heapq.heappop(open_list)
        
        # If current is None, we are in an invalid state
        if current is None:
            return None
        
        # Check if goal is reached
        if (current.x, current.y) == goal:
            path = []
            while current is not None:
                path.append((current.x, current.y))
                current = parent[(current.x, current.y)]
            return path[::-1]  # Return path in start-to-goal order
        
        visited.add((current.x, current.y))

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = current.x + dx, current.y + dy

            # Check bounds and if node is traversable (0 indicates traversable)
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                new_cost = cost_so_far[(current.x, current.y)] + 1  # Each step costs 1
                if (nx, ny) not in cost_so_far or new_cost < cost_so_far[(nx, ny)]:
                    cost_so_far[(nx, ny)] = new_cost
                    heuristic_cost = heuristic(nx, ny, goal[0], goal[1])
                    neighbor_node = Node(nx, ny, new_cost, heuristic_cost)
                    heapq.heappush(open_list, neighbor_node)
                    parent[(nx, ny)] = current  # Track parent for path reconstruction
    
    return None  # No path found

# Define the grid (0 is traversable, 1 is an obstacle)
grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Starting and goal positions
start = (0, 0)
goal = (4, 4)

# Run the A* algorithm
path = a_star(grid, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found.")
