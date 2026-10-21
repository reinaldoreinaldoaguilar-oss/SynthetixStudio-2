from commands.base_command import Command

class CdCommand(Command):
    def __init__(self, tree):
        self.tree = tree
    def execute(self, *args):
        if not args: return "Error: Falta el nombre. Uso: cd <nombre>"
        return self.tree.cd(args[0])