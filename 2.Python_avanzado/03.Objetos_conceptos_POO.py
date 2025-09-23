#--------------------------------------------------------#
# Curso avanzado de Python - Leccion 4: Objetos en Python
#--------------------------------------------------------#

#--------------------------------------------------------#
# Que es un objeto
#--------------------------------------------------------#
# Un objeto es algo que se crea a partir de una clase.
# Tiene atributos (datos) y metodos (acciones).
# En ingles objeto se dice "object".

#--------------------------------------------------------#
# Ejemplo basico de objeto
#--------------------------------------------------------#
class Animal():
    especie = None
    edad = None

    def hacer_sonido(self):
        print("Este animal hace un sonido generico")

# Creamos un objeto (instancia) de la clase Animal
perro = Animal()
gato = Animal()

# Cambiamos los atributos de cada objeto
perro.especie = "Perro"
perro.edad = 3
gato.especie = "Gato"
gato.edad = 2

print(perro.especie, "tiene", perro.edad, "anios")
print(gato.especie, "tiene", gato.edad, "anios")

# Llamamos al metodo
perro.hacer_sonido()
gato.hacer_sonido()

#--------------------------------------------------------#
# Estado, comportamiento e identidad
#--------------------------------------------------------#
# - Estado: son los atributos (ejemplo: nombre, edad, especie).
# - Comportamiento: son los metodos (ejemplo: correr, saltar).
# - Identidad: el nombre del objeto en el codigo (perro, gato).

# Otro ejemplo:
class Usuario():
    nombre = None
    edad = None
    
    def iniciar_sesion(self):
        print(self.nombre, "ha iniciado sesion")

    def cerrar_sesion(self):
        print(self.nombre, "ha cerrado sesion")

u1 = Usuario()
u2 = Usuario()

u1.nombre = "Ana"
u1.edad = 20
u2.nombre = "Luis"
u2.edad = 17

u1.iniciar_sesion()
u2.cerrar_sesion()

#--------------------------------------------------------#
# Reasignar valores a atributos
#--------------------------------------------------------#
# Podemos modificar el estado de un objeto en cualquier momento.

u1.edad = 21
print(u1.nombre, "ahora tiene", u1.edad, "anios")

#--------------------------------------------------------#
# Crear atributos nuevos en un objeto
#--------------------------------------------------------#
# Es posible crear atributos que no existian en la clase,
# pero solo viviran en ese objeto especifico.

u1.correo = "ana123@mail.com"
print("Correo de", u1.nombre, ":", u1.correo)

# Si intentamos acceder al atributo en otro objeto dara error.
# print(u2.correo)  # Esto marcaria error porque u2 no tiene correo

#--------------------------------------------------------#
# Instanciacion
#--------------------------------------------------------#
# A la accion de crear un objeto a partir de una clase se le llama instanciar.
# Y cada objeto creado es una instancia de esa clase.

class Producto():
    nombre = None
    precio = None

p1 = Producto()
p2 = Producto()

p1.nombre = "Lapiz"
p1.precio = 5
p2.nombre = "Cuaderno"
p2.precio = 30

print("Producto:", p1.nombre, "Precio:", p1.precio)
print("Producto:", p2.nombre, "Precio:", p2.precio)

#--------------------------------------------------------#
# Direccion de memoria de un objeto
#--------------------------------------------------------#
# Cuando imprimimos un objeto directamente, Python nos muestra
# en que direccion de memoria fue guardado.
print(p1)
print(p2)
#Recordemos:
# Un objeto es creado a partir de una clase.
# Estado = atributos, Comportamiento = metodos, Identidad = nombre del objeto.
# Se pueden reasignar atributos y tambien crear nuevos (aunque no es recomendable).
# Cada objeto es una instancia de una clase.
# Los objetos viven en memoria mientras el programa esta en ejecucion.
