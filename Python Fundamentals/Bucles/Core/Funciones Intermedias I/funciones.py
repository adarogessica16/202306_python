'''
Actualizar valores en diccionarios y listas

'''
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Cambiar el valor 10 en x a 15
x[1][0] = 15

# Cambiar el "apellido" del primer alumno de 'Jordan' a 'Bryant'
estudiantes[0]['last_name'] = 'Bryant'

# En el directorio_deportes, cambiar "Messi" por "Andrés"
directorio_deportes['fútbol'][0] = 'Andrés'

# Cambiar el valor 20 en z a 30
z[0]['y'] = 30
# Imprimir los resultados actualizados
print(x)
print(estudiantes)
print(directorio_deportes)
print(z)

'''
2- Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, 
la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:
'''
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(diccionario):
    for x in diccionario:
        for key, value in x.items():
            print(f"{key} - {value}")

iterateDictionary(estudiantes) 

'''
3-Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, 
la función imprima el valor almacenado en esa clave para cada diccionario. 
'''
def iterateDictionary2(key_name, diccionario):
    for x in diccionario:
        if key_name in x:
            print(x[key_name])


iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes) 

'''
4- Iterar a través de un diccionarios con valores de lista
Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, 
imprima el nombre de cada clave junto con el tamaño de su lista, 
y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:
'''
def printInfo(diccionario):
    for key, value in diccionario.items():
        print(f"{len(value)} {key}:")
        for item in value:
            print(item)
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

