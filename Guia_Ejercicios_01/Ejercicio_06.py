"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por
hora. Después debe mostrar por pantalla la paga que le corresponde
"""
valor = int(input("Ingrese el valor de la hora trabajada: "))
horas = int(input("Ingrese la cantidad de goras trabajadas: "))
paga = valor*horas

print("La paga por su trabajo es de: ",paga)
