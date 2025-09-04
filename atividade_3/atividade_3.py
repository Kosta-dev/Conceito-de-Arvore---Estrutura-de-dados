import random
from graphviz import Digraph


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

   
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

  
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)

    def visualize(self, filename="bst_tree"):
        dot = Digraph(comment="Binary Tree")
        counter = [0]

        def add_nodes_edges(node, parent=None):
            if node is None:
                return
            node_id = str(counter[0])
            counter[0] += 1

            dot.node(node_id, str(node.value))

            if parent is not None:
                dot.edge(parent, node_id)

            add_nodes_edges(node.left, node_id)
            add_nodes_edges(node.right, node_id)

        add_nodes_edges(self.root)
        dot.render(filename, format="png", cleanup=True)
        print(f"Árvore gerada: {filename}.png")

if __name__ == "__main__":
 
    valores_fixos = [55, 30, 80, 20, 45, 70, 90]
    bst_fixa = BinarySearchTree()
    for v in valores_fixos:
        bst_fixa.insert(v)

    print("==== Árvore Fixa ====")
    bst_fixa.visualize("bst_fixa")
    print("In-Order :", bst_fixa.inorder())
    print("Pre-Order:", bst_fixa.preorder())
    print("Post-Order:", bst_fixa.postorder())
    print()

 
    valores_random = random.sample(range(1, 100), 10)
    bst_rand = BinarySearchTree()
    for v in valores_random:
        bst_rand.insert(v)

    print("==== Árvore Randômica ====")
    print("Valores inseridos:", valores_random)
    bst_rand.visualize("bst_randomica")
    print("In-Order :", bst_rand.inorder())
    print("Pre-Order:", bst_rand.preorder())
    print("Post-Order:", bst_rand.postorder())