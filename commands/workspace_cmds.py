from commands.base_command import Command

class MkdirCommand(Command):
    def __init__(self, tree):
        self.tree = tree

    def execute(self, *args):
        if not args:
            return "Error: Falta el nombre de la carpeta. Uso: mkdir <nombre_carpeta>"
        return self.tree.mkdir(args[0])

class CdCommand(Command):
    def __init__(self, tree):
        self.tree = tree

    def execute(self, *args):
        if not args:
            return "Error: Falta el nombre del directorio. Uso: cd <nombre_carpeta>"
        return self.tree.cd(args[0])

class TreeCommand(Command):
    def __init__(self, tree):
        self.tree = tree

    def execute(self, *args):
        # Imprime la estructura jerárquica completa
        return self.tree.tree()