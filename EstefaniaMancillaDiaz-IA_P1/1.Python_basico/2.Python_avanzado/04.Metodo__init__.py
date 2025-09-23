#--------------------------------------------------------#
# Curso avanzado de Python - Leccion 5: Metodo __init__
#--------------------------------------------------------#

#--------------------------------------------------------#
# Que es __init__
#--------------------------------------------------------#
# __init__ es un metodo especial de Python que se ejecuta
# automaticamente cada vez que creamos un objeto de una clase.
# Sirve para dar un estado inicial a los atributos del objeto.
# Tambien se le llama constructor o inicializador.

#--------------------------------------------------------#
# Ejemplo sin __init__
#--------------------------------------------------------#
class Alumno:
    nombre = "sin nombre"
    edad = 0
    grupo = "desconocido"

    def presentarse(self):
        print("Soy", self.nombre, "tengo", self.edad, "anios y estoy en", self.grupo)

# Si quiero inicializar varios alumnos, debo reasignar atributos uno por uno:
a1 = Alumno()
a1.nombre = "Pedro"
a1.edad = 16
a1.grupo = "3B"

a2 = Alumno()
a2.nombre = "Maria"
a2.edad = 17
a2.grupo = "4A"

a1.presentarse()
a2.presentarse()

#--------------------------------------------------------#
# Ejemplo con __init__
#--------------------------------------------------------#
class Alumno:
    def __init__(self, nombre, edad, grupo):
        self.nombre = nombre
        self.edad = edad
        self.grupo = grupo

    def presentarse(self):
        print("Soy", self.nombre, "tengo", self.edad, "anios y estoy en", self.grupo)

# Ahora puedo inicializar objetos de forma directa:
a1 = Alumno("Pedro", 16, "3B")
a2 = Alumno("Maria", 17, "4A")

a1.presentarse()
a2.presentarse()

#--------------------------------------------------------#
# Argumentos posicionales y con nombre
#--------------------------------------------------------#
# Posicionales:
b1 = Alumno("Luis", 18, "5C")

# Con nombre (el orden ya no importa):
b2 = Alumno(edad=19, grupo="6A", nombre="Ana")

b1.presentarse()
b2.presentarse()

#--------------------------------------------------------#
# Valores por defecto en __init__
#--------------------------------------------------------#
class Producto:
    def __init__(self, nombre, precio, categoria="General"):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar(self):
        print("Producto:", self.nombre, "Precio:", self.precio, "Categoria:", self.categoria)

# Si no especifico la categoria, usara "General"
p1 = Producto("Lapiz", 5)
p2 = Producto("Cuaderno", 25, "Papeleria")

p1.mostrar()
p2.mostrar()

#--------------------------------------------------------#
# Atributos de clase vs atributos de instancia
#--------------------------------------------------------#
class Cuenta:
    banco = "MiBanco"   # atributo de clase (igual para todos)
    
    def __init__(self, titular, saldo):
        self.titular = titular   # atributo de instancia
        self.saldo = saldo       # cambia segun cada objeto

    def mostrar(self):
        print("Banco:", Cuenta.banco, "- Titular:", self.titular, "- Saldo:", self.saldo)

c1 = Cuenta("Juan", 1000)
c2 = Cuenta("Rosa", 200)

c1.mostrar()
c2.mostrar()

# Cambiamos el atributo de clase
Cuenta.banco = "BancoCentral"
c1.mostrar()
c2.mostrar()

# Recordemos:
# __init__ es un metodo especial que se ejecuta al crear un objeto.
# Se usa para dar valores iniciales a los atributos.
# Puede recibir argumentos posicionales o con nombre.
# Puede tener valores por defecto para simplificar la creacion de objetos.
# Los atributos de clase son compartidos por todos los objetos,
# y los de instancia son unicos para cada uno.
