# 💻 Synthetix Studio - Mini IDE (Fase 2)

Un entorno de desarrollo minimalista construido estrictamente desde cero en Python, aplicando Programación Orientada a Objetos (POO) y el **Patrón de Diseño Comando (Command Pattern)**. Este proyecto implementa estructuras de datos jerárquicas sin el uso de librerías externas para gestionar un espacio de trabajo, evaluar expresiones matemáticas, autocompletar palabras clave y realizar búsquedas globales indexadas.

## 🚀 Módulos y Estructuras de Datos

1. **Explorador de Espacio de Trabajo (Árbol N-ario):**
   - Representa un sistema de archivos virtual con carpetas infinitamente anidadas.
   - Recorridos en preorden para visualización jerárquica (estilo comando `tree`).

2. **Evaluador de Expresiones (Árbol Binario Clásico):**
   - Parsea expresiones matemáticas utilizando el algoritmo *Shunting Yard*.
   - Evalúa los resultados matemáticos exactos mediante recorridos en postorden.

3. **Autocompletado y Diccionario Rápido (Árbol AVL):**
   - Árbol binario de búsqueda autobalanceable con tiempos de operación garantizados de $O(\log n)$.
   - Sugerencias alfabéticas mediante recorridos inorden.

4. **Índice de Búsqueda Global (Árbol B):**
   - Motor de búsqueda de alta eficiencia indexando variables y funciones (Orden $m=4$, $t=2$).
   - Almacena múltiples referencias y ubicaciones precisas (archivo y línea).

## ⚙️ Arquitectura
El proyecto sigue principios de código limpio:
- **Patrón Comando:** Cero uso de menús tradicionales o sentencias `if/elif` anidadas. Cada acción de la consola CLI está completamente desacoplada.
- **Single Responsibility Principle:** Estricta separación de la lógica, manejando un único nodo o comando por archivo físico.
- **Manejo de Archivos:** Capacidad de crear y modificar archivos `.txt` o `.py` físicamente desde la consola virtual interactiva.

## 🛠️ Instalación y Uso

1. Clona este repositorio o descarga los archivos.
2. Abre una terminal (CMD o PowerShell) en la ruta principal del proyecto.
3. Ejecuta el archivo principal:
   ```bash
   python main.py