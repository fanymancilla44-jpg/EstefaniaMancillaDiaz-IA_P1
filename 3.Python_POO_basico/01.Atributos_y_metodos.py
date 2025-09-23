#---------------------------------------------------------------------#
# Curso basico de POO con Python - Leccion 2: Clases basicas y objetos
#---------------------------------------------------------------------#

# aqui vamos a crear una clase sencilla llamada NinjaPrincipal
# la clase tendra 3 atributos (hp, resistencia y xp) y un metodo
# llamado game_over() que muestra un mensaje cuando la vida llega a 0

class NinjaPrincipal:
    # atributos de la clase (como caracteristicas del personaje)
    hp = 100
    resistencia = 50
    xp = 0

    # metodo (una funcion dentro de la clase)
    def game_over(self):
        print("Game over")

# ahora instanciamos un objeto de la clase, o sea creamos un ninja
ninja = NinjaPrincipal()

# mostramos el valor del atributo hp
print("Vida inicial del ninja:", ninja.hp)

# cambiamos el valor de hp solo para este objeto
ninja.hp = 0
print("Vida actual del ninja:", ninja.hp)

# si la vida llega a 0, ejecutamos el metodo game_over()
if ninja.hp == 0:
    ninja.game_over()
