'''
Ejercicio de aprendizaje en Python #1
Fizz Buzz
Descripcion:
    ejercicio simple en el cual se hace una numeracion del 1 al 100 y se debe analizar lo siguiente:
    si el numero es multiplo de 3 en vez de imprimir el numero se imprime la palabra Fizz, si el numero
    es divisible entre 5 se escribe la palabra Buzz y si el numero es divisible tanto con 3 y 5
    se escribe la palabra Fizz Buzz
'''

'''
funcion divisible 3
    descripcion: determina si el numero que le pasas es divisible entre 3
    Devuelve: Boolean
'''
def divisible3(numero):
    if (numero % 3 == 0):
        return True
    else:
        return False
'''
funcion divisible 3
    descripcion: determina si el numero que le pasas es divisible entre 3
    Devuelve: Boolean
'''
def divisible5 (numero):
    if (numero %5 ==0):
        return True
    else:
        return False
'''
    funcion secuencia
    descripcion: crea una numeracion del 1 al 100 y en cada numero verifica si es divisible entre 3, 5 o ambos
    Devuelve: 
'''   
def secuencia ():
    for numero in range (1,101):
        if (divisible3(numero) & divisible5(numero) ):
            print ("Fiz Buzz")
        elif (divisible3(numero)):
            print("Fizz")
        elif (divisible5(numero)):
            print("Buzz")
        else:
            print(numero)
#Empieza programa
secuencia()    