"""
Santander Open Academy — Cursor con Python: desarrollo inteligente con IA

Contador de palabras en un archivo de texto.
Práctica con Cursor: lectura de ficheros, try/except y expresiones regulares.
La IA suele sugerir encoding='utf-8' y FileNotFoundError; conviene
comprobar la ruta que escribe el usuario.
"""

import re

archivo = input("Ingrese la ruta del archivo: ")

try:
    with open(archivo, "r", encoding="utf-8") as file:
        texto = file.read()
except FileNotFoundError:
    print("El archivo no existe")
    exit()

# \w+ agrupa letras/números; lower() unifica MAYÚSCULAS y minúsculas.
palabras = re.findall(r"\w+", texto.lower())
total_palabras = len(palabras)

print(f"Total palabras: {total_palabras}")


def enumerar_pares():
    """Ejercicio extra de bucles (mismo patrón que hello world.py)."""
    for i in range(2, 41, 2):
        print(i)


enumerar_pares()
