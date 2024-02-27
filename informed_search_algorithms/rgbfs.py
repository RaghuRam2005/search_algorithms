class Node:
    def __init__(self, name, heuristic_cost):
        self.name = name
        self.heuristic_cost = heuristic_cost
        self.children = []

    def add_child(self, child, cost):
        self.children.append((child, cost))

def recursive_gbfs(current_node, goal, path, total_cost, total_heuristic_cost):
    print(f"\nCurrent Node: {current_node.name}")
    path.append(current_node.name)
    print(f"Path: {path}")
    print(f"Total Cost: {total_cost}")
    print(f"Total Heuristic Cost: {total_heuristic_cost}")
    if current_node.name == goal:
        print("\nGoal Reached !")
        return True
    if not current_node.children:
        print("Dead end. Backtracking ... ")
        path.pop()
        return False
    current_node.children.sort(key=lambda x: x[0].heuristic_cost)
    for child, cost in current_node.children:
        if child.name not in path:
            if recursive_gbfs(child, goal, path, total_cost + cost, total_heuristic_cost):
                return True

    print("backtracking")
    path.pop()
    return False


arad = Node("Arad", 366)
zerind = Node("Zerind", 374)
sibiu = Node("Sibiu", 253)
timisoara = Node("Timisoara", 329)
oradea = Node("Oradea", 380)
lugoj = Node("Lugoj", 244)
mehadia = Node("Mehadia", 241)
dobreta = Node("Dobreta", 242)
craiova = Node("Craiova", 160)
rimnicu_vilcea = Node("Rimnicu Vilcea", 193)
pitesti = Node("Pitesti", 100)
fagaras = Node("Fagaras", 176)
bucharest = Node("Bucharest", 0)
giurgiu = Node("Giurgiu", 77)
urziceni = Node("Urziceni", 80)
hirsova = Node("Hirsova", 151)
eforie = Node("Eforie", 161)
vaslui = Node("Vaslui", 199)
iasi = Node("Iasi", 226)
neamt = Node("Neamt", 234)

arad.add_child(zerind, 75)
arad.add_child(sibiu, 140)
arad.add_child(timisoara, 118)
zerind.add_child(arad, 75)
zerind.add_child(oradea, 71)
sibiu.add_child(arad, 140)
sibiu.add_child(oradea, 151)
sibiu.add_child(fagaras, 99)
sibiu.add_child(rimnicu_vilcea, 80)
timisoara.add_child(arad, 118)
timisoara.add_child(lugoj, 111)
oradea.add_child(zerind, 71)
oradea.add_child(sibiu, 151)
lugoj.add_child(timisoara, 111)
lugoj.add_child(mehadia, 70)
mehadia.add_child(lugoj, 70)
mehadia.add_child(dobreta, 75)
dobreta.add_child(mehadia, 75)
dobreta.add_child(craiova, 120)
craiova.add_child(dobreta, 120)
craiova.add_child(pitesti, 138)
craiova.add_child(rimnicu_vilcea, 146)
rimnicu_vilcea.add_child(sibiu, 80)
rimnicu_vilcea.add_child(craiova, 146)
rimnicu_vilcea.add_child(pitesti, 97)
pitesti.add_child(craiova, 138)
pitesti.add_child(rimnicu_vilcea, 97)
pitesti.add_child(bucharest, 101)
fagaras.add_child(sibiu, 99)
fagaras.add_child(bucharest, 211)
bucharest.add_child(pitesti, 101)
bucharest.add_child(fagaras, 211)
bucharest.add_child(giurgiu, 90)
bucharest.add_child(urziceni, 85)
giurgiu.add_child(bucharest, 90)
urziceni.add_child(bucharest, 85)
urziceni.add_child(hirsova, 98)
urziceni.add_child(vaslui, 142)
hirsova.add_child(urziceni, 98)
hirsova.add_child(eforie, 86)
eforie.add_child(hirsova, 86)
vaslui.add_child(urziceni, 142)
vaslui.add_child(iasi, 92)
iasi.add_child(vaslui, 92)
iasi.add_child(neamt, 87)
neamt.add_child(iasi, 87)

start_node = arad
goal_node = bucharest
p = []
print("\nPath: ")
total_costs = 0
total_heuristic_costs = 0
if recursive_gbfs(start_node, goal_node.name, p, total_costs, total_heuristic_costs):
    print("Final path: ", p)
else:
    print("No path found")
