import random

#se  coloca un loop principal que preguntará si se quiere iniciar el juego (ronda), después de cada ronda de 3 partidas, se preguntará de nuevo
#se coloca un segundo loop para el número de partidas
#si el jugador elige un número fuera del rango disponible, se le solicitará que coloque nuevamente un número correcto
#si todo está bien, se dará inicio al juego, comparando respuestas
#después de jugar todas las partidas, se le pregunta nuevamente si quiere jugar de nuevo, si elige si, se reinicia el loop principal, si elige no, se imprime el "else"

nuevo_juego=input("Nuevo juego: Si/No ")


while nuevo_juego=="si" or nuevo_juego=="SI" or nuevo_juego=="Si" or nuevo_juego=="s" or nuevo_juego=="S":

    contador=0

    while contador<3:

        eleccion_jugador=int(input("Elige: 1=Piedra, 2=Papel, 3=Tijera "))
        computadora=random.randint(1,3)


        if eleccion_jugador !=1 and eleccion_jugador !=2 and eleccion_jugador !=3:
            print("elige un número entre el 1 al 3, tú pusiste ", eleccion_jugador)


        elif eleccion_jugador==computadora:

            if eleccion_jugador==1 and computadora==1:
                print("Empate, los dos sacaron piedra")

            elif eleccion_jugador==2 and computadora==2:
                print("Empate, los dos sacaron papel")

            elif eleccion_jugador==3 and computadora==3:
                print("Empate, los dos sacaron tijera")
            
            contador=contador+1

        elif eleccion_jugador!=computadora:

            if eleccion_jugador==1 and computadora==3:
                print("Ganaste, tú elegiste piedra y la computadora tijera")

            elif eleccion_jugador==3 and computadora==2:
                print("Ganaste, tú elegiste tijera y la computadora papel")
                
            elif eleccion_jugador==2 and computadora==1:
                print("Ganaste, tú elegiste papel y la computadora piedra")
            
            elif eleccion_jugador==1 and computadora==2:
                print("Perdiste, tú elegiste piedra y la computadora papel")

            elif eleccion_jugador==2 and computadora==3:
                print("Perdiste, tú elegiste papel y la computadora tijera")

            elif eleccion_jugador==3 and computadora==1:
                print("Perdiste, tú elegiste tijera y la computadora piedra")

            contador=contador+1

    nuevo_juego=input("Nuevo juego: Si/No ")

else:
    print("Gracias por jugar")