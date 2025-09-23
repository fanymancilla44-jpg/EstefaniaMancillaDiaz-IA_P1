#-------------------------------------------------------------------#
# Curso de python basico - leccion 7: Herencia con super() en python
#-------------------------------------------------------------------#

# En la herencia normal, si ponemos un __init__ en la subclase,
# este reemplaza al __init__ de la superclase. Eso puede ser un
# problema porque se pierden los atributos de la clase padre.
# Para evitar eso existe super(), que sirve para "rescatar"
# lo que ya tenia la clase padre y sumarle lo nuevo.

# Clase padre
class Usuarios:
    tipo_usuario = "Free"
    publicidad = True

    def __init__(self, nid, alias, nombre, apellidos):
        self.nid = nid
        self.alias = alias
        self.nombre = nombre
        self.apellidos = apellidos

    def muestra_datos(self):
        print("Nombre completo:", self.nombre, self.apellidos)
        print("ID:", self.nid)
        print("Alias:", self.alias)

# Subclase que hereda de Usuarios
class UsuariosPremium(Usuarios):
    tipo_usuario = "Premium"
    publicidad = False

    # Aqui agregamos mas atributos pero sin perder los de Usuarios
    def __init__(self, nid, alias, nombre, apellidos, participacion_sorteos, puntos_premios):
        super().__init__(nid, alias, nombre, apellidos)  # con esto jalamos el init de Usuarios
        self.participacion_sorteos = participacion_sorteos
        self.puntos_premios = puntos_premios
        self.contenido_premium = True

# Subclase que hereda de UsuariosPremium
class UsuariosPremiumPlus(UsuariosPremium):
    def __init__(self, nid, alias, nombre, apellidos, puntos_premios):
        # Aqui podemos fijar la participacion en sorteos a 25 directo
        super().__init__(nid, alias, nombre, apellidos, 25, puntos_premios)
        self.soporte_personal = True

# Probamos todo
usuario1 = Usuarios("001", "raulito43", "Raul", "Fernandez")
usuario1.muestra_datos()
print("Tipo:", usuario1.tipo_usuario, "| Publicidad:", usuario1.publicidad)

print("--------------------------------------------------")

usuario2 = UsuariosPremium("002", "paulita88", "Paula", "Bravo", 10, 150)
usuario2.muestra_datos()
print("Tipo:", usuario2.tipo_usuario, "| Sorteos:", usuario2.participacion_sorteos, "| Puntos:", usuario2.puntos_premios)

print("--------------------------------------------------")

usuario3 = UsuariosPremiumPlus("003", "carlitos99", "Carlos", "Mendoza", 300)
usuario3.muestra_datos()
print("Tipo:", usuario3.tipo_usuario, "| Sorteos:", usuario3.participacion_sorteos, "| Puntos:", usuario3.puntos_premios, "| Soporte:", usuario3.soporte_personal)

# Con super() se pueden heredar los atributos del padre sin reescribir todo.
# Cada subclase puede agregar lo suyo sin perder lo anterior.
# Es muy util cuando varias clases comparten logica y solo cambian algunos detalles.
