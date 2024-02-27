# bfs
# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start, goal):
    # Create a queue for BFS and a dictionary to track the parent of each node
    queue = [start]
    parent = {start: None}

    # Initialize variables to print the path
    current_node = start
    path = []

    while queue:
        current_node = queue.pop(0)
        path.append(current_node)  # Track the current node in the path

        if current_node == goal:
            break

        for neighbor in graph[current_node]:
            if neighbor not in parent:
                queue.append(neighbor)
                parent[neighbor] = current_node

    if current_node != goal:
        print("Path not found.")
    else:
        # Reconstruct and print the path
        print("Path found:")
        print_path(parent, start, goal, path)

def print_path(parent, start, goal, path):
    if goal == start:
        print(start)
    else:
        print_path(parent, start, parent[goal], path)
        print(goal)

start_node = 'A'
goal_node = 'F'
bfs(graph, start_node, goal_node)