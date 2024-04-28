'''
Ejercicio de aprendizaje en Python #5
Secuencia de numeros primos
Descripcion:
    ejercicio simple en el cual se le pide al usuario que ingrese un numero y se imprimira en pantalla una lista de numeros primos
    que empieza desde el 0 hasta el numero dado por el usuario
'''
#Librerias a ocupar
from math import isqrt
'''
Funcion es_primo
Descripcion: valida si el numero ingresado es primo o no
Devuelve:BOOLEAN
'''
def EsPrimo(n):
    # Los números menores que 2 no son primos
    if n < 2:
        return False
    # Itera desde 2 hasta la raíz cuadrada de n
    for i in range(2, isqrt(n) + 1):
        # Si n es divisible por i, no es primo
        if n % i == 0:
            return False
    # Si no se encontraron divisores, n es primo
    return True

'''
Funcion ListaPrimos
Descripcion: imprime la lista de numeros primos hasta el numero dado por el usuario
Devuelve:BOOLEAN
'''
def listaPrimos (numero):
    for n in range (1,numero):
        if (EsPrimo(n)):
            print(n)
#empieza programa principal        
print("Lista de numeros Primos")
numero_str=input("ingresa hasta que numero deseas que llegue la lista")
numero=int(numero_str)
listaPrimos(numero)

