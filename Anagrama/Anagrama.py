'''
Ejercicio de aprendizaje en Python #2
Anagrama
Descripcion:
    ejercicio simple en el cual se le pide al usuario que ingrese una palabra y se determinara si es un palindromo o no
'''
def verificarPalabra(palabra):
    palabra = palabra.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios en blanco
    tamano = len(palabra)
    for i in range(tamano // 2):  # Iterar hasta la mitad de la palabra
        if palabra[i] != palabra[tamano - i - 1]:  # Comprobar simetría
            return False
    return True

palabra = input("Por favor, ingresa una palabra o frase para verificar si es palíndromo: ")

if verificarPalabra(palabra):
    print("La palabra o frase '{}' es un palíndromo.".format(palabra))
else:
    print("La palabra o frase '{}' NO es un palíndromo.".format(palabra))
