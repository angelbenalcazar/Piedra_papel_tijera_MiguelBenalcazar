import random

def eleccion_incorrecta ():
    print("Elección incorrecta")

def agradecimiento():
     print("Gracias por jugar")

def empate ():
     print("Empate")

def perder ():
     print("Perdiste")

def ganar ():
     print("Ganaste")
     


print("Bienvenido al juego Piedra, papel o tijera. Tendrás la oportunidad de jugar contra la computadora o contra otro jugador en una ronda de tres partidas.")

modalidad_juego={'modalidad de juego': int(input("Elección jugador contra computadora, escribe: 1. Elección Jugador_1 contra jugador_2, escribe: 2: ")), 'jugador': input("Coloca tu nombre: ")}


if modalidad_juego['modalidad de juego']==1:


    nuevo_juego=input("Nuevo juego: Si/No ")

    while nuevo_juego=="si" or nuevo_juego=="SI" or nuevo_juego=="Si" or nuevo_juego=="s" or nuevo_juego=="S":

        contador=0
        
        while contador<3:

            juego={"seleccion_jugador": int(input("Jugador elige: 1=Piedra, 2=Papel, 3=Tijera ")), "seleccion_computadora": random.randint(1,3)}

            while juego["seleccion_jugador"]!=1 and juego["seleccion_jugador"] !=2 and juego["seleccion_jugador"] !=3:
                eleccion_incorrecta()
                juego["seleccion_jugador"]=int(input("Escoge de nuevo: 1=Piedra, 2=Papel, 3=Tijera "))


            if juego["seleccion_jugador"]==juego["seleccion_computadora"]:
                empate()
                contador+=1

            elif juego["seleccion_jugador"]!=juego["seleccion_computadora"]:
                if juego["seleccion_jugador"]==1 and juego["seleccion_computadora"]==3:
                        print("Ganaste, tú elegiste piedra y la computadora tijera")
                elif juego["seleccion_jugador"]==3 and juego["seleccion_computadora"]==2:
                        print("Ganaste, tú elegiste tijera y la computadora papel")
                elif juego["seleccion_jugador"]==2 and juego["seleccion_computadora"]==1:
                        print("Ganaste, tú elegiste papel y la computadora piedra")
                elif juego["seleccion_jugador"]==1 and juego["seleccion_computadora"]==2:
                        print("Perdiste, tú elegiste piedra y la computadora papel")
                elif juego["seleccion_jugador"]==2 and juego["seleccion_computadora"]==3:
                        print("Perdiste, tú elegiste papel y la computadora tijera")
                elif juego["seleccion_jugador"]==3 and juego["seleccion_computadora"]==1:
                        print("Perdiste, tú elegiste tijera y la computadora piedra")

                contador+=1

        nuevo_juego=input("Nuevo juego: Si/No ")

    else:
        agradecimiento()
        print("los parámetros del juego fueron: ", modalidad_juego)

elif modalidad_juego['modalidad de juego']==2:

    jugador2=input("Jugador 2 coloca tu nombre: ")


    nuevo_juego=input("Nuevo juego: Si/No ")


    while nuevo_juego=="si" or nuevo_juego=="SI" or nuevo_juego=="Si" or nuevo_juego=="s" or nuevo_juego=="S":

        contador=0

        while contador<3:


            jugador1_2={"seleccion_jugador1" : int(input("Jugador 1, elige: 1=Piedra, 2=Papel, 3=Tijera ")), "seleccion_jugador2": int(input("Jugador 2, elige: 1=Piedra, 2=Papel, 3=Tijera "))}

            while jugador1_2["seleccion_jugador1"] !=1 and jugador1_2["seleccion_jugador1"] !=2 and jugador1_2["seleccion_jugador1"] !=3:
                eleccion_incorrecta()
                jugador1_2["seleccion_jugador1"]=int(input("Escoge de nuevo: 1=Piedra, 2=Papel, 3=Tijera "))
                
            while jugador1_2["seleccion_jugador2"] !=1 and jugador1_2["seleccion_jugador2"] !=2 and jugador1_2["seleccion_jugador2"] !=3:
                eleccion_incorrecta()
                jugador1_2["seleccion_jugador2"]=int(input("Escoge de nuevo: 1=Piedra, 2=Papel, 3=Tijera "))


            if jugador1_2["seleccion_jugador1"]==jugador1_2["seleccion_jugador2"]:
                 empate()
                 contador+=1

            elif jugador1_2["seleccion_jugador1"]!=jugador1_2["seleccion_jugador2"]:

                if jugador1_2["seleccion_jugador1"]==1 and jugador1_2["seleccion_jugador2"]==3:
                    print("Ganó jugador 1, jugador 1 eligió piedra y jugador 2 tijera")

                elif jugador1_2["seleccion_jugador1"]==3 and jugador1_2["seleccion_jugador2"]==2:
                    print("Ganó jugador 1, jugador 1 eligió tijera y jugador 2 papel")
                    
                elif jugador1_2["seleccion_jugador1"]==2 and jugador1_2["seleccion_jugador2"]==1:
                    print("Ganó jugador 1, jugador 1 eligió papel y jugador 2 piedra")
                
                elif jugador1_2["seleccion_jugador1"]==1 and jugador1_2["seleccion_jugador2"]==2:
                    print("Ganó jugador 2, jugador 2 eligió papel y jugador 1 piedra")

                elif jugador1_2["seleccion_jugador1"]==2 and jugador1_2["seleccion_jugador2"]==3:
                    print("Ganó jugador 2, jugador 2 eligió tijera y jugador 1 papel")

                elif jugador1_2["seleccion_jugador1"]==3 and jugador1_2["seleccion_jugador2"]==1:
                    print("Ganó jugador 2, jugador 2 eligió piedra y jugador 1 tijera")

                contador=contador+1

        nuevo_juego=input("Nuevo juego: Si/No ")

    else:
        
        agradecimiento()

        modalidad_juego["jugador_2"]=jugador2

        print("los parámetros del juego fueron: ", modalidad_juego)