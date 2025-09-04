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

    # Inserção
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
       
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    
    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            
            if node.left is None and node.right is None:
                return None
            
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            successor = self._min_value_node(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1  
        return 1 + max(self._height(node.left), self._height(node.right))

   
    def depth(self, value):
        return self._depth(self.root, value, 0)

    def _depth(self, node, value, current_depth):
        if node is None:
            return -1  
        if node.value == value:
            return current_depth
        elif value < node.value:
            return self._depth(node.left, value, current_depth + 1)
        else:
            return self._depth(node.right, value, current_depth + 1)

 
    def visualize(self, filename="bst_tree"):
        dot = Digraph(comment="Binary Search Tree")
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
    bst = BinarySearchTree()
    for v in valores_fixos:
        bst.insert(v)

    print("Árvore fixa criada com valores:", valores_fixos)
    bst.visualize("bst_fixa")


    print("Busca pelo valor 45:", bst.search(45))

   
    bst.delete(30)
    print("Removido o valor 30")
    bst.visualize("bst_fixa_apos_remocao")

    # Nova inserção
    bst.insert(60)
    print("Inserido o valor 60")
    bst.visualize("bst_fixa_apos_insercao")

    print("Altura da árvore:", bst.height())
    print("Profundidade do nó 45:", bst.depth(45))


    valores_random = random.sample(range(1, 200), 15)
    bst_rand = BinarySearchTree()
    for v in valores_random:
        bst_rand.insert(v)

    print("Árvore randômica criada com valores:", valores_random)
    bst_rand.visualize("bst_randomica")
    print("Altura da árvore randômica:", bst_rand.height())