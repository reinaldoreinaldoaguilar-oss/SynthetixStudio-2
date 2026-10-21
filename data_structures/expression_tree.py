import re

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None

    def get_precedence(self, op):
        # Define la jerarquía de las operaciones matemáticas
        if op in ('+', '-'): return 1
        if op in ('*', '/'): return 2
        return 0

    def build_tree(self, expression):
        # 1. Separamos números y símbolos matemáticos
        tokens = re.findall(r'\d+\.\d+|\d+|[+/*()-]', expression)
        
        # 2. Convertimos a notación postfija (Algoritmo Shunting Yard)
        output = []
        operators = []
        for token in tokens:
            if token.replace('.', '', 1).isdigit(): # Si es un número
                output.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                if operators: operators.pop() # Quitamos el '('
            else: # Es un operador (+, -, *, /)
                while operators and operators[-1] != '(' and self.get_precedence(operators[-1]) >= self.get_precedence(token):
                    output.append(operators.pop())
                operators.append(token)
        
        while operators:
            output.append(operators.pop())

        # 3. Construimos el Árbol Binario
        stack = []
        for token in output:
            if token.replace('.', '', 1).isdigit():
                # Las hojas siempre son los operandos (números)
                stack.append(Node(token))
            else:
                # Los nodos internos son los operadores
                node = Node(token)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
                
        if stack:
            self.root = stack.pop()

    def _evaluate_postorder(self, node):
        # Condición base: si está vacío
        if node is None: return 0
            
        # Si es un nodo hoja (número), retornamos su valor
        if node.left is None and node.right is None:
            return float(node.value)
            
        # Recorrido en Postorden: Izquierda -> Derecha -> Raíz
        left_val = self._evaluate_postorder(node.left)
        right_val = self._evaluate_postorder(node.right)
        
        # Aplicamos el operador (Raíz)
        if node.value == '+': return left_val + right_val
        if node.value == '-': return left_val - right_val
        if node.value == '*': return left_val * right_val
        if node.value == '/': 
            if right_val == 0: raise ValueError("División por cero")
            return left_val / right_val

    def evaluate(self, expression):
        self.build_tree(expression)
        return self._evaluate_postorder(self.root)