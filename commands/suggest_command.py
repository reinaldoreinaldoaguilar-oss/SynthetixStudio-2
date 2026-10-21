from commands.base_command import Command

class SuggestCommand(Command):
    def __init__(self, avl_tree):
        self.tree = avl_tree
    def execute(self, *args):
        if not args: return "Error: Falta prefijo. Uso: suggest <prefijo>"
        suggestions = self.tree.suggest(args[0])
        return "\n".join(suggestions) if suggestions else f"Sin sugerencias para '{args[0]}'"