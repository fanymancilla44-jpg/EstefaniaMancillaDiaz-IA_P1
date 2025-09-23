#--------------------------------------------------------#
# Curso de python basico - leccion 10: listas en python
#--------------------------------------------------------#

# Las listas sirven para guardar varios datos en una sola variable.
# Es como una cajita que puede almacenar varios valores al mismo tiempo.
# Lo padre de las listas en Python es que pueden tener diferentes tipos de datos
# mezclados, como numeros, textos, decimales e incluso otras listas.

# Ejemplo 1: lista basica
camiseta = ["rojo", "L", 100, 10]
print(camiseta)  # muestra todos los valores juntos en forma de lista

# A diferencia de otros lenguajes como Java, donde los arrays
# solo pueden guardar un mismo tipo de dato, en Python
# podemos mezclar tipos sin problema.

# Ejemplo 2: lista con varios tipos de datos
mi_lista = ["hola", 25, 3.14, True]
print(mi_lista)

#--------------------------------------------------------#
# Indices en las listas
#--------------------------------------------------------#
# Cada elemento de la lista tiene un "indice" (una posicion).
# El indice empieza desde 0.
# Ejemplo:
colores = ["azul", "verde", "rojo"]
print(colores[0])  # posicion 0 -> "azul"
print(colores[1])  # posicion 1 -> "verde"
print(colores[2])  # posicion 2 -> "rojo"

# Si tratamos de usar una posicion que no existe, Python nos dara error.
# Ejemplo (esto da error): print(colores[7])

#--------------------------------------------------------#
# Cambiar valores en una lista
#--------------------------------------------------------#
# Podemos cambiar un valor de la lista usando su indice:
colores[0] = "amarillo"
print(colores)  # ahora la lista es ['amarillo', 'verde', 'rojo']

# si reasignas la lista completa, ya no sera lista, sino el valor nuevo:
colores = "amarillo"
print(colores)  # aqui ya no es lista, ahora es solo un string

#--------------------------------------------------------#
# Metodos importantes de las listas
#--------------------------------------------------------#

# append() -> anade un elemento al final
colores = ["azul", "verde", "rojo"]
colores.append("amarillo")
print(colores)  # ['azul', 'verde', 'rojo', 'amarillo']

# insert() -> inserta un elemento en una posicion especifica
colores = ["azul", "verde", "rojo"]
colores.insert(0, "amarillo")
print(colores)  # ['amarillo', 'azul', 'verde', 'rojo']

# extend() -> une dos listas
colores1 = ["azul", "verde", "rojo"]
colores2 = ["amarillo", "naranja", "marron"]
colores1.extend(colores2)
print(colores1)  # ['azul', 'verde', 'rojo', 'amarillo', 'naranja', 'marron']

# pop() -> elimina un elemento de la lista
colores = ["azul", "verde", "rojo"]
colores.pop()  # elimina el ultimo
print(colores)  # ['azul', 'verde']
colores.pop(0)  # elimina el de la posicion 0
print(colores)  # ['verde']

# remove() -> elimina un valor literal especifico
colores = ["rojo", "azul", "rojo", "verde"]
colores.remove("rojo")  # elimina SOLO el primer "rojo"
print(colores)  # ['azul', 'rojo', 'verde']

# index() -> busca la posicion de un valor
numeros = [87, 10, 5, 7, 378, 10]
posicion = numeros.index(10)  # devuelve 1 (posicion del primer 10)
print("El numero 10 esta en la posicion:", posicion)

# count() -> cuenta cuantas veces aparece un valor
coincidencias = numeros.count(10)
print("El numero 10 aparece", coincidencias, "veces")

#--------------------------------------------------------#
# Recordemos:
# Una lista se crea con corchetes [] y puede guardar varios valores.
# Los indices empiezan en 0.
# Podemos modificar sus elementos y usar metodos como append, insert, extend,
# pop, remove, index y count.
# Son super utiles para agrupar datos relacionados.

