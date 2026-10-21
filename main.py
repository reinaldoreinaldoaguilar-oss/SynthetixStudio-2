from command_invoker import CommandInvoker
from data_structures.n_ary_tree import NaryTree
from data_structures.expression_tree import ExpressionTree
from data_structures.avl_tree import AVLTree # <--- Importación
from commands.workspace_cmds import MkdirCommand, CdCommand, TreeCommand
from commands.eval_cmd import EvalCommand
from commands.dictionary_cmds import AddKeywordCommand, SuggestCommand # <--- Importación

def main():
    # 1. Inicializamos las estructuras
    workspace_tree = NaryTree()
    exp_tree = ExpressionTree()
    avl_tree = AVLTree() # <--- Inicializar Árbol AVL
    
    # 2. Inicializamos el invocador
    invoker = CommandInvoker()
    
    # 3. Registramos comandos
    invoker.register("mkdir", MkdirCommand(workspace_tree))
    invoker.register("cd", CdCommand(workspace_tree))
    invoker.register("tree", TreeCommand(workspace_tree))
    invoker.register("eval", EvalCommand(exp_tree))
    
    # Registrar nuevos comandos del Módulo 3
    invoker.register("add-keyword", AddKeywordCommand(avl_tree))
    invoker.register("suggest", SuggestCommand(avl_tree))

    print("=== Synthetix Studio (Mini IDE) ===")
    print("Comandos: mkdir, cd, tree, eval, add-keyword, suggest, exit\n")

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