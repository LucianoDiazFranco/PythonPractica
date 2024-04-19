"""
Escribir un programa que permita calcular la suma de tres números enteros ingresados por
teclado. Si el resultado es mayor a 50 dividir por 2, en caso contrario elevar el resultado al
cubo, si al calcular el cubo el resultado es superior a 5000 deberá mostrar por pantalla “Este
es un gran número
"""
nro1 = int(input("Numero Primer: "))
nro2 = int(input("Numero  Segundo: "))
nro3 = int(input("Numero Tercero: "))

suma = nro1 + nro2 + nro3

if (suma > 50):
    if suma**3> 1000000:
        print("El numero",suma,"elevado al cubo es un gran número")
    else:
        print("El numero",suma,"es mayor a 50 pero menor a 1000000 entonces dividido por 2 es:",suma/2)
else:
    cubo = suma**3
    print("El numero ",suma,"es menor que 50 asi que al cubo es:",cubo)



