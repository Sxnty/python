operacion_elegida = input("¿Que tipo de operacion desea realizar?(restar / sumar / multiplicar / dividir)")
print("Perfecto, usted eligio {}".format(operacion_elegida))

#sumar
if operacion_elegida == "sumar":
    numero_1 = int(input("Numero 1: "))
    numero_2 = int(input("Numero 2: "))
    resultado = numero_1+numero_2
    print("El resultado de {} + {} es: {}".format(numero_1,numero_2,resultado))
#Restar
elif operacion_elegida == "restar":
    numero_1 = int(input("Numero 1: "))
    numero_2 = int(input("Numero 2: "))
    resultado = numero_1-numero_2
    print("El resultado de {} - {} es: {}".format(numero_1,numero_2,resultado))
#multiplicar
elif operacion_elegida == "multiplicar":
    numero_1 = int(input("Numero 1: "))
    numero_2 = int(input("Numero 2: "))
    resultado = numero_1*numero_2
    print("El resultado de {} * {} es: {}".format(numero_1,numero_2,resultado))
#dividir
elif operacion_elegida == "dividir":
    numero_1 = int(input("Numero 1: "))
    numero_2 = int(input("Numero 2: "))
    resultado = numero_1/numero_2
    print("El resultado de {} / {} es: {}".format(numero_1,numero_2,resultado))
