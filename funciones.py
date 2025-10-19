#def saludar(nombre):
#    print("Hola ", nombre + " espero que tengas un gran día")

#nombre_usuario=input("Ingrese tu nombre: ")
#saludar(nombre_usuario)



def division(a,b,c):
    resultado=(a+b+c)/3
    print("la división es: ", resultado)

num1=float(input("ingrese un número: "))
num2=float(input("ingrese otro número: "))
num3=float(input("ingrese un número: "))

operacion=division(num1, num2, num3)
print(operacion)







import random

def elementos(a,b):
    if a==1 and b==1:
        print("empate, los dos sacaron piedra")
    elif a==2 and b==2:
        print ("empate, los dos sacaron papel")
    elif a==3 and b==3:
        print ("empate, los dos sacaron tijera")
    elif a==1 and b==3:
        if modalidad_juego["jugador"] and juego["seleccion_computadora"]:
            print (f"Ganó {modalidad_juego['jugador']}. {modalidad_juego['jugador']} sacó piedra y Computadora sacó tijera")
        else:
            print(f"Ganó {modalidad_juego['jugador']}. {modalidad_juego['jugador']} sacó piedra y {modalidad_juego['jugador_2']} sacó tijera")
    elif a==2 and b==1:
        if modalidad_juego["jugador"] and juego["seleccion_computadora"]:
            print (f"Ganó {modalidad_juego['jugador']}. {modalidad_juego['jugador']} sacó papel y Computadora sacó piedra")
        else:
            print(f"Ganó {modalidad_juego['jugador']}. {modalidad_juego['jugador']} sacó papel y {modalidad_juego['jugador_2']} sacó piedra")
        
    elif a==3 and b==2:
        if modalidad_juego["jugador"] and juego["seleccion_computadora"]:
            print (f"Ganó {modalidad_juego['jugador']}. {modalidad_juego['jugador']} sacó tijera y Computadora sacó papel")
        elif jugador1_2["seleccion_jugador1" and jugador1_2["seleccion_jugador2"]]:
            print(f"Ganó {modalidad_juego['jugador']}. {modalidad_juego['jugador']} sacó tijera y {modalidad_juego['jugador_2']} sacó papel")
    elif a==3 and b==1:
        if modalidad_juego["jugador"] and juego["seleccion_computadora"]:
            print (f"Perdió {modalidad_juego['jugador']}. {modalidad_juego['jugador']} sacó tijera y Computadora sacó piedra")
        else:
            print(f"Perdió {modalidad_juego['jugador']}. {modalidad_juego['jugador']} sacó tijera y {modalidad_juego['jugador_2']} sacó piedra")
    elif a==2 and b==3:
        if modalidad_juego["jugador"] and juego["seleccion_computadora"]:
            print (f"Perdió {modalidad_juego['jugador']}. {modalidad_juego['jugador']} sacó papel y Computadora sacó tijera")
        else:
            print(f"Perdió {modalidad_juego['jugador']}. {modalidad_juego['jugador']} sacó papel y {modalidad_juego['jugador_2']} sacó tijera")
    elif a==1 and b==2:
        if modalidad_juego["jugador"] and juego["seleccion_computadora"]:
            print (f"Perdió {modalidad_juego['jugador']}. {modalidad_juego['jugador']} sacó piedra y Computadora sacó papel")
        else:
            print(f"Perdió {modalidad_juego['jugador']}. {modalidad_juego['jugador']} sacó piedra y {modalidad_juego['jugador_2']} sacó papel")
        
    else:
        print ("Se eligió un número no válido")


