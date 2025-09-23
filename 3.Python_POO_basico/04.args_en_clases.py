#---------------------------------------------------------------------------------#
# Curso de python basico - leccion 5: Utilizacion de *args en las clases de python
#---------------------------------------------------------------------------------#

# En esta leccion vemos tres cosas:
# 1. Atributos de clase (se definen fuera del __init__)
# 2. Diferencia entre metodo y funcion
# 3. Uso de argumentos arbitrarios (*args) en una clase

# Clase Usuarios con atributos de clase y atributos normales
class Usuarios:
    # Atributos de clase (estan fuera del __init__)
    tipo_usuario = "Free"
    publicidad = True

    # Atributos de instancia (van dentro del __init__)
    def __init__(self, nid, alias, nombre, apellidos, *args):
        self.nid = nid
        self.alias = alias
        self.nombre = nombre
        self.apellidos = apellidos
        # Guardamos los argumentos extra en self.args
        self.args = args

# Creamos un objeto con varios argumentos adicionales
usuario1 = Usuarios("001", "PdePython", "Paula", "Bravo Rojas",
                    "Persona estudiosa", 
                    "Fan del lenguaje Python", 
                    "27")

# Mostramos un atributo de clase
print("Tipo de usuario:", usuario1.tipo_usuario)

# Cambiamos el atributo de clase solo en este objeto
usuario1.tipo_usuario = "Premium"
print("Nuevo tipo de usuario:", usuario1.tipo_usuario)

# Llamamos a un atributo de clase directamente desde la clase
print("Publicidad activa?", Usuarios.publicidad)

# Mostramos los argumentos extra que entraron por *args
print("Otros datos del usuario:", usuario1.args)

# *args sirve para pasar muchos valores extra sin tener
# que definirlos uno por uno en el __init__.

