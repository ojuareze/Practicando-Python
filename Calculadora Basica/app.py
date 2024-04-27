'''
Ejercicio de aprendizaje en Python #4
Calculadora Basica
Descripcion:
    ejercicio en el cual se crea una calculadora con operaciones basicas con 2 numero dados por el usuario

'''
# Librerias a importar
from calculadora import Calculadora
import os
import subprocess

'''
Funcion limpiar_pantala()
Descripcion: limpia la pantalla de la terminal
Devuelve:
'''
def limpiar_pantalla():
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)#se manda a llamar mediante la biblioteca de subproces a clear y se evalua el SO en el que se encuentra para ejecutarlo apropiadamente
'''
Funcion Principal()
Descripcion: Ejecuta el programa principal en un buble infinito que solo termina al ejecutar la opcion 7
Devuelve:
'''
def Principal():
    while True:
        limpiar_pantalla()
        print('Programa Calculadora')
        print('por favor elije una opcion')
        opcion_str=input('''
                     1.-Suma
                     2.-Resta
                     3.-Multiplicacion
                     4.-Division
                     5.-Potencia
                     6.-Raiz Cuadrada
                     7.-Salir
                     ''')
        opcion=int(opcion_str)
        if(opcion==1):
            limpiar_pantalla()
            print("Suma de dos numeros")
            numero1_str=input("Ingresa primer numero: ")
            numero2_str=input("Ingresa segundo numero: ")
            numero1=int (numero1_str)
            numero2= int (numero2_str)
            resultado=Calculadora.Suma(numero1,numero2)#mandamos a llamar al metodo suma de la clase calculadora
            print(resultado)
            input("")
        elif(opcion == 2):
            limpiar_pantalla()
            print("Resta de dos numeros")
            numero1_str=input("Ingresa primer numero: ")
            numero2_str=input("Ingresa segundo numero: ")
            numero1=int (numero1_str)
            numero2= int (numero2_str)
            resultado=Calculadora.Resta(numero1,numero2)
            print(resultado)
            input("")
        elif(opcion == 3):
            limpiar_pantalla()
            print("Multiplicacion de dos numeros")
            numero1_str=input("Ingresa primer numero: ")
            numero2_str=input("Ingresa segundo numero: ")
            numero1=int (numero1_str)
            numero2= int (numero2_str)
            resultado=Calculadora.Multiplicacion(numero1,numero2)
            print(resultado)
            input("")
        elif (opcion == 4):
            limpiar_pantalla()
            print("Divison de dos numeros")
            numero1_str=input("Ingresa primer numero: ")
            numero2_str=input("Ingresa segundo numero: ")
            numero1=int (numero1_str)
            numero2= int (numero2_str)
            resultado=Calculadora.Division(numero1,numero2)
            print(resultado)
            input("")
        elif(opcion == 5):
            limpiar_pantalla()
            print("Potencia de un numero")
            numero1_str=input("Ingresa el numero: ")
            numero1=int (numero1_str)
            resultado=Calculadora.Potencia(numero1)
            print(resultado)
            input("")
        elif(opcion == 6):
            limpiar_pantalla()
            print("Raiz cuadrada de un numero")
            numero1_str=input("Ingresa el numero: ")
            numero1=int (numero1_str)
            resultado=Calculadora.RaizCuadrada(numero1)
            print(resultado)
            input("")
        elif(opcion == 7):
            break #interrumpimos el bloque
#inicia programa principal        
Principal()