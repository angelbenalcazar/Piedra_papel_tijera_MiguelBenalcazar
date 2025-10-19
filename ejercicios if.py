x=10
y=5

if x!=y:
    print("x mayor que y")
elif x>y:
    print("x sigue siendo mayor que y")
elif x>y:
    print("x seguirá siendo mayor que y")

#estructura de datos

#para imprimir o llamar a un solo elemento

ejemplo1=(1,2,3,4)
print(ejemplo1[2])

#para imprimir los elementos entre el número inicial y final, sin contar el final

ejemplo2=(1,2,3,4,5,6,7,8,9,10)
print(ejemplo2[0:10])

ejemplo3=(-2,-1,0,1,2,3,4,5,6,7,8,9,10)
print(ejemplo3[8:10])

#para imprimir los elementos del final al inicio

ejemplo4=("juan","pedro","andres","p","j")
print(ejemplo4[2])
print(ejemplo4[::-1])

#para sumar dos tuplas, es necesario crear una tercera tupla con la suma de los dos anteriores

ejemplo5=ejemplo2+ejemplo4
print(ejemplo5)

#para contar cuántos elementos hay del mismo

ejemplo6=ejemplo1+ejemplo3
print(ejemplo6.count(0))

#Para reemplazar un elemento con otro en una lista

lista=["juan","perez","bob"]
lista[1]="vera"
print(lista)

#para mostrar en lista los elementos se usa for luego un nombre de una variable in lista, para imprimir o llamar se usa la nueva variable que se usa en la lista anterior

for list in lista:
    print(list)

lista3=[1,2,3]

#para sumar más elementos a una lista

lista+=lista3

print(lista)

for i in lista:
    print(i)

#para sumar otro elemento en una posición específica
lista4=[1,2,3,4,6,5,7,1]
lista4.insert(1, 2)
lista4.sort()
print(lista4)

#para borrar un elemento

lista4=[1,2,3,4,6,5,7, "Juan"]
lista4.remove(2)
print(lista4)

lista4=[1,2,3,4,6,5,7,"Juan"]
lista4.pop(2)
print(lista4)


