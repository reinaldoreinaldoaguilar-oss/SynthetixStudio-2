import re
from commands.base_command import Command

class IndexAllCommand(Command):
    def __init__(self, b_tree):
        self.b_tree = b_tree
        self.virtual_files = {
            "main.py": ["def calcular(contador):", "    return contador + 5"],
            "utils.py": ["contador = 0", "print(contador)"]
        }
    def execute(self, *args):
        for filename, lines in self.virtual_files.items():
            for line_num, line_content in enumerate(lines, start=1):
                for token in re.findall(r'[a-zA-Z_]\w*', line_content):
                    self.b_tree.insert(token, f"{filename}:línea {line_num}")
        return "Indexación completada (m=4)."