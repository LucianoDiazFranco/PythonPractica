"""
Escribir un programa que permita realizar 3 cálculos aritméticos, suma, resta y multiplicación.
Las opciones deben presentarse a modo de menú de opciones , el usuario elegirá la operación
deseada , el programa deberá verificar si el valor ingresado esta entre las opciones del menú
, si la opción ingresada no es correcta debe mostrar un mensaje que diga opción incorrecta y
salir del programa pero si la opción es correcta seguirá con el programa y se le pedirá al
usuario el ingreso de dos números enteros para ejecutar la operación seleccionada, luego debe
mostrar la operación seleccionada, el desarrollo y el resultado. ejemplo:
Menú:
Suma (1) Resta (2) Multiplicación (3)
opción: 1
dato : 1
dato : 2
El resultado de la suma 1 + 2 = 3.
"""
print('\n'
      '***MENU***\n'
      'Opcion 1 = Suma\n'
      'Opcion 2 = Resta\n'
      'Opcion 3 = Divicion\n'
      'Opcion 4 = Multiplicacion')

opcion = int(input("Ingrese la Opcion a Realizar: "))

nro1 = int(input("Ingrese el primer Numero: "))
nro2 = int(input("Ingrese el segundo Numero: "))

if opcion == 1:
    print("El resultado de la suma es:", nro1 + nro2)
elif opcion == 2:
    print("El resultado de la resta es:", nro1 - nro2)
elif opcion == 3:
    if nro2 == 0:
        print("No se puede dividir por 0")
    else:
        print("El resultado de la divicion es:",nro1 / nro2)
elif opcion == 4:
    print("El resultado de la multiplicacion es:",nro1*nro2)
else:
    print("Opcion incorrecta, *Elija una opcion del menu correcta*")

