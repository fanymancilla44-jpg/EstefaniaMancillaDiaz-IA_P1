#--------------------------------------------------------#
# Curso avanzado de Python - Leccion 2:
# Introduccion a la programacion orientada a objetos (POO)
#--------------------------------------------------------#

# Este tema es muy importante porque Python y muchos lenguajes modernos usan este estilo.
# Dominar POO se considera basico hoy en dia para cualquier programador.

#--------------------------------------------------------#
# Que es la programacion orientada a objetos
#--------------------------------------------------------#
# La idea principal es poder crear "objetos" con codigo.
# Estos objetos representan cosas de la vida real o imaginaria.
# Por ejemplo:
# Un personaje de videojuego con atributos como vida, fuerza y velocidad,
# y con comportamientos como correr, saltar o atacar.
# Un coche con atributos como color, modelo y velocidad,
# y comportamientos como frenar o acelerar.
# Un usuario de una aplicacion con nombre, edad, direccion,
# y acciones como iniciar sesion o cerrar sesion.

# Lo importante es que cada objeto tiene caracteristicas unicas,
# pero al mismo tiempo comparte cosas en comun con otros del mismo tipo.

#--------------------------------------------------------#
# Por que es importante POO
#--------------------------------------------------------#
# 1. En Python casi todo son objetos, asi que es fundamental entenderlos.
# 2. Ayuda a organizar mejor el codigo.
# 3. Facilita el mantenimiento de programas grandes.
# 4. Permite reutilizar codigo sin tener que escribirlo todo de nuevo.

#--------------------------------------------------------#
# Conceptos basicos que veremos en OOP
#--------------------------------------------------------#
# Clases
# Objetos
# Encapsulamiento
# Polimorfismo
# Herencia
# Abstraccion

#--------------------------------------------------------#
# Ejemplo simple de clase y objeto
#--------------------------------------------------------#
# Una clase es como un molde y el objeto es un "producto" hecho con ese molde.
# Aqui hacemos una clase Usuario para representar un usuario de una aplicacion.

class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print("Hola, soy", self.nombre, "y tengo", self.edad, "anios.")

# Creamos dos objetos diferentes con la misma clase
usuario1 = Usuario("Carlos", 18)
usuario2 = Usuario("Maria", 20)

usuario1.saludar()
usuario2.saludar()

# POO significa programacion orientada a objetos.
# Nos permite representar cosas reales en codigo.
# Es importante porque organiza, mantiene y reutiliza mejor el codigo.
# Lo basico de POO incluye: clases, objetos, herencia, polimorfismo,
# encapsulamiento y abstraccion.
