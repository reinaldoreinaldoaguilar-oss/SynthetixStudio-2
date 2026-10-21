import re
from data_structures.expression_node import Node


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
        
        output = []
        operators = []
        for token in tokens:
            if token.replace('.', '', 1).isdigit():
                output.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                if operators: operators.pop()
            else:
                while operators and operators[-1] != '(' and self.get_precedence(operators[-1]) >= self.get_precedence(token):
                    output.append(operators.pop())
                operators.append(token)
        
        while operators:
            output.append(operators.pop())

        stack = []
        for token in output:
            if token.replace('.', '', 1).isdigit():
                # Las hojas siempre son los operandos (números)
                stack.append(Node(token))
            else:
                node = Node(token)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
                
        if stack:
            self.root = stack.pop()

    def _evaluate_postorder(self, node):
        if node is None: return 0
            
        if node.left is None and node.right is None:
            return float(node.value)
            
        left_val = self._evaluate_postorder(node.left)
        right_val = self._evaluate_postorder(node.right)
        
        if node.value == '+': return left_val + right_val
        if node.value == '-': return left_val - right_val
        if node.value == '*': return left_val * right_val
        if node.value == '/': 
            if right_val == 0: raise ValueError("División por cero")
            return left_val / right_val

    def evaluate(self, expression):
        self.build_tree(expression)
        return self._evaluate_postorder(self.root)