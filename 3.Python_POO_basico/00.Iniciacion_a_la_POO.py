#--------------------------------------------------------#
# Curso basico de Python - Leccion 1:
# Iniciacion a la programacion orientada a objetos (POO)
#--------------------------------------------------------#

# Un objeto es como algo de la vida real pero en el programa
# Ejemplo: en un videojuego un personaje es un objeto y un enemigo es otro
# Cada uno tiene sus caracteristicas (atributos) y sus acciones (metodos)

# Otro ejemplo es una tienda en linea
# Los productos, el carrito de compras o el cliente, todos pueden ser objetos

# Los atributos son como las propiedades de un objeto
# Ejemplo: un pantalon tiene color y tipo
# podemos tener un pantalon negro sport y otro blanco sport
# Ambos tienen el mismo atributo pero con valores distintos

# Para poder crear objetos necesitamos una clase
# Una clase es como el molde o la receta
# A este proceso de crear objetos a partir de una clase se le llama instanciacion

# Asi se crea una clase vacia en Python:
class NombreClase:
    pass  # pass se usa para no dejar la clase vacia y evitar errores

# Ahora vamos a crear un objeto a partir de esa clase
primer_objeto = NombreClase()

# Con eso ya tenemos un objeto creado
# Si la clase tuviera atributos o metodos, este objeto los tendria tambien

# Ventaja de usar clases y no solo funciones:
# Si quieres hacer varios objetos que comparten cosas en comun
# como color, tamaño, etc, con la clase solo lo defines una vez
# y todos los objetos lo heredan
# Con funciones tendrias que repetir el codigo muchas veces y seria un desastre
