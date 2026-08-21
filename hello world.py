"""
Santander Open Academy — Cursor con Python: desarrollo inteligente con IA

Primer contacto con el editor: Tab completa bucles y funciones; el chat
explica qué hace cada línea. Objetivo: ver que la IA acelera código
sencillo, pero hay que leer y ejecutar lo generado.
"""

print("Hello, World!")

# range(10) produce 0..9; útil para comprobar que el script corre en Cursor.
for i in range(10):
    print(i)


def enumerar_pares():
    """Imprime pares de 2 a 40. Práctica de funciones y range con paso."""
    for i in range(2, 41, 2):
        print(i)


enumerar_pares()
