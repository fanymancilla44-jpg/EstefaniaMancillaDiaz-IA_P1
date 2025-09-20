#--------------------------------------------------------#
# Curso de python basico - leccion 2: Comentarios en python
#--------------------------------------------------------#
# Como se muestra en las lineas anteriores son conocidos como comentarios
# que empiezan con el simbolo (#)
# esto quiere decir que que dentro de un codigo ejecutable puedes comentar
# sin afectar el codigo, es como si fuera invisible para el codigo 
# como si no existiera por lo que no afecta para nada el codigo

#Ejemplo 1:
print("hola mundo") #esto se ejecuta y se muestra.
#print("hola mundo") --- mientras que esto no se muestra python lo ignora
#mientras se ponga (#) en una linea que si es parte del codigo
#pero por cierta razon quieres que ignore ese paso se pone al inicio de 
#la linea y desactiva esa parte del codigo

#Ejemplo 2:
def funcion_grande():
    #parte 1
    #codigo ---, los ("...")solo indican que falta codigo ahi, o son orientativos
    ...
#Ejemplo 3: comentarios a la derecha del codigo
print("hola mundo") #este comentario no afecta el codigo porque no esta al inicio
#en pocas palabras no desactiva la funcion.

#Ejemplo 4:
"""
Este es un comentario multilínea de Python, puedes escribir un texto 
sin necesidad de poner en cada linea el (#)
otro dato puedes utilizar tambien las comillas simples (''') y es la misma finalidad
"""