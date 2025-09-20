#--------------------------------------------------------#
# Curso de python basico - leccion 5: 
# Normas y convenciones de nombres de variables en python
#--------------------------------------------------------#

# En Python hay reglas obligatorias (si no las cumples da error)
# y convenciones (buenas prácticas para escribir código limpio).

# -------------------------------
# REGLAS (obligatorias)
# -------------------------------

# 1. Python distingue mayusculas y minusculas
nombre_variable = 1
NOMBRE_VARIABLE = 2
Nombre_Variable = 3
print(nombre_variable, NOMBRE_VARIABLE, Nombre_Variable) # Son variables diferentes

# 2. Solo se pueden usar letras, numeros y "_"
numero1 = 100
fecha_actual = "2025-09-19"
resultado_final = True

# Ejemplos invalidos (darian error):
# 1numero = 10
# $dinero = 50
# nombre-usuario = "fany"

# 3. No empezar con un numero
_valido = "Sí"
a1_b2_c3 = "También válido"

# -------------------------------
# PALABRAS RESERVADAS
# -------------------------------
# No puedes usar las palabras reservadas de Python como variables
# Ejemplo:
# global = 10
# if = "texto"
# for = 5

# -------------------------------
# CONVENCIONES (buenas prácticas)
# -------------------------------

# Usa nombres descriptivos
saludo = "Hola"
numero = 7
numero_preciso = 7.5657

# Ejemplos poco claros
x = "Hola"
y = 7
z = 7.5657

# Escribe las variables en minusculas
edad = 20
nombre_completo = "Carlos Pérez"

# Para nombres compuestos usa snake_case
hora_actual = "10:30"
variable_con_varias_palabras = "ejemplo"

# Constantes en mayusculas
PI = 3.14159
RADIO_TIERRA = 6371

# Evita acentos, ñ u otros simbolos
# válido = "sí"      NO recomendable
valido = "sí"        # Mejor así
ano = 2025           # Usar "ano" en vez de "año"

# -------------------------------
# EJEMPLO: función con nombres claros
# -------------------------------
def sumar(numero1, numero2):
    """Suma dos números y devuelve el resultado"""
    return numero1 + numero2

print("Suma:", sumar(3, 5))
