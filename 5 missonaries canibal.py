from collections import deque

# Define the initial state and the goal state
initial_state = (3, 3, 1)  # (missionaries on left, cannibals on left, boat position)
goal_state = (0, 0, 0)     # (missionaries on left, cannibals on left, boat position)

# Define all possible moves
moves = [
    (1, 0),  # 1 missionary crosses
    (0, 1),  # 1 cannibal crosses
    (2, 0),  # 2 missionaries cross
    (0, 2),  # 2 cannibals cross
    (1, 1)   # 1 missionary and 1 cannibal cross
]

# Check if a state is valid (no missionaries eaten by cannibals)
def is_valid_state(missionaries_left, cannibals_left, missionaries_right, cannibals_right):
    if missionaries_left < 0 or missionaries_right < 0 or cannibals_left < 0 or cannibals_right < 0:
        return False
    if (missionaries_left > 0 and missionaries_left < cannibals_left) or (missionaries_right > 0 and missionaries_right < cannibals_right):
        return False
    return True

# Breadth-First Search to find the solution
def solve_missionaries_cannibals():
    queue = deque([(initial_state, [])])  # Queue stores (state, path)
    visited = set()  # Track visited states

    while queue:
        (missionaries_left, cannibals_left, boat_position), path = queue.popleft()

        # If we reach the goal state, return the path taken
        if (missionaries_left, cannibals_left, boat_position) == goal_state:
            return path + [(missionaries_left, cannibals_left, boat_position)]

        # Mark the current state as visited
        visited.add((missionaries_left, cannibals_left, boat_position))

        # Calculate the number of missionaries and cannibals on the right side
        missionaries_right = 3 - missionaries_left
        cannibals_right = 3 - cannibals_left

        # Explore all possible moves
        for missionaries_move, cannibals_move in moves:
            if boat_position == 1:  # Boat on the left side
                new_state = (missionaries_left - missionaries_move, 
                             cannibals_left - cannibals_move, 0)
            else:  # Boat on the right side
                new_state = (missionaries_left + missionaries_move, 
                             cannibals_left + cannibals_move, 1)

            new_missionaries_left, new_cannibals_left, new_boat_position = new_state
            new_missionaries_right = 3 - new_missionaries_left
            new_cannibals_right = 3 - new_cannibals_left

            # Check if the new state is valid and has not been visited
            if is_valid_state(new_missionaries_left, new_cannibals_left, new_missionaries_right, new_cannibals_right) and new_state not in visited:
                # Add the new state to the queue with the updated path
                queue.append((new_state, path + [(missionaries_left, cannibals_left, boat_position)]))

    return None  # No solution found

# Run the solution
solution = solve_missionaries_cannibals()
if solution:
    print("Solution found:")
    for step in solution:
        print(f"Left side: {step[0]} missionaries, {step[1]} cannibals, Boat: {'Left' if step[2] == 1 else 'Right'}")
else:
    print("No solution found.")
