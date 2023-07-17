#imprime todos los números enteros del 0 al 150.
for i in range(151):
    print(i)
# imprime todos los múltiplos de 5 entre 5 y 1,000.
for x in range(5,1001):
    if x % 5 == 0:
        print(x)
#imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
for x in range(1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print ("Coding")
    else:
        print(x)
#agrega los enteros impares del 0 al 500,000, e imprime la suma final.
contador = 0
for x in range(1,500001, 2):
    contador= contador + x
print("La suma de impares es:", contador)
#imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4. 
for x in range(2018,0,-4):
    print(x)
# establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean 
# múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 
lowNum= 2
highNum= 9
mult = 3
for x in range(lowNum, highNum + 1):
    if x % mult == 0:
        print(x)

