#-------------------------------------------------------------#
# Curso de python basico - leccion 3: Tipos de datos en python
#-------------------------------------------------------------#

"""
los tipos de datos como se menciono algunos en la leccion 1 de variables
son de tipo entero(int), flotante(float), textos(string) y por ultimo, 
que se mostrara en este sript los booleanos(bool).
"""
#Ejemplo 1:(int)se implementa para numero enteros,positivos, negativos y ceros
# y siempre va sin comillas
numero = 5
numero = -5 # para que lea bien que es negativo debe estar pegado al valor sin espacio
numero = 0
#Ejemplo 2:(float) representa numeros decimales
pi = 3.1416 #importante siempre debe ser con un (.) y no con una (,).
pi = -3.1416 # para valor negativo solo debe agregarse el signo a lado del valor

#Ejemplo 3:(string) esto es una cadena de caracteres como letras, simbolos, etc.
#se puede crear este tipo de dato poniendo el entrecomillado
nombre = "fany" #esto es correcto
nombre = 'fany' #esto es correcto
#nombre = 'fany" #esto es incorrecto, debe ser el mismo tipo de comillas que se usa.

#Ejemplo 4:(bool) es un tipo de dato que solo puede tener uno de dos valores posibles
# true (verdadero) o false (falso) y se utilizan para tomar decisiones en el código.
valor_booleano = True
valor_booleano = False
# estos dos valores son sin comillas, para evitar 
# que sean tratados como tipo de dato string.