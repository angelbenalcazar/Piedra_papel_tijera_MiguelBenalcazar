import random

#función principal

def elementos(a,b, jugador1, jugador2):
    if a==b:
        if a==1:
            print("Empate, los dos sacaron piedra")
        if a==2:
            print("Empate, los dos sacaron papel")
        if a==3:
            print("Empate, los dos sacaron tijera")

    elif a==1 and b==3:
        print (f"Ganó {jugador1}. {jugador1} sacó piedra y {jugador2} sacó tijera")
    elif a==2 and b==1:
        print (f"Ganó {jugador1}. {jugador1} sacó papel y {jugador2} sacó piedra")
    elif a==3 and b==2:
        print (f"Ganó {jugador1}. {jugador1} sacó tijera y {jugador2} sacó papel")
    elif a==3 and b==1:
        print (f"Ganó {jugador2}. {jugador1} sacó tijera y {jugador2} sacó piedra")
    elif a==2 and b==3:
        print (f"Ganó {jugador2}. {jugador1} sacó papel y {jugador2} sacó tijera")
    elif a==1 and b==2:
        print (f"Ganó {jugador2}. {jugador1} sacó piedra y {jugador2} sacó papel")
    else:
        print ("Se eligió un número no válido")

#función de agradecimiento

def agradecimiento():
     if modalidad_juego["modalidad de juego"]==1:
        print("Gracias por jugar", modalidad_juego["jugador"])
     else:
         print(f"Gracias por jugar {modalidad_juego['jugador']} y {modalidad_juego['jugador_2']}")




#Inicio del juego

print("Bienvenido al juego Piedra, papel o tijera.") 
print("Tendrás la oportunidad de jugar contra la computadora o contra otro jugador en una ronda de tres partidas.")

modalidad_juego={
    'modalidad de juego': int(input("Elección jugador contra computadora, escribe: 1. Elección Jugador_1 contra jugador_2, escribe: 2: ")),
    'jugador': input("Coloca tu nombre: ")
    }

#Juego entre jugador contra computadora

if modalidad_juego['modalidad de juego']==1:
    print(f"Genial {modalidad_juego['jugador']}, vas a jugar contra la computadora")


    nuevo_juego=input("Nuevo juego: Si/No ").lower()

    while nuevo_juego in ["si", "s"]:

        contador=0
        
        while contador<3:

            juego={
                "seleccion_jugador": int(input(f"{modalidad_juego['jugador']} elige: 1=Piedra, 2=Papel, 3=Tijera ")),
                "seleccion_computadora": random.randint(1,3)
                    }

            elementos(juego["seleccion_jugador"],juego["seleccion_computadora"], modalidad_juego["jugador"], "computadora")

            if juego["seleccion_jugador"] in [1,2,3]:
                contador+=1

        nuevo_juego=input("Nuevo juego: Si/No ").lower()

    else:
        agradecimiento()


#Juego entre dos personas

elif modalidad_juego['modalidad de juego']==2:
    

    jugador2=input("Jugador 2 coloca tu nombre: ")

    modalidad_juego["jugador_2"]=jugador2

    print(f"Genial, la ronda será {modalidad_juego['jugador']} contra {modalidad_juego['jugador_2']}")


    nuevo_juego=input("Nuevo juego: Si/No ").lower()


    while nuevo_juego in ["si","s"]:

        contador=0

        while contador<3:


            jugador1_2={
                "seleccion_jugador1" : int(input(f"{modalidad_juego['jugador']} elige: 1=Piedra, 2=Papel, 3=Tijera ")),
                "seleccion_jugador2": int(input(f"{modalidad_juego['jugador_2']}, elige: 1=Piedra, 2=Papel, 3=Tijera "))
                }
            
            if jugador1_2["seleccion_jugador1"] in [1,2,3] and jugador1_2["seleccion_jugador2"] in [1,2,3]:
                elementos(jugador1_2["seleccion_jugador1"],jugador1_2["seleccion_jugador2"], modalidad_juego['jugador'], modalidad_juego['jugador_2'])
                contador+=1
            else:
                print("Uno de los jugadores eligió un número no válido. Inténtenlo de nuevo.")

        nuevo_juego=input("Nuevo juego: Si/No ").lower()

    else:

        agradecimiento()

else:
    print("Opción no válida, elige entre 1 y 2")