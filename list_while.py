my_list = []
input_user = ""
j = 0 # while menu #
while j < 1:
    print("1.Lista de compra")
    print("2.Salir")
    selection = int(input("Seleccione una opcion:"))

    if selection == 1:
        j = 1
        while input_user != "FIN":
            input_user = input("Que deseas comprar? (Dijita FIN para terminar) : ").upper()
            if input_user != "FIN":
                my_list.append(input_user)

        len_list = len(my_list)
        actual_indice = 0

        while  actual_indice < len_list:
            print("Tengo que comprar {}".format(my_list[actual_indice]))
            actual_indice += 1
        print("Esta es mi lista de compra")

    if selection == 2:
        j = 1
        print("Programa terminado")





























