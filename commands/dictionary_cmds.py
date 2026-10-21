from commands.base_command import Command

class AddKeywordCommand(Command):
    def __init__(self, avl_tree):
        self.tree = avl_tree

    def execute(self, *args):
        if not args:
            return "Error: Faltan argumentos. Uso: add-keyword <palabra> [descripcion opcional]"
        
        keyword = args[0]
        # Unir el resto de los argumentos como descripción si existen
        description = " ".join(args[1:]) if len(args) > 1 else "Palabra clave del sistema"
        return self.tree.insert_node(keyword, description)

class SuggestCommand(Command):
    def __init__(self, avl_tree):
        self.tree = avl_tree

    def execute(self, *args):
        if not args:
            return "Error: Falta el prefijo. Uso: suggest <prefijo>"
            
        prefix = args[0]
        suggestions = self.tree.suggest(prefix)
        
        if not suggestions:
            return f"No hay sugerencias para '{prefix}'"
            
        return "\n".join(suggestions)