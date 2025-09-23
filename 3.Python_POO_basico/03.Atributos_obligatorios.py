#-----------------------------------------------------------------------------#
# Curso basico de POO con Python - Leccion 4:mAtributos obligatorios en clases
#-----------------------------------------------------------------------------#

# En esta leccion vemos que con __init__ podemos obligar
# a que los objetos tengan ciertos atributos desde el inicio.
# Asi evitamos que se creen incompletos.

class Ninjas:
    def __init__(self, hp, resistencia, xp, vidas):
        # Estos son los atributos obligatorios
        self.hp = hp
        self.resistencia = resistencia
        self.xp = xp
        self.vidas = vidas

    def game_over(self):
        print("Game over")

# Crear un ninja principal con todos los atributos
ninja_principal = Ninjas(100, 50, 1, 3)

# Crear un enemigo con menos vida y resistencia
ninja_enemigo = Ninjas(25, 10, 0, 1)

# Mostrar datos
print("Ninja principal -> HP:", ninja_principal.hp,
      "Resistencia:", ninja_principal.resistencia,
      "XP:", ninja_principal.xp,
      "Vidas:", ninja_principal.vidas)

print("Ninja enemigo -> HP:", ninja_enemigo.hp,
      "Resistencia:", ninja_enemigo.resistencia,
      "XP:", ninja_enemigo.xp,
      "Vidas:", ninja_enemigo.vidas)

# Probar agregando un atributo extra SOLO al principal
ninja_principal.salto = True
print("El ninja principal puede saltar?", ninja_principal.salto)

# Esta forma de usar __init__ esta mas ordenada porque ya
# te obliga a meter los valores desde el inicio. Asi no se
# te olvida nada y cada objeto queda bien armado.

