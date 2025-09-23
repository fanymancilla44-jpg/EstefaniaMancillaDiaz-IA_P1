#-----------------------------------------------------------------------#
# Curso basico de POO con Python - Leccion 3: El metodo __init__ y self
#-----------------------------------------------------------------------#

# En esta clase usamos el constructor __init__ para inicializar
# los atributos al momento de crear un objeto.
# Self representa al propio objeto y permite acceder a sus datos.

class Ninjas:
    def __init__(self, hp, resistencia, xp, vidas):
        self.hp = hp
        self.resistencia = resistencia
        self.xp = xp
        self.vidas = vidas

    def game_over(self):
        print("Game over")

# Creamos un objeto principal con valores iniciales
ninja_principal = Ninjas(100, 50, 1, 3)

# Creamos un enemigo con valores diferentes
ninja_enemigo = Ninjas(25, 10, 0, 1)

# Mostramos los atributos de cada uno
print("Ninja principal -> HP:", ninja_principal.hp,
      "Resistencia:", ninja_principal.resistencia,
      "Vidas:", ninja_principal.vidas)

print("Ninja enemigo -> HP:", ninja_enemigo.hp,
      "Resistencia:", ninja_enemigo.resistencia,
      "Vidas:", ninja_enemigo.vidas)

# Agregamos un nuevo atributo solo al ninja principal
ninja_principal.salto = True
print("El ninja principal puede saltar?", ninja_principal.salto)

# Si la vida de un ninja llega a 0, ejecutamos game_over()
if ninja_enemigo.hp == 0:
    ninja_enemigo.game_over()

# En fin
#  __init__ es como el constructor, sirve para arrancar la clase
# self es como decir "este objeto" (se refiere a si mismo)
# cada objeto puede tener sus propios valores (hp, xp, etc)
# si creas muchos objetos no repites codigo, solo usas __init__
# tambien puedes agregar atributos extra a un objeto en especifico

