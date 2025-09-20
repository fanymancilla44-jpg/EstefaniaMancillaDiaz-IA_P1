#-------------------------------------------------------------------#
# Curso de python basico - leccion 8: cadenas de caracteres (strings)
#-------------------------------------------------------------------#
# en python un string es simplemente una cadena de texto
# puede tener letras, numeros o simbolos como $ o #

# -------------------------------
# concatenacion de cadenas
# -------------------------------
# concatenar significa unir cadenas con el signo +
parte1 = "la programacion es como la vida:"
parte2 = " llena de errores, pero tambien de posibilidades."

frase = parte1 + parte2
print("concatenacion:", frase)

# tambien se puede meter un espacio como otra cadena
frase2 = parte1 + " " + parte2.strip()
print("concatenacion con espacio extra:", frase2)

# incluso directamente dentro del print
print("hola " + "mundo")

# -------------------------------
# tipos de comillas
# -------------------------------
# en python se pueden usar comillas simples o dobles
print("esto es un string con comillas dobles")
print('esto es un string con comillas simples')

# problema: si mezclamos comillas iguales dentro del texto
# print(""el tiempo es oro", me dijo.")  #esto da error

# solucion 1: alternar comillas
print('"el tiempo es oro", me dijo.')
print("'el tiempo es oro', me dijo.")

# solucion 2: usar el caracter de escape \"
print("\"el tiempo es oro\", me dijo.")
print('\'el tiempo es oro\', me dijo.')

# -------------------------------
# formateo de cadenas (f-strings)
# -------------------------------
# es mas facil y legible que concatenar con +
nombre = "fany"
print(f"hola, {nombre}. tenga un maravilloso dia.")

# tambien acepta operaciones dentro de las llaves
a = 10
b = 30
print(f"la suma de {a} + {b} es: {a + b}")

# o valores numericos sin problema (ejemplo con pi)
pi = 3.14159265359
print(f"el valor de pi siempre sera {pi}")

# -------------------------------
# metodos de cadenas
# -------------------------------
# los strings tienen metodos que se usan con un punto

frase = "la imaginacion es el principio de la creacion."

# capitalize() -primera letra mayuscula
print("capitalize():", frase.capitalize())

# upper() -todo a mayusculas
print("upper():", frase.upper())

# lower() -todo a minusculas
print("lower():", frase.lower())

# -------------------------------
# ejemplo practico con entrada de usuario
# -------------------------------
# nombre_usuario = input("introduce tu nombre:\n")
# print(f"hola {nombre_usuario.capitalize()}, bienvenido.")

