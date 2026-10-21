from command_invoker import CommandInvoker
from data_structures.n_ary_tree import NaryTree
from data_structures.expression_tree import ExpressionTree
from data_structures.avl_tree import AVLTree
from data_structures.b_tree import BTree
from commands.mkdir_command import MkdirCommand
from commands.cd_command import CdCommand
from commands.tree_command import TreeCommand
from commands.eval_cmd import EvalCommand
from commands.add_keyword_command import AddKeywordCommand
from commands.suggest_command import SuggestCommand
from commands.index_all_command import IndexAllCommand
from commands.find_global_command import FindGlobalCommand
from commands.help_cmd import HelpCommand 
from commands.edit_command import EditCommand

def main():
    workspace_tree = NaryTree()
    exp_tree = ExpressionTree()
    avl_tree = AVLTree()
    b_tree = BTree(t=2) 
    
    invoker = CommandInvoker()
    
    invoker.register("mkdir", MkdirCommand(workspace_tree))
    invoker.register("cd", CdCommand(workspace_tree))
    invoker.register("tree", TreeCommand(workspace_tree))
    invoker.register("eval", EvalCommand(exp_tree))
    invoker.register("add-keyword", AddKeywordCommand(avl_tree))
    invoker.register("suggest", SuggestCommand(avl_tree))
    invoker.register("index-all", IndexAllCommand(b_tree))
    invoker.register("find-global", FindGlobalCommand(b_tree))
    invoker.register("help", HelpCommand())
    invoker.register("edit", EditCommand(workspace_tree))

    print("=== Synthetix Studio (Mini IDE) ===")
    print("Escribe 'help' para ver la lista de comandos disponibles, o 'exit' para salir.\n")

    while True:
        try:
            user_input = input(f"{workspace_tree.current.name}> ")
            if user_input.strip() == "": continue
            if user_input.strip().lower() == "exit":
                print("Cerrando Synthetix Studio...")
                break

            resultado = invoker.execute_command(user_input)
            if resultado: print(resultado)
                
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()