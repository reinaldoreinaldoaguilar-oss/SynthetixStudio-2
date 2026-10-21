import re
from commands.base_command import Command

class IndexAllCommand(Command):
    def __init__(self, b_tree):
        self.b_tree = b_tree
        # Simulamos archivos virtuales abiertos en el IDE para poder indexar
        self.virtual_files = {
            "main.py": [
                "def calcular_total(contador):",
                "    return contador + 5"
            ],
            "utils.py": [
                "contador = 0",
                "print(contador)"
            ]
        }

    def execute(self, *args):
        total_tokens = 0
        for filename, lines in self.virtual_files.items():
            for line_num, line_content in enumerate(lines, start=1):
                # Extraemos solo palabras (tokens)
                tokens = re.findall(r'[a-zA-Z_]\w*', line_content)
                for token in tokens:
                    location = f"{filename}:línea {line_num}"
                    self.b_tree.insert(token, location)
                    total_tokens += 1
                    
        return f"Indexación completada. Se indexaron tokens de los archivos abiertos en el Árbol B (m=4)."

class FindGlobalCommand(Command):
    def __init__(self, b_tree):
        self.b_tree = b_tree

    def execute(self, *args):
        if not args:
            return "Error: Falta el token. Uso: find-global <token>"
            
        token = args[0]
        result = self.b_tree.search(token)
        
        if not result:
            return f"El token '{token}' no se encontró en ningún archivo."
            
        # Formatear la salida
        output = f"Resultados para '{token}':\n"
        for loc in result['locations']:
            output += f"  -> {loc}\n"
        return output