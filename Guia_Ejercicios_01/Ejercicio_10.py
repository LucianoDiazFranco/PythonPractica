"""
Escribir un programa que solicite la fecha de nacimiento en formato “dd/mm/aaaa”, y muestre
por pantalla la fecha por separado el día, el mes y el año.
"""
# Solicitar al usuario que ingrese la fecha de nacimiento en formato "dd/mm/aaaa"
fecha_nacimiento = input("Por favor, ingresa su fecha de nacimiento en formato 'dd/mm/aaaa': ")

# Dividir la fecha en día, mes y año utilizando el carácter '/'
dia, mes, anio = fecha_nacimiento.split('/')

# Mostrar la fecha por separado
print("Día:", dia)
print("Mes:", mes)
print("Año:", anio)