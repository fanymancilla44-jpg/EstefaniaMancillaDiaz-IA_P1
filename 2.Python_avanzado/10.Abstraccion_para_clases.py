#--------------------------------------------------------------#
# Curso avanzado de Python - Leccion 10: Abstraccion en clases
#--------------------------------------------------------------#

# La abstraccion significa ocultar los detalles internos
# de como funciona algo, y mostrar solo lo importante.
# Ejemplo real: para manejar un coche solo usas volante,
# pedales y palanca. No necesitas saber como funciona el motor.

#--------------------------------------------------------#
# Diferencia entre encapsulamiento y abstraccion
#--------------------------------------------------------#
# Encapsulamiento: oculta los datos internos y organiza
# todo dentro de la clase (atributos + metodos).
# Abstraccion: muestra solo lo esencial al usuario,
# sin que sepa como esta implementado.

#--------------------------------------------------------#
# Clases abstractas en Python
#--------------------------------------------------------#
# Para crear clases abstractas usamos abc y @abstractmethod.
# Una clase abstracta NO puede usarse directamente,
# solo sirve como modelo para otras clases.
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass

# Las subclases estan obligadas a implementar hablar()
class Perro(Animal):
    def hablar(self):
        print("woof")

class Gato(Animal):
    def hablar(self):
        print("miau")

p = Perro()
g = Gato()
p.hablar()
g.hablar()

#--------------------------------------------------------#
# Que pasa si no implementamos el metodo hablar?
#--------------------------------------------------------#
class Pez(Animal):
    pass

# Si intentamos usar Pez, da error porque falta hablar():
# pez = Pez()   # <- TypeError

# Recordemos:
# Abstraccion: te concentras en que hace un objeto,
# no en como lo hace.
# Usamos clases abstractas para obligar a las subclases
# a implementar ciertos metodos.
# Ventajas: codigo mas simple, reutilizable y organizado.
