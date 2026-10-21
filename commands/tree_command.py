from commands.base_command import Command

class TreeCommand(Command):
    def __init__(self, tree):
        self.tree = tree
    def execute(self, *args):
        return self.tree.tree()