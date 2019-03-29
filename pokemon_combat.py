pokemon_elegido = input("Contra que pokemon deseas pelear? (Squirtle, Bulbasor, Charmander) ")

vida_pikachu = 100
vida_enemigo = 0
ataque_enemigo = 0


if pokemon_elegido == "Squirtle" :
    vida_enemigo = 100
elif pokemon_elegido == "Bulbasor" :
    vida_enemigo = 120
elif pokemon_elegido == "Charmander" :
    vida_enemigo = 90

while vida_enemigo > 0 and vida_pikachu > 0:
    ataque_elegido = input("¿Que ataque quieres usar? (chispazo / impactrueno)")
    if ataque_elegido == "chispazo":
        vida_enemigo -= 10

    if ataque_elegido == "impactrueno":
        vida_enemigo -= 15


    if pokemon_elegido == "Squirtle":
        vida_pikachu -= 10
        print("Squirtle te hace un ataque de 10 de daño")

    if pokemon_elegido == "Bulbasor":
        vida_pikachu -= 6
        print("Bulbasor te hace un ataque de 6 de daño")

    if pokemon_elegido == "Charmander":
        vida_pikachu -= 15
        print("Charmander te hace un ataque de 15 de daño")


    print("La vida de pikachu es ahora de {} ".format(vida_pikachu))
    print("La vida del enemigo ahora es {} ".format(vida_enemigo))

if vida_enemigo <= 0:
    print("Felicidades, has ganado!")

if vida_pikachu <= 0:
    print("Que pena, has perdido!")



print("El combate ha finalizado")
