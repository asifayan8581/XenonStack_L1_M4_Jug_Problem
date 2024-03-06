from collections import deque

def bfs_solve(jug1_capacity, jug2_capacity, target_amount):
    initial_state = (0, 0, [])
    queue = deque([initial_state])
    visited_states = set()
    
   

    while queue:
        current_state = queue.popleft()

        if current_state[0] == target_amount:
            print_operations(current_state[2])
            print(f"Large jug can have {target_amount} gallons of water at last")
            return True  # Solution found

        visited_states.add((current_state[0], current_state[1]))

        # Fill small jug
        fill_small_jug = (jug1_capacity, current_state[1], current_state[2] + [f"Fill Small Jug: {jug1_capacity},{current_state[1]}"])
        #print(f"{jug1_capacity},{current_state[1]}")
        if fill_small_jug[:2] not in visited_states:
            queue.append(fill_small_jug)

        # Fill large jug
        fill_large_jug = (current_state[0], jug2_capacity, current_state[2] + [f"Fill Large Jug: {current_state[0]},{jug2_capacity}"])
        if fill_large_jug[:2] not in visited_states:
            queue.append(fill_large_jug)

        # Empty small jug
        empty_small_jug = (0, current_state[1], current_state[2] + ["Empty Small Jug"])
        if empty_small_jug[:2] not in visited_states:
            queue.append(empty_small_jug)

        # Empty large jug
        empty_large_jug = (current_state[0], 0, current_state[2] + ["Empty Large Jug"])
        if empty_large_jug[:2] not in visited_states:
            queue.append(empty_large_jug)

        # Pour from small jug to large jug
        pour_small_to_large = (
            max(0, current_state[0] - (jug2_capacity - current_state[1])),
            min(jug2_capacity, current_state[1] + current_state[0]),
            current_state[2] + [f"Pour ({min(current_state[0], jug2_capacity - current_state[1])} gallons) from Small to Large Jug ({max(0, current_state[0] - (jug2_capacity - current_state[1]))}\
,{min(jug2_capacity, current_state[1] + current_state[0])})"]
        )
        if pour_small_to_large[:2] not in visited_states:
            queue.append(pour_small_to_large)

        # Pour from large jug to small jug
        pour_large_to_small = (
            min(jug1_capacity, current_state[0] + current_state[1]),
            max(0, current_state[1] - (jug1_capacity - current_state[0])),
            current_state[2] + [f"Pour Large to Small Jug ({min(current_state[1], jug1_capacity - current_state[0])} gallons)"]
        )
        if pour_large_to_small[:2] not in visited_states:
            queue.append(pour_large_to_small)

    return False  # No solution found

def print_operations(operations):
    print("\nSteps to achieve the target:")
    for operation in operations:
        print(operation)

# Get user input
jug1 = int(input("Enter the capacity of the first jug: "))
jug2 = int(input("Enter the capacity of the second jug: "))
target = int(input("Enter the target amount of water to be left in the larger jug: "))
jug1_capacity = min(jug1,jug2)
jug2_capacity = max(jug1,jug2)
print(f"Small jug Capacity: {jug1_capacity}, large jug capacity: {jug2_capacity}")


# Solve using BFS and print operations with gallon amount
if bfs_solve(jug1_capacity, jug2_capacity, target):
    print("\nSolution exists")
else:
    print("\nSolution does not exist")
