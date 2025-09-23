#--------------------------------------------------------#
# Curso de python basico - leccion 6:
# Herencia de clases en python (superclases y subclases)
#--------------------------------------------------------#

# La herencia en POO sirve para que una clase "hija" (subclase)
# pueda heredar atributos y metodos de otra clase "padre" (superclase).
# Con esto evitamos repetir codigo y hacemos el programa mas limpio.

# Clase padre o superclase
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

# Clase hija o subclase que hereda de Usuarios
class UsuariosPremium(Usuarios):
    # Cambiamos solo lo diferente respecto a la superclase
    tipo_usuario = "Premium"
    publicidad = False

# Creamos un objeto de la clase normal
usuario1 = Usuarios("001", "raulito43", "Raul", "Fernandez Gomila")
usuario1.muestra_datos()
print("Tipo de usuario:", usuario1.tipo_usuario)
print("Publicidad:", usuario1.publicidad)

print("--------------------------------------------------")

# Creamos un objeto de la clase heredada (Premium)
usuario2 = UsuariosPremium("002", "paulita88", "Paula", "Bravo Rojas")
usuario2.muestra_datos()
print("Tipo de usuario:", usuario2.tipo_usuario)
print("Publicidad:", usuario2.publicidad)

# Lo bueno de la herencia es que no tenemos que copiar y pegar
# todo el codigo de nuevo, solo cambiamos lo que sea diferente.