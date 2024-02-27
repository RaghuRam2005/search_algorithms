import math

def alphabeta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or len(node.children) == 0:
        return node.value

    if maximizing_player:
        max_eval = -math.inf
        for child in node.children:
            eval = alphabeta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for child in node.children:
            eval = alphabeta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []


# The above class is used to create a tree. Every node is associated with a value and childern
# Creating a simple game tree with height 3
root = Node()
root.value = 3

child1 = Node(5)
child2 = Node(6)
child3 = Node(9)
root.children = [child1, child2, child3]

grandchild1 = Node(1)
grandchild2 = Node(2)
grandchild3 = Node(0)
grandchild4 = Node(8)
grandchild5 = Node(4)
grandchild6 = Node(7)
child1.children = [grandchild1, grandchild2, grandchild3]
child2.children = [grandchild4, grandchild5]
child3.children = [grandchild6]


# Calculate best score using alpha-beta pruning algorithm
best_score = alphabeta(root, 3, -math.inf, math.inf, True)  # Height of the tree is 3

print(f"Best score: {best_score}")
