#--------------------------------------------------------------------------#
# Curso avanzado de Python - Leccion 7: Guia completa de herencia en clases
#--------------------------------------------------------------------------#

# La herencia es uno de los 4 pilares de la POO.
# Sirve para crear nuevas clases que heredan atributos y metodos
# de otra clase base, evitando repetir codigo.

#Ejemplo
# Clase base o superclase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentar(self):
        print("Hola, soy", self.nombre, "y tengo", self.edad, "anios.")

# Subclase que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # usamos super() para llamar al init de Persona
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    def estudiar(self):
        print(self.nombre, "esta estudiando", self.carrera)

# Creamos objetos
p1 = Persona("Carlos", 40)
e1 = Estudiante("Ana", 20, "Ingenieria")

p1.presentar()
e1.presentar()
e1.estudiar()

#--------------------------------------------------------#
# Que paso aqui
#--------------------------------------------------------#
# Persona es la clase base con nombre y edad.
# Estudiante hereda de Persona y agrega el atributo carrera.
# Con super() reutilizamos el codigo del init de Persona
# para no repetirlo en Estudiante.

#--------------------------------------------------------#
# Otra subclase
#--------------------------------------------------------#
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia
    
    def dar_clase(self):
        print("El profesor", self.nombre, "imparte", self.materia)

prof1 = Profesor("Laura", 35, "Matematicas")

prof1.presentar()
prof1.dar_clase()

#--------------------------------------------------------#
# Si no usamos super()
#--------------------------------------------------------#
# Podriamos reescribir el init completo, pero seria duplicar codigo:
class ProfesorMalo(Persona):
    def __init__(self, nombre, edad, materia):
        self.nombre = nombre
        self.edad = edad
        self.materia = materia

# Funciona igual, pero es menos eficiente.
pm = ProfesorMalo("Luis", 50, "Historia")
print(pm.nombre, pm.materia)

#--------------------------------------------------------#
# Herencia en cadena
#--------------------------------------------------------#
# Una subclase puede ser base para otra subclase.
class Deportista(Persona):
    def __init__(self, nombre, edad, deporte):
        super().__init__(nombre, edad)
        self.deporte = deporte
    
    def entrenar(self):
        print(self.nombre, "esta entrenando", self.deporte)

class Futbolista(Deportista):
    def __init__(self, nombre, edad, equipo):
        super().__init__(nombre, edad, "futbol")
        self.equipo = equipo
    
    def jugar(self):
        print(self.nombre, "juega en el equipo", self.equipo)

jug1 = Futbolista("Diego", 25, "Tigres")
jug1.presentar()
jug1.entrenar()
jug1.jugar()

# Recordemos:
# Herencia = crear nuevas clases que aprovechan codigo de otras.
# Clase base = superclase. Clase hija = subclase.
# super() nos deja llamar al init o metodos de la superclase.
# Con herencia evitamos repetir codigo.
