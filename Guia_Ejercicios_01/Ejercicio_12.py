"""
Escribir un programa que permita el ingreso de 2 dígitos, si es menor a 50 debe mostrar la
mitad de ese número.
"""
nro = int(input("Ingrese un numero de dos digitos: "))
if (nro < 50):
    print("El numero",nro,"es menor que 50 asi que la mitad del numero es: ",  nro/2)
else:
    print("El numero",nro,"es mayor que 50, asi que queda igual")