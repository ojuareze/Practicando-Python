'''
Clase Calculadora
Descripcion:
    clase en la cual se establecen las funciones de Suma, Resta, Multiplicacion, Division, Potencia y Raiz Cuadrada de una calculadora basica
    
'''
#Declaraciond e librerias
from math import pow, sqrt

class Calculadora:
    def __init__(self) :
        pass
    '''
    Funcion Suma
    Descripcion: Suma 2 numeros dados
    Devuelve: Resultado de la suma de 2 numeros
    '''  
    def Suma (numero1,numero2):
        resultado = numero1+numero2
        return resultado
    '''
    Funcion Resta
    Descripcion: Resta 2 numeros dados
    Devuelve: Resultado de la resta de 2 numeros
    '''     
    def Resta (numero1,numero2):
        resultado = numero1-numero2
        return resultado
    '''
    Funcion Multiplicacion
    Descripcion: Multiplica 2 numeros dados
    Devuelve: Resultado de la multiplicacion de 2 numeros
    '''     
    def Multiplicacion (numero1,numero2):
        resultado = numero1*numero2
        return resultado
    '''
    Funcion Division
    Descripcion: divide 2 numeros dados
    Devuelve: Resultado de la division de 2 numeros
    '''     
    def Division (numero1,numero2):
        resultado = numero1/numero2
        return resultado
    '''
    Funcion RaizCuadrada
    Descripcion: ejecuta la operacion raiz cuadrada a un numero dado
    Devuelve: Resultado de la raiz del numero
    '''     
    def RaizCuadrada (numero):
        resultado = sqrt(numero)#ocupamos la libreria de math
        return resultado
    '''
    Funcion Potencia
    Descripcion: ejecuta la pontencia de un numero al cuadrado por defecto
    Devuelve: Resultado de la petencia
    '''     
    def Potencia (numero):
        resultado = pow(numero,2)#ocupamos la libreria math
        return resultado