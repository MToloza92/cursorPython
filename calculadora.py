"""
Santander Open Academy — Cursor con Python: desarrollo inteligente con IA

Calculadora de consola: input, conversión de tipos y decisiones.
Práctica con Cursor: depurar con IA (p. ej. división por cero y el hecho
de que input() devuelve texto, no números, hasta usar float()).
"""

numero1 = float(input("Ingrese el primer numero: "))
operacion = input("Ingrese la operacion: ")
numero2 = float(input("Ingrese el segundo numero: "))

# None = aún no hay resultado válido (error o operación desconocida).
resultado = None

if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    # Validar antes de dividir evita ZeroDivisionError.
    if numero2 == 0:
        print("Error: no se puede dividir entre cero.")
    else:
        resultado = numero1 / numero2
else:
    print("Operacion no valida")

if resultado is not None:
    print(f"El resultado es: {resultado}")

if operacion == "salir":
    print("Saliendo del programa...")
    exit()
