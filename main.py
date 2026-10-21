from command_invoker import CommandInvoker
from data_structures.n_ary_tree import NaryTree
from data_structures.expression_tree import ExpressionTree
from data_structures.avl_tree import AVLTree
from data_structures.b_tree import BTree
from commands.workspace_cmds import MkdirCommand, CdCommand, TreeCommand
from commands.eval_cmd import EvalCommand
from commands.dictionary_cmds import AddKeywordCommand, SuggestCommand
from commands.search_cmds import IndexAllCommand, FindGlobalCommand
from commands.help_cmd import HelpCommand 

def main():
    # 1. Inicializamos todas las estructuras del proyecto
    workspace_tree = NaryTree()
    exp_tree = ExpressionTree()
    avl_tree = AVLTree()
    b_tree = BTree(t=2) # t=2 asegura orden m=4 (max 3 claves)
    
    # 2. Inicializamos el invocador
    invoker = CommandInvoker()
    
    # 3. Registramos todos los comandos
    invoker.register("mkdir", MkdirCommand(workspace_tree))
    invoker.register("cd", CdCommand(workspace_tree))
    invoker.register("tree", TreeCommand(workspace_tree))
    invoker.register("eval", EvalCommand(exp_tree))
    invoker.register("add-keyword", AddKeywordCommand(avl_tree))
    invoker.register("suggest", SuggestCommand(avl_tree))
    invoker.register("index-all", IndexAllCommand(b_tree))
    invoker.register("find-global", FindGlobalCommand(b_tree))
    
    # Registrar el comando Help
    invoker.register("help", HelpCommand())

    print("=== Synthetix Studio (Mini IDE) ===")
    print("Escribe 'help' para ver la lista de comandos disponibles, o 'exit' para salir.\n")

    # 4. Bucle principal
    while True:
        try:
            user_input = input(f"{workspace_tree.current.name}> ")
            
            if user_input.strip() == "":
                continue
                
            if user_input.strip().lower() == "exit":
                print("Cerrando Synthetix Studio...")
                break

            resultado = invoker.execute_command(user_input)
            if resultado:
                print(resultado)
                
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()