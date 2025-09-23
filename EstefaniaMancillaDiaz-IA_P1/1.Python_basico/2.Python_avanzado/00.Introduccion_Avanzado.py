#-----------------------------------------------------------------------------------#
# Curso avanzado de Python - Leccion 1: Introduccion a OOP, modularidad y defensiva
#-----------------------------------------------------------------------------------#

# Aqui ya no veremos lo basico, sino cosas que ayudan a programar de forma mas seria.
# Los temas principales son:
# 1. Programacion Orientada a Objetos (OOP)
# 2. Programacion modular
# 3. Programacion defensiva y depuracion
# Tambien se ven funciones mas avanzadas y un poco de matematicas y logica.

#--------------------------------------------------------#
# Requisitos para este curso
#--------------------------------------------------------#
# Antes de meterse a lo avanzado hay que tener bases.
# Saber usar Python con lo basico: variables, bucles, condicionales y funciones.
# Tambien saber cosas sencillas como crear carpetas, instalar programas y navegar en internet.
# Si todavia no sabes eso, primero conviene repasar lo basico.

#--------------------------------------------------------#
# Programacion orientada a objetos (OOP)
#--------------------------------------------------------#
# OOP significa trabajar con clases y objetos.
# Una clase es como un molde y los objetos son los "productos" que salen de ese molde.
# Con OOP podemos organizar mejor el codigo.

# Ejemplo sencillo de clase y objeto:
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print("Hola, soy", self.nombre, "y tengo", self.edad, "anios.")

persona1 = Persona("Ana", 20)
persona1.saludar()

#--------------------------------------------------------#
# Programacion modular
#--------------------------------------------------------#
# Cuando un programa es muy grande, se divide en partes llamadas modulos.
# Cada modulo es un archivo .py y se pueden importar unos a otros.
# Python tambien tiene modulos ya hechos, como math.

import math
print("La raiz cuadrada de 16 es:", math.sqrt(16))

#--------------------------------------------------------#
# Funciones avanzadas
#--------------------------------------------------------#
# Ademas de las funciones normales, Python tiene cosas como:
# - Funciones lambda (que son funciones rapidas en una sola linea)
# - Decoradores, generadores e iteradores (esto se ve mas adelante)

# Ejemplo de lambda:
doble = lambda x: x * 2
print("El doble de 5 es:", doble(5))

#--------------------------------------------------------#
# Programacion defensiva y depuracion
#--------------------------------------------------------#
# Aqui la idea es adelantarse a los errores.
# En Python se usan try y except para manejar problemas en el codigo.

try:
    numero = int("hola")  # esto va a dar error
except ValueError:
    print("Error: no se puede convertir a numero")
finally:
    print("Esto siempre se ejecuta")

#--------------------------------------------------------#
# Matematicas y logica de programacion
#--------------------------------------------------------#
# La logica y las matematicas son importantes para resolver problemas.
# Sirven para pensar paso a paso y estructurar mejor el codigo.

for i in range(1, 4):
    print(f"Tabla del {i}:")
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)

# En fin este curso avanzado de Python trata sobre:
# Clases y objetos
# Uso de modulos y organizacion del codigo
# Funciones mas avanzadas
# Programacion defensiva para manejar errores
# Matematicas y logica aplicada a la programacion
# Con esto se empieza a pasar de lo basico a algo mas avanzado.
