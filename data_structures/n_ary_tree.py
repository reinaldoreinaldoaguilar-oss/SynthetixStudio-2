from data_structures.n_ary_node import Node

class NaryTree:
    def __init__(self):
        self.root = Node("root")
        self.current = self.root

    def mkdir(self, folder_name):
        if folder_name in self.current.children:
            return f"Error: La carpeta '{folder_name}' ya existe."
        
        new_folder = Node(folder_name)
        new_folder.parent = self.current
        self.current.children[folder_name] = new_folder
        return f"Carpeta '{folder_name}' creada exitosamente."

    def cd(self, folder_name):
        if folder_name == "..":
            if self.current.parent is not None:
                self.current = self.current.parent
                return f"Directorio actual: {self.current.name}"
            return "Ya estás en la raíz (root)."
        
        if folder_name in self.current.children and not self.current.children[folder_name].is_file:
            self.current = self.current.children[folder_name]
            return f"Directorio actual: {self.current.name}"
        
        return f"Error: Directorio '{folder_name}' no encontrado."

    def tree(self, node=None, indent=""):
        if node is None:
            node = self.root
            
        output = indent + ("|_ " if indent else "") + node.name + "\n"
        for child in node.children.values():
            output += self.tree(child, indent + "  ")
        return output