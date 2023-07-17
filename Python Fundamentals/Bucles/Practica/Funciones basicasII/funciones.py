'''
crea una función que acepte un número como entrada. 
Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]
'''
def countdown(numero):
    lista=[]
    for x in range(5,0, -1):
        lista.append(x)
    return lista

#print de prueba
print(countdown(5))

'''
crea una función que reciba una lista con dos números. 
Imprime el primer valor y devuelve el segundo.
Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2
'''
def imprimir_devolver(lista):
    print(lista[0])
    return lista[1]

#print de prueba
lista=[1,2]
print( imprimir_devolver(lista))

'''
crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)
'''
def primero_mas_longitud(lista):
    primer = lista[0]
    return primer + len(lista)
#print de prueba

print( primero_mas_longitud([1,2,3,4,5]) )

'''
Escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False
'''
def valores_mayores_que_el_segundo(lista):
    if len(lista) < 2:
        return False
    listaNueva = []
    segundo = lista[1]
    for elemento in lista:
        if elemento > segundo:
            listaNueva.append(elemento)
    print(len(listaNueva))
    return listaNueva

#print de prueba
print(valores_mayores_que_el_segundo([5,2,3,2,1,4]))
print(valores_mayores_que_el_segundo([3]))

'''
Escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]
'''
def length_and_value(tamaño, valor):
    lista=[]
    for x in range(0,tamaño):
        lista.append(valor)
    return lista
#print de prueba
print(length_and_value(4,7))
print(length_and_value(6,2))