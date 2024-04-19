"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la
cuenta atrás desde ese número hasta cero separados por comas. (Investigue cómo mostrar
datos con print en la misma línea de texto), Si se anima trate de no imprimir la última coma
después del 0.
Ejemplo: 5
5,4,3,2,1,0,
5,4,3,2,1,0
"""
nro = int(input("Ingrese un número entero positivo: "))

# Imprimir la cuenta atrás desde el número ingresado hasta cero
print("Cuenta atrás:", end=" ")
# Empezamos desde el número ingresado y vamos hasta 0 (inclusive(-1), decrementando de 1 en 1
for i in range(nro, -1, -1):
    #Para sacar la ultima coma
    if i == 0:#si llega a 0 el siguiente nro va sin coma
        print(i, end="")
    else:
        print(i, end=",")