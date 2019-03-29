numero_ganador = int(input("Elige numero ganador: "))
print("Perfecto, su numero quedo guardado")

numero_usuario = int(input("Adivina el numero: "))
while numero_ganador != numero_usuario:
    numero_usuario = int(input("Adivina el numero: "))

print("Perfecto, Adivinaste!")
