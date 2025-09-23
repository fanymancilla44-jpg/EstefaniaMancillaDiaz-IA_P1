#--------------------------------------------------------#
# Curso avanzado de Python - Leccion 3:
# Introduccion a las clases en Python
#--------------------------------------------------------#

#--------------------------------------------------------#
# Que es una clase
#--------------------------------------------------------#
# Una clase es como una plantilla que sirve para crear objetos.
# Los objetos representan cosas del mundo real o imaginario.
# Clase en ingles se dice "class".

#--------------------------------------------------------#
# Sintaxis basica de una clase
#--------------------------------------------------------#
# Se usa la palabra reservada class y un nombre con mayusculas iniciales (CapWords).

class PersonaEjemplo():
    # aqui podria ir codigo de la clase
    pass

#--------------------------------------------------------#
# Convencion de nombres
#--------------------------------------------------------#
# Por regla de estilo (PEP8), las clases se nombran en CapWords.
# Ejemplo correcto: MiClase, CocheDeportivo
# Ejemplo incorrecto: mi_clase, coche_deportivo

#--------------------------------------------------------#
# Uso de pass en clases
#--------------------------------------------------------#
# Si quieres declarar la clase pero todavia no escribir el codigo, se usa pass.
class Animal():
    pass

#--------------------------------------------------------#
# Atributos y metodos
#--------------------------------------------------------#
# Atributos: variables dentro de la clase.
# Metodos: funciones dentro de la clase.

class Coche():
    # Atributos
    marca = None
    modelo = None
    ruedas = 4

    # Metodos
    def encender(self):
        print("El coche esta encendido")

    def apagar(self):
        print("El coche esta apagado")

# Creamos objetos de tipo Coche
c1 = Coche()
c2 = Coche()

c1.marca = "Nissan"
c1.modelo = "Versa"
c2.marca = "Toyota"
c2.modelo = "Corolla"

print("Coche 1:", c1.marca, c1.modelo)
print("Coche 2:", c2.marca, c2.modelo)

c1.encender()
c2.apagar()

#--------------------------------------------------------#
# Otro ejemplo de clase (mas simple)
#--------------------------------------------------------#
class Estudiante():
    nombre = None
    edad = None
    
    def presentarse(self):
        print("Hola, me llamo", self.nombre, "y tengo", self.edad, "anios.")

e1 = Estudiante()
e1.nombre = "Luis"
e1.edad = 17
e1.presentarse()

#--------------------------------------------------------#
# type() para comprobar clases
#--------------------------------------------------------#
# En Python todo es un objeto. Podemos ver de que clase es cada cosa.

print(type("Hola"))     # str
print(type(25))         # int
print(type(3.14))       # float

# Los objetos tienen metodos ya definidos.
texto = "aprender python"
print(texto.upper())  # convierte el texto a MAYUSCULAS
#Recordemos:
# Una clase es un molde para crear objetos.
# Los objetos tienen atributos (datos) y metodos (acciones).
# Se nombran con CapWords segun la guia PEP8.
# Python ya trae clases internas como str, int, list, etc.
# Con clases podemos reutilizar y organizar mejor el codigo.
