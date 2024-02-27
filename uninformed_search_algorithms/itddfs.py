# Iterative Deepening Depth-First Search (IDDFS)
# Create a simple graph as an adjacency list (you can replace this with your own graph).
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def iddfs(graph, start, goal):
    max_depth = 0  # The maximum depth to explore
    while True:
        print(f"Depth limit: {max_depth}")
        result = dls(graph, start, goal, max_depth)
        if result == goal:
            print("Found the goal:", result)
            return
        print("Goal not found at this depth.")
        max_depth += 1

def dls(graph, node, goal, depth):
    if depth == 0:
        if node == goal:
            return node
        if depth > 0:
            print(f"Visiting node: {node} at depth {depth}")
        for neighbor in graph[node]:
            result = dls(graph, neighbor, goal, depth - 1)
            if result is not None:
                return result
            return None
        else:
            return None

# Start the IDDFS algorithm
start_node = 'A'
goal_node = 'F'
iddfs(graph, start_node, goal_node)
