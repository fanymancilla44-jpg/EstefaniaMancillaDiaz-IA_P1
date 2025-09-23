#-------------------------------------------------------------#
# Curso avanzado de Python - Leccion 9: Polimorfismo en clases
#-------------------------------------------------------------#

# El polimorfismo es cuando un mismo metodo o funcion
# puede comportarse de distintas maneras segun el objeto.
# Es como cuando una persona puede ser estudiante,
# trabajador y deportista a la vez: depende del contexto.

#--------------------------------------------------------#
# Ejemplo basico con la funcion len()
#--------------------------------------------------------#
print(len("hola mundo"))        # cuenta caracteres
print(len([1, 2, 3, 4]))        # cuenta elementos de la lista
print(len({"a": 1, "b": 2}))    # cuenta pares clave-valor

#--------------------------------------------------------#
# Polimorfismo en clases
#--------------------------------------------------------#
class Animal:
    def hablar(self):
        print("soy un animal")

class Perro(Animal):
    def hablar(self):
        print("woof")

class Gato(Animal):
    def hablar(self):
        print("meow")

a = Animal()
p = Perro()
g = Gato()

a.hablar()   # usa metodo de Animal
p.hablar()   # usa metodo de Perro
g.hablar()   # usa metodo de Gato

#--------------------------------------------------------#
# Polimorfismo en funciones
#--------------------------------------------------------#
def dar_voz(objeto):
    objeto.hablar()

dar_voz(a)
dar_voz(p)
dar_voz(g)

#--------------------------------------------------------#
# Sobrescritura de metodos (overriding)
#--------------------------------------------------------#
# Una subclase puede cambiar el metodo de la superclase
class Persona:
    def saludar(self):
        print("hola soy una persona")

class Estudiante(Persona):
    def saludar(self):
        print("hola soy estudiante")

pe = Persona()
es = Estudiante()
pe.saludar()
es.saludar()

#--------------------------------------------------------#
# "Sobrecarga" en Python con *args
#--------------------------------------------------------#
# En Python no existe la sobrecarga como en otros lenguajes,
# pero podemos simularla usando *args para aceptar cualquier
# cantidad de parametros.
def multiplicar(*args):
    resultado = 1
    for n in args:
        resultado *= n
    print("resultado:", resultado)

multiplicar(2, 3)
multiplicar(2, 3, 4)
multiplicar(2, 3, 4, 5)

# Recordemos:
# Polimorfismo = mismo metodo, diferentes resultados.
# Ejemplo clasico: len() sirve para strings, listas, diccionarios.
# En clases: subclases pueden redefinir metodos (overriding).
# Sobrecarga como tal no existe, pero se simula con *args.
