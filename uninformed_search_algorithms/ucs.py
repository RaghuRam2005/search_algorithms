import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, start, end, cost):
        if start not in self.edges:
            self.edges[start] = []
        self.edges[start].append((end, cost))

def uniform_cost_search(graph, start, goal):
    visited = set()
    priority_queue = [(0, start, [])]  # (cost, node, path)

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        path = path + [node]  # Add the current node to the path
        visited.add(node)  # Mark the node as visited

        # Print information about the visited node
        print(f"Visited Node: {node}, Cost: {cost}, Path: {path}")

        if node == goal:
            return path

        if node in graph.edges:
            for neighbor, neighbor_cost in graph.edges[node]:
                if neighbor not in visited:
                    new_cost = cost + neighbor_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor, path))

    return None

if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 5)
    g.add_edge("B", "D", 10)
    g.add_edge("C", "D", 3)
    g.add_edge("D", "E", 7)
    g.add_edge("E", "A", 3)

    start_node = "A"
    goal_node = "D"

    print(f"Starting Uniform Cost Search from {start_node} to {goal_node}\n")
    result = uniform_cost_search(g, start_node, goal_node)

    if result:
        print(f"\nShortest Path: {result}")
    else:
        print(f"\nNo path found from {start_node} to {goal_node}")
