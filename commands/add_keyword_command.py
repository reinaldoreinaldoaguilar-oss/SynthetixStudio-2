from commands.base_command import Command

class AddKeywordCommand(Command):
    def __init__(self, avl_tree):
        self.tree = avl_tree
    def execute(self, *args):
        if not args: return "Error: Faltan argumentos. Uso: add-keyword <palabra>"
        keyword = args[0]
        description = " ".join(args[1:]) if len(args) > 1 else "Palabra clave"
        return self.tree.insert_node(keyword, description)