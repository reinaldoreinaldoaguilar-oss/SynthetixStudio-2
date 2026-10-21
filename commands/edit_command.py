import os
from commands.base_command import Command
from data_structures.n_ary_node import Node

class EditCommand(Command):
    def __init__(self, tree):
        self.tree = tree

    def execute(self, *args):
        if len(args) < 2:
            return 'Error: Faltan argumentos. Uso: edit <nombre_archivo> "<contenido>"'
        
        filename = args[0]
        content = " ".join(args[1:]).strip('"').strip("'")
        
        if filename not in self.tree.current.children:
            new_file_node = Node(filename, is_file=True)
            new_file_node.parent = self.tree.current
            self.tree.current.children[filename] = new_file_node
            
        try:
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(content + "\n")
            return f"Archivo '{filename}' modificado exitosamente."
        except Exception as e:
            return f"Error al modificar el archivo físico: {e}"