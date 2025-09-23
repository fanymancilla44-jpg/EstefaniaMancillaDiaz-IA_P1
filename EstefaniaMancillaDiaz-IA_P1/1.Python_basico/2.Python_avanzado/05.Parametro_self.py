#--------------------------------------------------------#
# Curso avanzado de Python - Leccion 6: El parametro self
#--------------------------------------------------------#

#--------------------------------------------------------#
# Que es self
#--------------------------------------------------------#
# self es siempre el primer parametro en un metodo de clase.
# Representa al propio objeto.
# Gracias a self podemos acceder a los atributos y metodos del objeto.
# Aunque no pasemos self al llamar un metodo, Python lo pasa por nosotros.

# Ejemplo basico
class Mascota:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
    
    def saludar(self):
        print("Hola, soy", self.nombre, "y soy un", self.especie)

# Al crear un objeto, self se sustituye automaticamente por ese objeto
m1 = Mascota("Rocky", "perro")
m2 = Mascota("Michi", "gato")

m1.saludar()   # self -> m1
m2.saludar()   # self -> m2

#--------------------------------------------------------#
# Como funciona internamente
#--------------------------------------------------------#
# Cuando escribimos m1.saludar(), Python realmente hace:
# Mascota.saludar(m1)
# O sea, pasa el objeto m1 como primer argumento al metodo.

# Esto explica por que si no ponemos self, da error.

# Ejemplo incorrecto (esto da error):
# def saludar():
#     print("hola")
# Porque al llamar m1.saludar(), Python intenta pasar el objeto como argumento,
# pero el metodo no espera ninguno.

#--------------------------------------------------------#
# Usar self en metodos
#--------------------------------------------------------#
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def iniciar_sesion(self):
        print("El usuario", self.nombre, "ha iniciado sesion")

    def cumplir_anios(self):
        self.edad += 1
        print(self.nombre, "ahora tiene", self.edad, "anios")

u1 = Usuario("Ana", 20)
u2 = Usuario("Luis", 17)

u1.iniciar_sesion()
u2.iniciar_sesion()

u1.cumplir_anios()
u2.cumplir_anios()

#--------------------------------------------------------#
# self es solo una convencion
#--------------------------------------------------------#
# No es palabra reservada, podriamos usar otro nombre,
# pero no se recomienda porque seria confuso.
class Vehiculo:
    def __init__(este, marca, modelo):
        este.marca = marca
        este.modelo = modelo

    def mostrar(este):
        print("Vehiculo:", este.marca, este.modelo)

v1 = Vehiculo("Nissan", "Versa")
v1.mostrar()

# Aunque funcione, lo comun y recomendable es usar siempre "self".

# Recordemos:
# self es el primer parametro de todo metodo en una clase.
# Representa al objeto que llama al metodo.
# Sirve para acceder a atributos y metodos del propio objeto.
# Python pasa self de manera automatica al ejecutar metodos.
# Aunque se pueda cambiar el nombre de self, no es buena idea.
