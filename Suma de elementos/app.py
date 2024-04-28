'''
Ejercicio de aprendizaje en Python #6
Suma de Elementos
Descripcion:
    ejercicio en el cual se le pide al usuario una lista de numeros, practicamente sin limite y al finalizar de
    ingresarlos se sumaran todos, para ello se ocupan listas para el manejo de los numeros
'''
'''
Funcion SolicitarNumeros
Descripcion: Funcion que solicita numeros al usuario y los agrega en una lista hasta que el usuario ingrese #
Devuelve:Lista []
'''
def SolicitarNumeros():
    lista=[]
    while True:
        numero_str=input("ingresar un numero a la lista, para terminar ingresa #")
        if (numero_str == '#'):
            return lista
        else:
          numero=int(numero_str)    
          lista.append(numero)
        
'''
Funcion SumaNumeros
Descripcion: Funcion en primera instancia verifica que la lista que recibe tenga algo, de no ser asi retorna 0
             si contiene algo suma los numeros que se encuentran dentro de ella y devuelve la sumatoria
Devuelve:int
'''
def  SumaNumeros(lista: list):
    if (len(lista)==0):
        return 0
    else:    
        resultado=0
        return sum(lista)#metodo que suma los elementos de la lista
# Programa pincipal
print ("Suma de elementos")
lista=[]
lista=SolicitarNumeros()
print("El resultado de la suma de los numeros es: ",SumaNumeros(lista))