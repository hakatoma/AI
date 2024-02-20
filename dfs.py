from tabulate import tabulate

def dfs(initial_state, is_goal, get_adjacent_nodes):
    # Initialize list L using the initial state of the problem
    L = [(initial_state, [])]  # Each element is a tuple (node, path_to_node)
    visited = set()  # Set to keep track of visited nodes
    dfs_steps = []  # List to store DFS traversal steps
    
    while L:
        # If L is empty, return failure
        if not L:
            return "Failure", dfs_steps
        
        # Choose a node u at the front of L
        u, path = L.pop()
        
        # If u is the goal state, return the corresponding solution
        if is_goal(u):
            dfs_steps.append((u, get_adjacent_nodes(u), list(L)))
            return path + [u], dfs_steps
        
        # Mark u as visited
        visited.add(u)
        
        # For each node v adjacent to node u
        for v in get_adjacent_nodes(u):
            # If v is not visited
            if v not in visited:
                # Insert v into the front of L and update its path
                L.append((v, path + [u]))
        
        # Store current DFS traversal step
        dfs_steps.append((u, get_adjacent_nodes(u), list(L)))
    
    # If goal state is not found
    return "Failure", dfs_steps

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
input_file_path = "AI in class\input-dfs.txt"
graph = read_graph_info(input_file_path)
initial_state = next(iter(graph))

solution, dfs_steps = dfs(initial_state, is_goal, lambda state: get_adjacent_nodes(state, graph))

# Write DFS traversal steps to an output file
output_file_path = "dfs_output.txt"
with open(output_file_path, 'w', encoding='utf-8') as file:
    # Write DFS traversal steps
    table_data = [["Expanded node", "Adjacency list", "List L"]]
    for step in dfs_steps:
        expanded_node, adjacency_list, list_L = step
        table_data.append([expanded_node, adjacency_list, list_L])
    
    table = tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")
    file.write("DFS traversal steps:\n")
    file.write(table)
    file.write("\n\n")
    
    # Write solution
    file.write("Solution:\n")
    if solution != "Failure":
        file.write(" -> ".join(solution))
    else:
        file.write("No path found")

print(f"DFS traversal steps and solution have been written to {output_file_path}")
