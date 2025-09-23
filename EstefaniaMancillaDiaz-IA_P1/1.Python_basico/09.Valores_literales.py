#----------------------------------------------------------------------#
# Curso de python basico - leccion 9: Los Valores literales en python
#----------------------------------------------------------------------#

# Vamos a ver que son los valores literales en Python.
# Un valor literal es simplemente un valor que escribimos directo en el codigo,
# sin necesidad de calcularlo o pedirlo al usuario.
# Por ejemplo: numeros como 10, textos como "Hola", o valores como True/False.

# Ejemplo 1: una cadena literal (string)
frase = "Aprendiendo Python"   # esta frase es literal porque esta escrita fija en el codigo
print(frase)

# Si despues cambiamos el valor de la variable, lo que hacemos es reasignar otro literal
frase = "La frase ha cambiado totalmente"
print(frase)
# Aqui se reemplaza el valor literal anterior por uno nuevo, pero ambos son literales.

# Ejemplo 2: cadena literal vs valor no literal
# Cuando usamos input(), el texto dentro del input es literal,
# pero lo que escriba el usuario NO lo es, porque no lo sabemos hasta que se ejecute.
nombre = input("Introduzca su nombre:\n")  # es literal
print("Su nombre es: " + nombre)  
# "Su nombre es: " es literal, pero el nombre que pongas tu en la consola no lo es.

# Truco para identificar:
# Preguntate: ¿se el valor antes de ejecutar el programa?
#  Si la respuesta es si, es un valor literal.
#  Si la respuesta es no (depende de algo externo como input), entonces no es literal.

# Ejemplo 3: otros tipos de valores literales
numero1 = 10   # literal tipo entero (int)
numero2 = 586  # otro literal tipo entero
pi = 3.1416    # literal tipo decimal (float)
es_mayor = True  # literal booleano (bool)
print(numero1, numero2, pi, es_mayor)

# Python recomienda que las constantes (valores que no cambian) se escriban en MAYUSCULAS.
# Por ejemplo: PI = 3.1416
# Eso ayuda a identificar mas facil los valores que tratamos como literales fijos.

# Ejemplo 4: valor literal sin soporte
"Este valor es literal y no tiene soporte, esta 'suelto en el codigo'."
# Esto Python lo lee, pero como no tiene variable donde guardarse, no sirve de nada.

# Recordemos:
# Un literal es un dato fijo que escribes tal cual en el codigo.
# Pueden ser cadenas, numeros, booleanos, etc.
# Si lo conoces antes de ejecutar, es literal.
