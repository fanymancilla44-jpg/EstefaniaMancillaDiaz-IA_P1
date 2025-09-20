#-------------------------------------------------------------------------#
# Curso de python basico - leccion 6: Entradas y salida de datos en python
#-------------------------------------------------------------------------#
"""
 la entrada de datos es el proceso de introducir información en un programa 
 desde una fuente externa, como el teclado (usando input()) o un archivo. 
 La salida de datos es el proceso de mostrar o escribir información 
 desde el programa
"""
#comenzamos con la salida(print())
print("hola mundo") #muestra el mensaje
dato = 10
print("Dato",dato) #muestra el mensaje y el valor
#print(*objects, sep=' ', end='\n', file=None, flush=False)
# objects nos permite un numero ilimitado de objetos
#esto pueden ser cadenas ,numero entero o decimales,etc
#sep es un parametro donde estan las comillas simples tenemos espacios automaticos entre el resultado final
#el end es un fin y el \n significa un salto de linea para que no quede pegado a lo anterior
#los \n son para dar orden en el codigo 

#la entrada(input())
#1cantidad = input("Pon una cantidad: ")
#es un espacion sin memoria donde escribimos lo que requiera
#guarda la informacion y ya hay una entrada de un tipo de dato
#con esto queda dentro del programa, es decir; esa informacion entra

#si implementamos las dos
# Entrada de datos
cantidad = input("Pon una cantidad: ") #entra el dato al programa
# Salida de datos
print("La cantidad almacenada es: ", cantidad ) #muestra mensaje y el dato

#tipos de datos de entradas
# Solicita dos números para sumar
numero_1 = input("Introduce el primer numero a sumar: ") #a una variable se solicita una entrada
numero_2 = input("Introduce el segundo numero a sumar: ")
# Realiza y guarda la suma
suma = numero_1 + numero_2
# Muestra el resultado
print(suma)