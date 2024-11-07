import heapq

# Define the goal state for the 8-puzzle
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, cost=0, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost  # Cost is the depth + heuristic
        self.depth = depth

    def __lt__(self, other):
        return self.cost < other.cost

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_neighbors(node):
    x, y = get_blank_position(node.state)
    neighbors = []
    moves = {
        'UP': (x - 1, y),
        'DOWN': (x + 1, y),
        'LEFT': (x, y - 1),
        'RIGHT': (x, y + 1)
    }

    for move, (new_x, new_y) in moves.items():
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in node.state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(PuzzleNode(new_state, node, move, node.depth + 1 + manhattan_distance(new_state), node.depth + 1))
    return neighbors

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_x, target_y = divmod(value - 1, 3)
                distance += abs(target_x - i) + abs(target_y - j)
    return distance

def is_goal(state):
    return state == goal_state

def a_star(initial_state):
    start_node = PuzzleNode(initial_state, cost=manhattan_distance(initial_state))
    frontier = []
    heapq.heappush(frontier, start_node)
    explored = set()

    while frontier:
        current_node = heapq.heappop(frontier)
        explored.add(tuple(map(tuple, current_node.state)))

        if is_goal(current_node.state):
            return reconstruct_path(current_node)

        for neighbor in generate_neighbors(current_node):
            neighbor_state_tuple = tuple(map(tuple, neighbor.state))
            if neighbor_state_tuple not in explored:
                heapq.heappush(frontier, neighbor)

    return None

def reconstruct_path(node):
    path = []
    while node.parent is not None:
        path.append(node.move)
        node = node.parent
    return path[::-1]

# Example usage
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution = a_star(initial_state)
if solution:
    print("Solution found:")
    print(" -> ".join(solution))
else:
    print("No solution found.")
