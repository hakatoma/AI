from collections import deque
from tabulate import tabulate

def bfs(initial_state, is_goal, get_adjacent_nodes):
    # Initialize list L using the initial state of the problem
    L = deque([(initial_state, [])])  # Each element is a tuple (node, path_to_node)
    visited = set()  # Set to keep track of visited nodes
    bfs_steps = []  # List to store BFS traversal steps
    path = None  # Initialize path
    
    while L:
        # If L is empty, return failure
        if not L:
            return "Failure", bfs_steps, path
        
        # Choose a node u at the front of L
        u, path = L.popleft()
        
        # If u is the goal state, return the corresponding solution
        if is_goal(u):
            bfs_steps.append((u, get_adjacent_nodes(u), list(L)))
            return path + [u], bfs_steps, path
        
        # Mark u as visited
        visited.add(u)
        
        # For each node v adjacent to node u
        for v in get_adjacent_nodes(u):
            # If v is not visited
            if v not in visited:
                # Insert v into the queue of L and update its path
                L.append((v, path + [u]))
        
        # Store current BFS traversal step
        bfs_steps.append((u, get_adjacent_nodes(u), list(L)))
    
    # If goal state is not found
    return "Failure", bfs_steps, path

# Function to read graph information from a text file
def read_graph_info(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            node, neighbor = line.strip().split()
            if node not in graph:
                graph[node] = []
            graph[node].append(neighbor)
    return graph

# Example usage:
def is_goal(state):
    return state == 'H'

# Modify get_adjacent_nodes function to use the graph dictionary
def get_adjacent_nodes(state, graph):
    return graph.get(state, [])

# Read initial state and graph information from the input file
input_file_path = "AI in class\input-bfs.txt"
graph = read_graph_info(input_file_path)
initial_state = next(iter(graph))

solution, bfs_steps, path = bfs(initial_state, is_goal, lambda state: get_adjacent_nodes(state, graph))

# Write BFS traversal steps and path to an output file
output_file_path = "bfs_output.txt"
with open(output_file_path, 'w', encoding='utf-8') as file:
    # Write BFS traversal steps
    table_data = [["Expanded node", "Adjacency list", "List L"]]
    for step in bfs_steps:
        expanded_node, adjacency_list, list_L = step
        table_data.append([expanded_node, adjacency_list, list_L])
    
    table = tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")
    file.write("BFS traversal steps:\n")
    file.write(table)
    file.write("\n\n")
    
    # Write path
    file.write("Path found:\n")
    if solution != "Failure":
        file.write(" -> ".join(solution))
    else:
        file.write("No path found")

print(f"BFS traversal steps and path have been written to {output_file_path}")
