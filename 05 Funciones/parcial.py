num1 = 3
vector = [4, 6, 1]

mayor = vector[0]  # mayor = 4 (inicializado con el primer elemento)

for i in range(1, num1):  # Recuadro 1: ⇔ → num1 (itera sobre índices 1 y 2)
    if vector[i] > mayor:  # Recuadro 2: ⇔ → > (compara si el elemento actual es mayor)
        mayor = vector[i]

print(mayor)  # Salida: 6