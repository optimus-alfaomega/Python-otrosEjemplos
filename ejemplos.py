#Puntos clave

#1. Hay dos tipos de ciclos en Python: while y for:

#El ciclo while ejecuta una sentencia o un conjunto de declaraciones siempre que una condición booleana especificada sea verdadera, por ejemplo:

# Ejemplo 1
while True:
    print("Atascado en un ciclo infinito")

# Ejemplo 2
contador = 5
while contador > 2:
    print(contador)
    contador -= 1

#El ciclo for ejecuta un conjunto de sentencias muchas veces; se usa para iterar sobre una secuencia (por ejemplo, una lista, un diccionario, una tupla o un conjunto; pronto aprenderás sobre ellos) u otros objetos que son iterables (por ejemplo, cadenas). Puedes usar el ciclo for para iterar sobre una secuencia de números usando la función incorporada range. Mira los ejemplos a continuación:

# Ejemplo 1
palabra = "Python"
for letter in palabra:
    print(letter, fin = "*")

# Ejemplo 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

#2. Puedes usar las sentencias break y continue para cambiar el flujo de un ciclo:

#Utiliza break para salir de un ciclo, por ejemplo:

texto = "OpenEDG Python Institute"
for letter in texto:
    if letter == "P":
        break
    print(letter, end= "")

#Utiliza continue para omitir la iteración actual, y continuar con la siguiente iteración, por ejemplo:

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end= "")



#3. Los ciclos while y for también pueden tener una cláusula else en Python. La cláusula else se ejecuta después de que el ciclo finalice su ejecución siempre y cuando no haya terminado con break, por ejemplo:

n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")

#4. La función range() genera una secuencia de números. Acepta enteros y devuelve objetos de rango. La sintaxis de range() tiene el siguiente aspecto: range(start, stop, step), donde:

###start es un parámetro opcional que especifica el número de inicio de la secuencia (0 por defecto).
###stop es un parámetro opcional que especifica el final de la secuencia generada (no está incluido).
###y step es un parámetro opcional que especifica la diferencia entre los números en la secuencia es (1 por defecto).
###Código de ejemplo:

for i in range(3):
    print(i, end=" ") # salidas: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ") # salidas: 6, 4, 2
	
### RECORRIDO CON BUCLE FOR CON UNA LISTA EN PYTHON 
	

miLista = [10, 1, 8, 3, 5]
suma = 0

for i in miLista:
    suma += i

print(suma) 


### RECORRIDO CON BUCLE FOR CON UNA LISTA EN PYTHON 
miLista = [10, 1, 8, 3, 5]
suma = 0

for i in range(len(miLista)):
    suma += miLista[i]

print(suma)


#ordenamiento INVERTIR ELEMENTOS de una lista 

miLista = [10, 1, 8, 3, 5,30,85,63,25,4,33,7,2,56]
longitud = len(miLista)

for i in range (longitud // 2):
    miLista[i], miLista[longitud-i-1] = miLista[longitud-i-1], miLista[i]


print(miLista) 


#ordenamiento BURBUJA

miLista = [8, 10, 6, 2, 4] # lista para ordenar
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while

while swapped:
    swapped = False # no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
       
        if miLista[i] > miLista[i + 1]:
            swapped= True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]
            print(miLista)
			
#ordenamiento BURBUJA A LA MALPARIDEZ (recortado)			
miLista = [8, 10, 6, 2, 4]
miLista.sort() 
print(miLista) 
#ordenamiento BURBUJA A LA MALPARIDEZ inverso(recortado)			
miLista = [8, 10, 6, 2, 4]
miLista.reverse() 
print(miLista) 

