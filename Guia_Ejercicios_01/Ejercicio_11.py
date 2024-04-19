"""
Escribir un programa que permita el ingreso por teclado de una oración de cinco palabras, y
muestre por pantalla, en minúsculas, en mayúsculas y por último solo el primer carácter de la
oración en mayúscula.
"""
palabra = input("Ingrese una horacion de cinco palabras: ")
print(palabra.upper())
print(palabra.lower())
# Mostrar solo el primer carácter en mayúscula
primera_palabra_mayus = palabra[0].upper() +palabra[1:].lower()
print(primera_palabra_mayus)