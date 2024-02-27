# Define the map of Australia with its regions and their neighbors
australia = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}

# Function to check if a color assignment is valid
def is_valid(node, color, coloring):
    for neighbor in australia[node]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True

# Backtracking algorithm to solve the map coloring problem
def map_coloring(node, colors, coloring):
    if node not in coloring:
        for color in colors:
            if is_valid(node, color, coloring):
                coloring[node] = color
                next_node = list(australia.keys())[list(australia.keys()).index(node) + 1] if list(australia.keys()).index(node) < len(australia) - 1 else None
                if next_node is None or map_coloring(next_node, colors, coloring):
                    return True
                coloring[node] = None
        return False
    else:
        next_node = list(australia.keys())[list(australia.keys()).index(node) + 1] if list(australia.keys()).index(node) < len(australia) - 1 else None
        if next_node is None or map_coloring(next_node, colors, coloring):
            return True
        return False

# Function to initiate the map coloring
def solve_map_coloring():
    colors = ['Red', 'Green', 'Blue', 'Yellow']
    coloring = {}
    if map_coloring('WA', colors, coloring):
        print("Map coloring solution found:")
        print(coloring)
    else:
        print("No solution found.")

# Solve the map coloring problem
solve_map_coloring()
