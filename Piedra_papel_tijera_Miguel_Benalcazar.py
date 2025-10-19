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










juego={'modalidad de juego': int(input("Jugador contra computadora, escribe: 1. Jugador1 contra jugador2, escribe: 2. ")), 'jugador': input("Coloca tu nombre: ")}


if juego['modalidad de juego']==1:


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
        print("Gracias por jugar ", juego['jugador'])

        print(juego)



elif juego['modalidad de juego']==2:

    jugador2=input("Jugador 2 coloca tu nombre: ")


    nuevo_juego=input("Nuevo juego: Si/No ")


    while nuevo_juego=="si" or nuevo_juego=="SI" or nuevo_juego=="Si" or nuevo_juego=="s" or nuevo_juego=="S":

        contador=0

        while contador<3:

            eleccion_jugador1=int(input("Jugador 1, elige: 1=Piedra, 2=Papel, 3=Tijera "))
            eleccion_jugador2=int(input("Jugador 2, elige: 1=Piedra, 2=Papel, 3=Tijera "))

            

            while eleccion_jugador1 !=1 and eleccion_jugador1 !=2 and eleccion_jugador1 !=3:
                print("Jugador 1, elige un número entre el 1 al 3, tú pusiste ", eleccion_jugador1)
                eleccion_jugador1=int(input("Jugador 1, elige: 1=Piedra, 2=Papel, 3=Tijera "))


                
            while eleccion_jugador2 !=1 and eleccion_jugador2 !=2 and eleccion_jugador2 !=3:
                print("Jugador 2, elige un número entre el 1 al 3, tú pusiste ", eleccion_jugador2)
                eleccion_jugador2=int(input("Jugador 2, elige: 1=Piedra, 2=Papel, 3=Tijera "))
                


            if eleccion_jugador1==eleccion_jugador2:

                if eleccion_jugador1==1 and eleccion_jugador2==1:
                    print("Empate, los dos sacaron piedra")

                elif eleccion_jugador1==2 and eleccion_jugador2==2:
                    print("Empate, los dos sacaron papel")

                elif eleccion_jugador1==3 and eleccion_jugador2==3:
                    print("Empate, los dos sacaron tijera")
                
                contador=contador+1

            elif eleccion_jugador1!=eleccion_jugador2:

                if eleccion_jugador1==1 and eleccion_jugador2==3:
                    print("Ganó jugador 1, jugador 1 eligió piedra y jugador 2 tijera")

                elif eleccion_jugador1==3 and eleccion_jugador2==2:
                    print("Ganó jugador 1, jugador 1 eligió tijera y jugador 2 papel")
                    
                elif eleccion_jugador1==2 and eleccion_jugador2==1:
                    print("Ganó jugador 1, jugador 1 eligió papel y jugador 2 piedra")
                
                elif eleccion_jugador1==1 and eleccion_jugador2==2:
                    print("Ganó jugador 2, jugador 2 eligió papel y jugador 1 piedra")

                elif eleccion_jugador1==2 and eleccion_jugador2==3:
                    print("Ganó jugador 2, jugador 2 eligió tijera y jugador 1 papel")

                elif eleccion_jugador1==3 and eleccion_jugador2==1:
                    print("Ganó jugador 2, jugador 2 eligió piedra y jugador 1 tijera")

                contador=contador+1

        nuevo_juego=input("Nuevo juego: Si/No ")

    else:
        print("Gracias por jugar ", juego['jugador'], "y ", jugador2)

        print(juego)