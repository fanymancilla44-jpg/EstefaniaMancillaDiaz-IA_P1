#----------------------------------------------------------------#
# Curso avanzado de Python - Leccion 8: Encapsulamiento en clases
#----------------------------------------------------------------#

# El encapsulamiento es la idea de agrupar atributos y metodos
# dentro de una clase. Es como meter todo en una "capsula".
# En Python no es tan estricto como en otros lenguajes (Java),
# pero usamos guiones bajos para marcar la visibilidad.

#--------------------------------------------------------#
# Tipos de acceso en Python
#--------------------------------------------------------#
# Publico      -> sin guion bajo
# Protegido    -> _atributo
# Privado      -> __atributo

class Usuario:
    def __init__(self, id, nombre, clave):
        self.id = id            # publico
        self._nombre = nombre   # protegido
        self.__clave = clave    # privado

# Creamos un objeto
u1 = Usuario(1, "Ana", "1234")

# Acceso publico
print(u1.id)        # funciona
# Acceso protegido
print(u1._nombre)   # funciona pero no deberiamos usarlo fuera
# Acceso privado
# print(u1.__clave) # da error

#--------------------------------------------------------#
# Metodo publico para acceder a un atributo privado
#--------------------------------------------------------#
class Usuario2:
    def __init__(self, nombre, clave):
        self.nombre = nombre
        self.__clave = clave

    def mostrar_clave(self):  # getter
        print("La clave es:", self.__clave)

    def cambiar_clave(self, nueva):  # setter
        self.__clave = nueva

u2 = Usuario2("Luis", "abcd")
u2.mostrar_clave()   # accede con metodo
u2.cambiar_clave("xyz")
u2.mostrar_clave()

#--------------------------------------------------------#
# Encapsulamiento con herencia
#--------------------------------------------------------#
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad  # protegido

class Perro(Animal):
    def mostrar(self):
        print("Tengo", self._edad, "anios")

p1 = Perro("Rocky", 5)
p1.mostrar()        # accede a atributo protegido
print(p1._edad)     # posible pero no recomendado

#--------------------------------------------------------#
# Ejemplo con metodo privado
#--------------------------------------------------------#
class Persona:
    def __init__(self, nombre, altura_cm):
        self.nombre = nombre
        self.altura_cm = altura_cm
    
    def __altura_metros(self):   # metodo privado
        return self.altura_cm / 100
    
    def mostrar_altura(self):    # metodo publico
        print("Altura en metros:", self.__altura_metros())

pe1 = Persona("Marta", 170)
pe1.mostrar_altura()

#Recordemos:
# Publico: libre acceso.
# Protegido (_): acceso desde clase o subclase.
# Privado (__): acceso solo en la clase.
# Podemos usar getters y setters para manejar privados.
# En Python son convenciones, no reglas estrictas.
