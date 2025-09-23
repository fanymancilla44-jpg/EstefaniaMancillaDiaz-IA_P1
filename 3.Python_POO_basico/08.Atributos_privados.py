#-------------------------------------------------------------------------#
# Curso de python basico - leccion 9: Encapsulamiento - atributos privados
#-------------------------------------------------------------------------#

# En esta leccion vamos a explicar que es el encapsulamiento.
# En palabras simples, sirve para proteger algunos datos
# de una clase y que no se puedan cambiar desde afuera.
# Esto es muy util cuando tenemos informacion sensible
# como contrasenas, datos personales, etc.

#--------------------------------------------------------#
# Clase Usuarios con atributo privado __password
#--------------------------------------------------------#
class Usuarios:
    # El metodo __init__ es el constructor, sirve para
    # inicializar los valores de cada usuario.
    def __init__(self, nid, alias, nombre, apellidos, password):
        self.nid = nid                # identificador unico del usuario
        self.alias = alias            # nombre corto o nick
        self.nombre = nombre          # nombre real
        self.apellidos = apellidos    # apellidos del usuario
        self.__password = password    # atributo privado (lleva __)

    # Este metodo muestra los datos del usuario
    # Aqui si podemos acceder al atributo __password
    # porque estamos dentro de la clase.
    def muestra_datos(self):
        print("El nombre y los apellidos del usuario son:", self.nombre, self.apellidos)
        print("El ID de usuario es:", self.nid)
        print("El alias del usuario es:", self.alias)
        print("La contrasena es:", self.__password)

# Aqui creamos un objeto de tipo Usuarios.
# Como el __init__ pide 5 parametros, tenemos que ponerlos todos.
usuario1 = Usuarios("002", "Hakunamatata", "fany", "Diaz", "pozole1234")

# Ahora usamos el metodo muestra_datos() para ver toda la info del usuario.
# Notese que si intento imprimir usuario1.__password directamente me va a dar error,
# porque esta protegido por el encapsulamiento.
usuario1.muestra_datos()

# Con __ delante de un atributo lo volvemos "privado".
# Solo podemos usar ese atributo dentro de la clase.
# Esto protege la informacion y obliga a usar metodos
# que nosotros mismos definamos para acceder a ella.