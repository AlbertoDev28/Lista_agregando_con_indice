"""Enunciado: Crea una lista con los números del 1 al 5. Usa insert()
para agregar el número 0 en la
primera posición, luego usa extend() para agregar
los números 6 y 7 al final, y finalmente usa sum()
para calcular la suma de los elementos"""

lista_numero20 = [1, 2, 3, 4, 5]
lista_numero20.insert(0,0)
lista_numero20.extend([6,7])
suma = sum(lista_numero20)
print(f"La lista de los numero es: {lista_numero20} \nLa suma de los elementos es: {suma}")


