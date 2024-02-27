#dfs
# Define a sample graph as an adjacency list.
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graph, node, goal, visited, path):
    # Print the current node being explored.
    print("Visiting node:", node)

    # Mark the current node as visited.
    visited.add(node)

    # Add the current node to the path.
    path.append(node)

    # If the current node is the goal, print the path and return True.
    if node == goal:
        print("Goal reached! Path:", ' -> '.join(path))
        return True

    # Recursively visit the neighbors of the current node.
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited, path):
                return True

    # If the goal is not found in this branch, backtrack.
    print("Backtracking from node:", node)
    path.pop()

    return False

def dfs_search(graph, start, goal):
    # Initialize a set to keep track of visited nodes.
    visited = set()

    # Initialize a list to store the current path.
    path = []

    # Start the DFS search from the 'start' node.
    if not dfs(graph, start, goal, visited, path):
        print("Goal not reached.")

# Define the start and goal nodes.
start_node = 'A'
goal_node = 'F'

# Call the DFS search function.
dfs_search(graph, start_node, goal_node)
