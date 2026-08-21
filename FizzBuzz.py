"""
Santander Open Academy — Cursor con Python: desarrollo inteligente con IA

Ejercicio clásico de condiciones (if / elif / else).
Práctica con Cursor: pedir el algoritmo al chat y revisar el orden de
las condiciones (primero 3 y 5 juntos; si no, FizzBuzz nunca se imprime).
"""

# Recorre 1 a 100. % es el resto de la división (0 = es múltiplo).
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
