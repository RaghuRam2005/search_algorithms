#This code is for forward checking algorithm
#The only constarint is that the same color should not be assigned to neighbouring states
# Define the map of Australia with its regions and their neighbors
australia = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}

# Function to get the degree of a node (number of unassigned neighbors)
def get_degree(node, coloring):
    degree = 0
    for neighbor in australia[node]:
        if neighbor not in coloring:
            degree += 1
    return degree

# Function to check if a color assignment is valid
def is_valid(node, color, coloring):
    for neighbor in australia[node]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True

# Function to perform forward checking with the degree heuristic
def forward_checking(node, colors, coloring):
    if len(coloring) == len(australia):
        return coloring  # Solution found

    uncolored_nodes = [n for n in australia if n not in coloring]
    uncolored_nodes.sort(key=lambda n: get_degree(n, coloring), reverse=True)

    for node in uncolored_nodes:
        for color in colors:
            if is_valid(node, color, coloring):
                new_coloring = dict(coloring)
                new_coloring[node] = color
                result = forward_checking(node, colors, new_coloring)
                if result is not None:
                    return result

    return None  # No solution found

# Function to solve the map coloring problem using forward checking with the degree heuristic
def solve_map_coloring():
    colors = ['Red', 'Green', 'Blue', 'Yellow']
    initial_coloring = {}
    solution = forward_checking('WA', colors, initial_coloring)
    if solution is not None:
        print("Map coloring solution found:")
        print(solution)
    else:
        print("No solution found.")

# Solve the map coloring problem
solve_map_coloring()
