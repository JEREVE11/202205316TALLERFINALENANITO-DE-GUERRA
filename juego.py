
"""Un dado.
-  Un jugador que avanza por casillas.
-  Casillas normales.
-  Casillas de habilidad que recuperan una vida.
-  Una casilla de peligro que te devuelve al inicio.
-  3 vidas.
-  Una meta pequeña de 20 casillas"""
import random

# Datos del jugador
posicion = 1
vidas = 3
meta = 20

print("================================")
print("      RETO NIVEL SILVESTRE")
print("================================")
print("Llega hasta la casilla", meta)
print("Tienes", vidas, "vidas.")

while posicion < meta and vidas > 0:

    print("\nEstás en la casilla:", posicion)
    input("Presiona ENTER para lanzar el dado...")

    dado = random.randint(1, 6)
    print(" Sacaste:", dado)

    posicion += dado

    # No pasar de la meta
    if posicion > meta:
        posicion = meta

    print(" Avanzaste a la casilla:", posicion)

    # Casillas especiales
    if posicion in [5, 12, 17]:
        print(" ¡Encontraste salsa morada!")
        vidas += 1
        print(" Recuperaste una vida.")
        print("Vidas:", vidas)

    elif posicion in [8, 15]:
        print(" ¡Cuidado! Pisaste una casilla de peligro.")
        vidas -= 1
        posicion = 1
        print(" Perdiste una vida.")
        print("Regresas al inicio.")

    else:
        print(" Casilla normal.")

    print("Vidas:", vidas)

# Final del juego
if vidas <= 0:
    print("\n GAME OVER")
    print("Te quedaste sin vidas.")

else:
    print("\n ¡FELICIDADES!")
    print("Llegaste a la meta.")

 ### ¿Cómo funciona?

"""El tablero realmente sería algo como:


INICIO
  
[1] → [2] → [3] → [4] → [5] → [6] → [7] → [8] ...
                                        
 En el programa:

 - `random.randint(1, 6)` simula el dado.
- `posicion` indica dónde está el jugador.
- `vidas` guarda las vidas.
- Las casillas `5, 12, 17` son de **salsa morada**.
- Las casillas `8, 15` son de **peligro**.
- La meta está en la casilla `20`."""
