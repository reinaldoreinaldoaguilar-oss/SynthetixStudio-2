from commands.base_command import Command

class EvalCommand(Command):
    def __init__(self, exp_tree_parser):
        self.parser = exp_tree_parser

    def execute(self, *args):
        if not args:
            return 'Error: Falta la expresión matemática. Uso: eval "(4+8)*3"'
        
        expresion = "".join(args).replace('"', '').replace("'", "")
        
        try:
            resultado = self.parser.evaluate(expresion)
            
            if resultado.is_integer():
                resultado = int(resultado)
                
            return f"Resultado: {resultado}"
        except Exception as e:
            return f"Error al evaluar la expresión: {e}"