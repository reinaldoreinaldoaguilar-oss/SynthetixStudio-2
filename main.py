from command_invoker import CommandInvoker
from data_structures.n_ary_tree import NaryTree
from data_structures.expression_tree import ExpressionTree
from commands.workspace_cmds import MkdirCommand, CdCommand, TreeCommand
from commands.eval_cmd import EvalCommand

def main():
    # 1. Inicializamos las estructuras de datos (Árbol N-ario y Árbol Binario)
    workspace_tree = NaryTree()
    exp_tree = ExpressionTree()
    
    # 2. Inicializamos el invocador de comandos
    invoker = CommandInvoker()
    
    # 3. Registramos los comandos del Módulo 1 y 2 asociándolos a la palabra clave
    invoker.register("mkdir", MkdirCommand(workspace_tree))
    invoker.register("cd", CdCommand(workspace_tree))
    invoker.register("tree", TreeCommand(workspace_tree))
    invoker.register("eval", EvalCommand(exp_tree))

    print("=== Synthetix Studio (Mini IDE) ===")
    print("Comandos: mkdir <nombre>, cd <nombre> (o cd ..), tree, eval \"<expresion>\", exit\n")

    # 4. Bucle principal de la CLI
    while True:
        try:
            # Mostramos el prompt con el nombre del directorio actual
            user_input = input(f"{workspace_tree.current.name}> ")
            
            if user_input.strip() == "":
                continue
                
            if user_input.strip().lower() == "exit":
                print("Cerrando Synthetix Studio...")
                break

            # Ejecutamos a través del gestor de comandos
            resultado = invoker.execute_command(user_input)
            if resultado:
                print(resultado)
                
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()