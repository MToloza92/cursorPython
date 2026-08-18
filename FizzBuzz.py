#Fizzbuzz#
#imprimir los numeros del 1 al 100
#si el numero es divisible por 3, imprimir Fizz
#si el numero es divisible por 5, imprimir Buzz
#si el numero es divisible por 3 y 5, imprimir FizzBuzz
#si el numero no es divisible por 3 ni 5, imprimir el numero
for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)