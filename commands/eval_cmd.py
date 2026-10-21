from commands.base_command import Command

class EvalCommand(Command):
    def __init__(self, exp_tree_parser):
        self.parser = exp_tree_parser

    def execute(self, *args):
        if not args:
            return 'Error: Falta la expresión matemática. Uso: eval "(4+8)*3"'
        
        # Unimos los argumentos por si el usuario dejó espacios y quitamos las comillas
        expresion = "".join(args).replace('"', '').replace("'", "")
        
        try:
            # Aquí es donde construimos el árbol y retornamos el resultado exacto
            resultado = self.parser.evaluate(expresion)
            
            # Formateamos para que no muestre ".0" si es un número entero
            if resultado.is_integer():
                resultado = int(resultado)
                
            return f"Resultado: {resultado}"
        except Exception as e:
            return f"Error al evaluar la expresión: {e}"