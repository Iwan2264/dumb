import heapq

def water_jug_bfs(capacity1, capacity2, target):
    visited = set()
    queue = []
    path = {}

    heapq.heappush(queue, (0, (0, 0)))
    path[(0, 0)] = None

    while queue:
        _, (jug1, jug2) = heapq.heappop(queue)

        if jug1 == target or jug2 == target:
            result = []
            state = (jug1, jug2)
            while state:
                result.append(state)
                state = path[state]
            return result[::-1]
        
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        transitions = [
            (capacity1, jug2),  
            (jug1, capacity2),  
            (0, jug2),
            (jug1, 0),
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)),
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1))
        ]

        for new_jug1, new_jug2 in transitions:
            if (new_jug1, new_jug2) not in visited:
                priority = abs(target - new_jug1) + abs(target - new_jug2)
                heapq.heappush(queue, (priority, (new_jug1, new_jug2)))
                path[(new_jug1, new_jug2)] = (jug1, jug2)

    return None

capacity1 = 3
capacity2 = 5
target = 4

solution = water_jug_bfs(capacity1, capacity2, target)

if solution:
    print("\nThe destination state is found")
    print("The Path is:")
    for step in solution:
        print(f"{step}\n", end=" ")
else:
    print("No solution found")
