import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h
    
    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    # Manhattan distance heuristic
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(position, grid):
    neighbors = []
    x, y = position
    directions = [(0,1), (1,0), (0,-1), (-1,0)]  # Right, Down, Left, Up
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 0:
            neighbors.append((new_x, new_y))
    return neighbors

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

def a_star(start, goal, grid):
    open_list = []
    closed_set = set()
    
    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current = heapq.heappop(open_list)
        
        if current.state == goal:
            return reconstruct_path(current)
        
        closed_set.add(current.state)
        
        for neighbor in get_neighbors(current.state, grid):
            if neighbor in closed_set:
                continue
            
            g = current.g + 1
            h = heuristic(neighbor, goal)
            neighbor_node = Node(neighbor, current, g, h)
            
            if all(neighbor != node.state for node in open_list):
                heapq.heappush(open_list, neighbor_node)
    
    return None

# Define the grid (0 = walkable, 1 = blocked)
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (4, 0)
goal = (0, 0)

path = a_star(start, goal, grid)

if path:
    print("The destination cell is found")
    print("The Path is:")
    for step in reversed(path):
        if step == path[0]:
            print(f"-> {step}")
        else:
            print(f"-> {step}", end=" ")
else:
    print("No path found")
