"""
Escribir un programa que muestre números del 0 al 30 uno debajo de otro.
● Cuando los números sean 3, 8, 17, 26 debe mostrar el mensaje “saltando instrucciones
con(xxxxxxxxxxxxx el nombre de la instrucción que permite realizar saltos en un bucle)
llegue al número 3 o 8 o 17 o 26”
● Cuando los números sean mayor a 25 debe preguntar si continúa o sale del conteo
(por ejemplo presione Presione: 'S' para salir , cualquier otra tecla para continuar)
○ Si presiona cualquier tecla el programa seguirá su curso
○ Si presiona S, terminará el programa, antes de terminar debe mostrar a qué
número de conteo llegó .
"""

for i in range(31):
    print(i)
    if i in [3, 8, 17, 26]:#Elijo que numeros quiron anotar
        print("Saltando instrucciones con 'break' llegué al número", i)
        continue
    elif i > 24:
        desea = input("Desea continuar con el conteo? (Si lo desea, presione 'S', sino cualquier otra tecla): ")
        if desea.upper() != 'S':
           print("Conteo Terminado")
        break  # Salir del bucle for

else:
    print("Se alcanzó el número 30.")
