from data_structures.avl_node import Node

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        
        y.left = x
        x.right = T2

        
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, keyword, description):
        
        if not root:
            return Node(keyword, description)
        elif keyword < root.keyword:
            root.left = self.insert(root.left, keyword, description)
        elif keyword > root.keyword:
            root.right = self.insert(root.right, keyword, description)
        else:
            return root  

        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        
        balance = self.get_balance(root)

        
    
        if balance > 1 and keyword < root.left.keyword:
            return self.right_rotate(root)

    
        if balance < -1 and keyword > root.right.keyword:
            return self.left_rotate(root)

        
        if balance > 1 and keyword > root.left.keyword:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        
        if balance < -1 and keyword < root.right.keyword:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
        
    def insert_node(self, keyword, description):
        self.root = self.insert(self.root, keyword, description)
        return f"Palabra '{keyword}' añadida al diccionario AVL."

    def in_order_suggest(self, node, prefix, suggestions):
        if node:
            self.in_order_suggest(node.left, prefix, suggestions)
            if node.keyword.startswith(prefix):
                suggestions.append(f"{node.keyword}: {node.description}")
            self.in_order_suggest(node.right, prefix, suggestions)

    def suggest(self, prefix):
        suggestions = []
        self.in_order_suggest(self.root, prefix, suggestions)
        return suggestions