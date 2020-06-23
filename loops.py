# loops

# for loop: ejecutar un codigo basado en cuantos items haya en la lista (cantidad exacta)

juegos = ["halo", "watchdogs", "call of duty"]

for juegoFavorito in juegos:
    print("hay un juego favorito: " + juegoFavorito)


# while loop: ejectuar un codigo basado en si una condicion es verdadera (cantidad inexacta)

numero = 1

while numero < 10:
    print("el numero es: " + str(numero))
    if numero == 3:
        print("oh, el tres es mi numero favorito")
    numero = numero + 1
