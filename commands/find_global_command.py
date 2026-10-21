from commands.base_command import Command

class FindGlobalCommand(Command):
    def __init__(self, b_tree):
        self.b_tree = b_tree
    def execute(self, *args):
        if not args: return "Error: Falta token. Uso: find-global <token>"
        result = self.b_tree.search(args[0])
        if not result: return "Token no encontrado."
        output = f"Resultados para '{args[0]}':\n"
        for loc in result['locations']: output += f"  -> {loc}\n"
        return output