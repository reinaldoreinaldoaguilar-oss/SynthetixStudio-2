from commands.base_command import Command

class HelpCommand(Command):
    def execute(self, *args):
        help_text = """
=== Manual de Comandos (Synthetix Studio) ===

[Módulo 1: Explorador de Espacio de Trabajo]
  mkdir <carpeta>     : Crea un nuevo directorio en el nivel actual.
  cd <carpeta>        : Cambia el directorio de trabajo (Usa '..' para subir).
  tree                : Imprime la estructura jerárquica del proyecto en preorden.
  edit <archivo> <txt>: Crea/modifica un archivo físico y lo registra en el árbol.

[Módulo 2: Evaluador de Expresiones]
  eval "<expresion>"  : Parsea y evalúa una expresión matemática en postorden.
                        Ejemplo: eval "(4+8)*3"

[Módulo 3: Diccionario Rápido]
  add-keyword <token> : Inserta una palabra clave en el diccionario AVL autobalanceado.
  suggest <prefijo>   : Sugiere palabras en orden alfabético (inorden).

[Módulo 4: Búsqueda Global]
  index-all           : Escanea archivos virtuales y construye el Árbol B (m=4).
  find-global <token> : Busca en qué archivos y líneas se encuentra una variable.

[Sistema]
  help                : Muestra esta lista de comandos detallada.
  exit                : Cierra el entorno Synthetix Studio.
=============================================
"""
        return help_text