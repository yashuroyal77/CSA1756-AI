from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    # Queue for storing states (jug1, jug2) and a set for visited states
    queue = deque()
    visited = set()
    
    # Start with both jugs empty
    queue.append((0, 0))
    visited.add((0, 0))
    
    # Perform BFS
    while queue:
        jug1, jug2 = queue.popleft()
        
        # If we reach the target in either jug, return True
        if jug1 == target or jug2 == target or jug1 + jug2 == target:
            return True
        
        # List all possible next states
        possible_moves = [
            (jug1_capacity, jug2),    # Fill jug1
            (jug1, jug2_capacity),    # Fill jug2
            (0, jug2),                # Empty jug1
            (jug1, 0),                # Empty jug2
            (min(jug1 + jug2, jug1_capacity), max(0, jug2 - (jug1_capacity - jug1))),  # Pour water jug2 -> jug1
            (max(0, jug1 - (jug2_capacity - jug2)), min(jug1 + jug2, jug2_capacity))   # Pour water jug1 -> jug2
        ]
        
        # Explore each possible move
        for new_jug1, new_jug2 in possible_moves:
            if (new_jug1, new_jug2) not in visited:
                visited.add((new_jug1, new_jug2))
                queue.append((new_jug1, new_jug2))
    
    return False  # If all possible states have been explored without finding the target

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2

result = water_jug_bfs(jug1_capacity, jug2_capacity, target)
if result:
    print("It is possible to measure exactly", target, "liters of water.")
else:
    print("It is not possible to measure exactly", target, "liters of water.")
