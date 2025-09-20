#------------------------------------------------------------------#
# Curso de python basico - leccion 6: Matematicas basicas en python
#------------------------------------------------------------------#

"""
Las matematicas basicas en python son las mas conocidas como suma, resta,
multiplicacion,division.
pero tambien python podemos implementar la potencia, modulo, division entera,
prioridad de parentesis y representacion para numeros largos
"""
"""
estas son herramientas que nos ayudan facilitar a la resolucion de un problema 
en lenguaje de programacion
"""
'''
Comenzando con la suma (+) sirve para sumar dos valores 
o incluso muchos mas valores
'''
#Ejemplo 1
20+15+10 #en python la suma se reliza de izquierda a derecha y luego el que sigue,
# python lo realiza de la siguiente manera
print(20+15) # primero los dos valores = 35
print(35+10) # luego el resultado anterior + el siguiente valor = 45
print(20+15+20) #si queremos que nos muestre el resultado se llama de esta manera
#Ejemplo 2
#crearemos una variable donde se almacenara el resultado de la suma y lo mostraremos
Resultado = 20+15
print(Resultado)
'''
 La resta (-) sirve para restar dos valores 
o incluso muchos mas valores o tambien conocido como
operacion de sustraccion,quiere decir sustrae un valor a otro.
'''
#Ejemplo 1
#crearemos una variable donde se almacenara el resultado de la resta y lo mostraremos
Resta = 20-15
print(Resta)
'''
 La multiplicacion (*) se coloca en medio de dos valores
o incluso muchos mas valores para realizar la operacion.
'''
#Ejemplo 1
#crearemos una variable donde se almacenara el resultado de la miltiplicacion y lo mostraremos
multiplicacion = 20*15
print(multiplicacion)
'''
 La division (/) se coloca en medio de dos valores
para realizar la operacion.
'''
#Ejemplo 1
#crearemos una variable donde se almacenara el resultado de la division y lo mostraremos
division = 20/15
print(division) # en la division por lo general da resulados de tipo float 
#Ejemplo 2
division2 = 20/20
print(division2)# el resultado que mostrara sera 1.0(flotante) no 1.

'''
Las operaciones multiples y mixtas, son aquellas donde utilizas varios operandos
'''
#Ejemplo 1
total = 20*15+10+7-22/3 #cuando es asi por regla matematica el orden de desarrollo
# empieza primero con la mas dominate como la multplicacion y division despues sigue
# con la suma y la resta.
print(total)
'''
Para declarar variables numericas donde se almacenara el dato o valor es de la siguiente manera
'''
#Ejemplo 1
valor_1 = 50 #almacena el 50
valor_2 = 20 #almacena el 20
suma= valor_1 + valor_2 #puede ser cualquier operacion, pero siempre se declara asi con su respectivo simbolo
print(suma) #muestra el resultado 
'''
El modulo (%) es lo mismo que la division pero no muestra el cociente
si no que muestra el resto o tambien conocido como residuo
'''
#Ejemplo 1
# Declaramos dos variables numericas
numero1 = 10 # Dividendo
numero2 = 3 # Divisor

# Calculamos el cociente y el resto de la division
cociente = numero1 / numero2 # Division normal
resto = numero1 % numero2 # Division modulo

# Imprimimos el cociente y el resto
print("Cociente:", cociente)
print("Resto:", resto) #si solo queremos mostrar el resto no es necesario la parte del cociente

'''
La division entera (//) como dice su nombre divide pero siempre 
muestra un resultado entero , no como la division normal de tipo (float)
'''
#Ejemplo 1
# Declaramos dos variables numericas
num1 = 7 # Dividendo
num2 = 2 # Divisor

# Calculamos la división
divi = num1 / num2 #el resultado es 7/2 =3.5
division_entera = num1 // num2 #esta elimina el 0.5 y la deja en 3(int)

# Imprimimos los resultados
print(divi)
print(division_entera)# como cuando te piden sacar la media 
#de un listado esta es la herramienta correcta ya que en ocasiones da valores flotantes
#pero en otra leccion especificaremos los listados
'''
La potencia (**) calcula potencias lo que es los exonentes de forma rapida 
'''
#Ejemplo 1
# Cálculo de 2 elevado a 5
operacion = 2 * 2 * 2 * 2 * 2 #se multiplica por si mismo depende la cantidad del exponente
print(operacion)
#ahora utulizando el operador
operacion1= 2 ** 5 # es de esta forma y correcta
print(operacion1)
'''
Los parentesis () en las matematicas es importante ya que se encargan de agrupar
un valores con cierta o ciertas operaciones y sin no hay corchetes en las operaciones
pero si parentesis siempre debemos comenzar con parentesis.
'''
#Ejemplo 1
resul= 10 + 6 * 2 #no hay agrupaciones por lo tanto empieza por la multiplicacion
print(resul) #da un resultado
resul2 = (10 + 6) * 2 #hay agrupaciones, por lo que comineta con la operacion dentro de los ()
# y ese resultado lo multiplica por 2
print(resul2) #da otro resultado
#como podemos ver en las dos son los mismos valores y operaciones, pero los()
#cambian el resultado por el orden y operacion que se realizo dentro de ella.
'''
Numeros largos, guiones bajos para numeros grandes y decimales
estos serian como tips para ayudas visuales en el codigo
'''
"""
numero_largo = 56404357843987 (dificil de leer)
numero_largo = 56_404_357_843_987 (con la ayuda de los guiones bajos la lectura es mas facil)
print(numero_largo) -(aunque tenga guiones te mostrara el el valor dificil de leer porque no altera tu numero)
numero_largo = 56_404_357_843_987.78(igual con este ayuda visual)
print(numero_largo) (pero el resultado sera sin guiones, respentando los numeros y puntos)
numero_largo = 56_404_357_843_987.7_865_657 (esta es otra manera de separalos incluso con decimales)
print(numero_largo)(nuevamente respeta los numeros y guiones son ignorados)
"""
#por ultimo como dato importante siempre deben  ser separados por guiones bajos
#cada 3 cifras,si no se completan 3 cifras ya no se ponen, 
#en el caso de un punto decimal como se muestra anteriormente,despues del punto 
#comienza a contar de 3 cifras de nuevo y siempre se empieza
#de derecha a izquierda 
