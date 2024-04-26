'''
Ejercicio de aprendizaje en Python #3
Fibonacci
Descripcion:
    ejercicio simple en el cual se le pide al usuario un numero y se mostrara la serie fibonacci hasta el numero ingresado
'''
#Librerias a ocupar
from math import pow, sqrt
#Constantes Definidas
NUMERO_EULIANO=1.618033988749895
'''
Funcion SerieFib
Descripcion: Ejecuta la serie fibonacci N numero de veces solicitadas
Devuelve:
'''
def SerieFib(numero):
    for n in range (0,numero):
        resultado=(pow(NUMERO_EULIANO,n) -pow( (1 - NUMERO_EULIANO) ,n) )/ sqrt(5)#Formula que calcula el numero fibonacci
        print (n,".- ",int(resultado))#se imprime el resultado casteandolo a entero

#empieza el programa
print ("Serie Fibonacci")
numero_str=input("Por favor,hasta que numero deseas ver la serie fibonacci ")#se pide el numero al usuario
numero_ent=int(numero_str)#se convierte de string a int
SerieFib(numero_ent)#se ejecuta


