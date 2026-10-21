class Node:
    def __init__(self, keyword, description):
        self.keyword = keyword
        self.description = description
        self.left = None
        self.right = None
        self.height = 1

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

        # Rotación
        x.right = y
        y.left = T2

        # Actualizar alturas
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Rotación
        y.left = x
        x.right = T2

        # Actualizar alturas
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, keyword, description):
        # 1. Inserción normal de BST
        if not root:
            return Node(keyword, description)
        elif keyword < root.keyword:
            root.left = self.insert(root.left, keyword, description)
        elif keyword > root.keyword:
            root.right = self.insert(root.right, keyword, description)
        else:
            return root  # Las palabras duplicadas no se insertan

        # 2. Actualizar altura
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Obtener el factor de balanceo
        balance = self.get_balance(root)

        # 4. Balancear el árbol si es necesario
        # Caso Izquierda Izquierda
        if balance > 1 and keyword < root.left.keyword:
            return self.right_rotate(root)

        # Caso Derecha Derecha
        if balance < -1 and keyword > root.right.keyword:
            return self.left_rotate(root)

        # Caso Izquierda Derecha
        if balance > 1 and keyword > root.left.keyword:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Caso Derecha Izquierda
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