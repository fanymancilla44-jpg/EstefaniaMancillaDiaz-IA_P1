#------------------------------------------------------------------#
# Curso de python basico - leccion 4: Palabras reservadas en python
#------------------------------------------------------------------#
# En python existen palabras que ya tienen un significado
# especial para el lenguaje. a esas se les llama
# **palabras reservadas** o **keywords**.

# Nota: No se pueden usar como nombre de variable,
# función o clase porque ya están ocupadas.

# Ejemplo (esto daría error):
# global = 10   # SyntaxError

# Lo correcto sería:
variable_global = 10
print("Ejemplo de variable válida:", variable_global)

# ------------------------------------------------------
# Para saber cuáles son esas palabras, podemos usar el
# modulo keyword, que trae python por defecto.
# ------------------------------------------------------

import keyword

print("\nPalabras reservadas en Python:")
print(keyword.kwlist)

# ------------------------------------------------------
# listado completo de las palabras reservadas
# ------------------------------------------------------

# and -sirve para comparar dos condiciones y devuelve True solo si ambas son verdaderas
x = True
y = False
print("\nEjemplo and:", x and y)  # False

# or -devuelve True si al menos una de las condiciones es verdadera
print("Ejemplo or:", x or y)  # True

# not -invierte el valor lógico (True se vuelve False y al revés)
print("Ejemplo not:", not x)  # False

# if -sirve para hacer condiciones
if x:
    print("Ejemplo if: x es verdadero")

# elif - es como un "sino si" cuando hay varias condiciones
num = 10
if num < 5:
    print("num menor que 5")
elif num == 10:
    print("Ejemplo elif: num es igual a 10")

# else -se usa cuando ninguna condición anterior se cumple
if num < 5:
    print("menor que 5")
else:
    print("Ejemplo else: no se cumplió lo anterior")

# for -bucles, sirve para repetir código
for i in range(3):
    print("Ejemplo for:", i)

# while -otro tipo de bucle que se repite mientras se cumpla una condición
contador = 0
while contador < 2:
    print("Ejemplo while:", contador)
    contador += 1

# break -rompe un bucle antes de que termine
for i in range(5):
    if i == 3:
        break
    print("Ejemplo break:", i)

# continue -salta a la siguiente vuelta del bucle
for i in range(5):
    if i == 2:
        continue
    print("Ejemplo continue:", i)

# def -se usa para crear funciones
def saludar():
    print("Ejemplo def: Hola!")
saludar()

# return -se usa dentro de funciones para devolver un valor
def sumar(a, b):
    return a + b
print("Ejemplo return:", sumar(2, 3))

# class -define una clase (plantilla para crear objetos)
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
p = Persona("fany")
print("Ejemplo class:", p.nombre)

# import  -sirve para llamar modulos o librerias
import math
print("Ejemplo import: raíz cuadrada de 16 =", math.sqrt(16))

# from -se usa para importar solo una parte de un modulo
from math import pi
print("Ejemplo from:", pi)

# as -permite ponerle un "alias" a un modulo
import math as m
print("Ejemplo as:", m.sqrt(9))

# pass -se usa como marcador de "no hago nada todavía"
def funcion_vacia():
    pass

# try, except, finally  -se usan para manejar errores
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Ejemplo except: no se puede dividir entre cero")
finally:
    print("Ejemplo finally: este bloque siempre se ejecuta")

# raise -sirve para lanzar un error manualmente
# raise ValueError("ejemplo raise: error provocado")
#Lo comento porque rompe la ejecución

# True, False, None → valores especiales
print("Ejemplo True y False:", True, False)
print("Ejemplo None:", None)

# lambda -funciones anonimas (rapidas)
doble = lambda x: x * 2
print("Ejemplo lambda:", doble(4))