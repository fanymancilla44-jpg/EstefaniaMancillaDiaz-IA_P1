#--------------------------------------------------------#
# Curso de python basico - leccion 8:
# Herencia de clases en diferentes archivos
#--------------------------------------------------------#

# En esta leccion vamos a ver que las clases y la herencia
# no tienen que estar siempre en un solo archivo.
# Podemos repartirlas en varios archivos y usarlas con import.
# Eso es muy util para proyectos grandes, porque separa el codigo
# y lo hace mas ordenado.

# Archivo b.py -> contiene la clase base Usuarios
# Archivo c.py -> hereda de Usuarios y crea UsuariosPremium
# Archivo d.py -> hereda de UsuariosPremium y crea UsuariosPremiumPlus
# Archivo a.py -> importa los demas archivos y ejecuta el programa

#--------------------------------------------------------#
# Archivo b.py
#--------------------------------------------------------#
class Usuarios:
    tipo_usuario = "Free"
    publicidad = True

    def __init__(self, nid, alias, nombre, apellidos):
        self.nid = nid
        self.alias = alias
        self.nombre = nombre
        self.apellidos = apellidos

    def muestra_datos(self):
        print("El nombre y los apellidos del usuario son:", self.nombre, self.apellidos)
        print("El ID de usuario es:", self.nid)
        print("El alias del usuario es:", self.alias)

#--------------------------------------------------------#
# Archivo c.py
#--------------------------------------------------------#
# import b   # <- esto quedaría así si el archivo existiera
# class UsuariosPremium(b.Usuarios):
class UsuariosPremium(Usuarios):   # lo dejamos en el mismo archivo
    tipo_usuario = "Premium"
    publicidad = False

    def __init__(self, nid, alias, nombre, apellidos, participacion_sorteos, puntos_premios):
        super().__init__(nid, alias, nombre, apellidos)
        self.participacion_sorteos = participacion_sorteos
        self.puntos_premios = puntos_premios

    def muestra_datos(self):
        super().muestra_datos()
        print("Puntos premios:", self.puntos_premios)
        print("Participaciones sorteos:", self.participacion_sorteos)
#--------------------------------------------------------#
# Archivo d.py
#--------------------------------------------------------#
# import c   # <- si estuviera separado
# class UsuariosPremiumPlus(c.UsuariosPremium):
class UsuariosPremiumPlus(UsuariosPremium):   # en un solo archivo
    def __init__(self, nid, alias, nombre, apellidos, participacion_sorteos, puntos_premios, nivel):
        super().__init__(nid, alias, nombre, apellidos, participacion_sorteos, puntos_premios)
        self.nivel = nivel

    def muestra_datos(self):
        super().muestra_datos()
        print("Nivel Premium Plus:", self.nivel)


#--------------------------------------------------------#
# Archivo a.py
#--------------------------------------------------------#
# import b, c, d   # <- quedaría así si fueran modulos separados

# Creamos los objetos a partir de las clases
usuario1 = Usuarios("001", "raulito43", "Raul", "Fernandez Gomila")
usuario2 = UsuariosPremium("002", "PdePython", "Paula", "Vega Garcia", 10, 500)
usuario3 = UsuariosPremiumPlus("003", "BreakTheSystem", "Anonymous", "Anonymous", 25, 1500, "Diamante")

print("\nDATOS USUARIO 1 - Usuarios")
usuario1.muestra_datos()

print("\nDATOS USUARIO 2 - UsuariosPremium")
usuario2.muestra_datos()

print("\nDATOS USUARIO 3 - UsuariosPremiumPlus")
usuario3.muestra_datos()

# Separar clases en archivos distintos ayuda a organizar proyectos.
# import nos permite usar esas clases en cualquier archivo.
# super() sirve para aprovechar el codigo de la clase padre.