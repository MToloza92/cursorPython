#Programa para contar palabras en un texto#


#pedir al usuaurio la ruta de un archivo
archivo = input("Ingrese la ruta del archivo: ")
try:
    with open(archivo, 'r', encoding='utf-8') as file:
        texto = file.read()
except FileNotFoundError:
    print("El archivo no existe")
    exit()

# Separar el contenido en palabras

import re

palabras = re.findall(r"\w+", texto.lower())

total_palabras = len(palabras)

print(f"Total palabras: {total_palabras}")






##funcion para enumerar pares hasta el 40##
def enumerar_pares():
    for i in range(2, 41, 2):
        print(i)

enumerar_pares()

