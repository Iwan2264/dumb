def water_jug_dfs(capacity1, capacity2, target):
    visited = set()
    path = []

    def dfs(jug1, jug2):
        if (jug1, jug2) in visited:
            return False
        
        visited.add((jug1, jug2))

        path.append((jug1, jug2))

        if jug1 == target or jug2 == target:
            return True

        transitions = [
            (capacity1, jug2),  
            (jug1, capacity2),  
            (0, jug2),          
            (jug1, 0),          
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)),  
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1))   
        ]

        for new_jug1, new_jug2 in transitions:
            if dfs(new_jug1, new_jug2):
                return True

        path.pop()
        return False

    dfs(0, 0)


    return path

capacity1 = 3  
capacity2 = 5 
target = 4    

solution = water_jug_dfs(capacity1, capacity2, target)

if solution:
    print("Solution steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")