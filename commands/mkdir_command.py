from commands.base_command import Command

class MkdirCommand(Command):
    def __init__(self, tree):
        self.tree = tree
    def execute(self, *args):
        if not args: return "Error: Falta el nombre. Uso: mkdir <nombre>"
        return self.tree.mkdir(args[0])