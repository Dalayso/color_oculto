#Descubrir el color oculto

print("\n● inicio del juego\n\n")

color = "xanatu"

intentos = 0

print("*" * 15)

while intentos < 3:
    print("\n^^^Menu^^^\nOpcion 1: Jugar\nOpcion 2: Salir\n")
    opciones = input("")
    while opciones == "1":
        color_elejido = input("● Ingrese un color para adivinar el color oculto: ")
        intentos += 1
        print(f"\n▪︎ su numero de intentos es: {intentos}\n")
        if color_elejido != color and intentos < 3:
            print("▪︎Intentalo de nuevo\n")
        elif color_elejido == color:
            print(f"》》》¡¡¡Acertaste el color  {color}!!!《《《""\n\n》》》¡¡¡Felicidades!!!《《《\n")
            intentos = 0
            break
        else:
            print(" :( Lo siento, se te acabaron los intentos\n")
            intentos = 0
            break
    else:
        break
print("**********************GAME OVER*************************")