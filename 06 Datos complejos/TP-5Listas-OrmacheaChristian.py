
def uno_al_100():
    multiplos_4 = []
    for i in range(1,101):
        if i % 4 == 0:
            multiplos_4.append(i)
    return multiplos_4
#2
def el_penultimo():
    lista = [1,2,3,4,5]
    return(lista[-2])
#3
def lista_vacia():
    lista_vacia = []
    lista_vacia.append(input("Ingrese la primera palabra: \n"))
    lista_vacia.append(input("Ingrese la segunda palabra: \n"))
    lista_vacia.append(input("Ingrese la tercera palabra: \n"))
    print(lista_vacia)
#4
def animales():
    animales = ["perro", "gato", "conejo", "pez"]
    animales[1] = "loro"
    animales[-1] = "oso"
    print(animales)
#5 Esta funcion remueve el numero mas grande de la lista de numeros y luego imprime por pantalla el resultado.
#6
def los2primeros():
    lista_diez_treinta = []
    for i in range(10, 30, 5):
        lista_diez_treinta.append(i)
    print(lista_diez_treinta[0])
    print(lista_diez_treinta[1])
#7
def reemplazar():
    autos = ["sedan", "polo", "suran", "gol"]
    autos[1] = "Kangoo"
    autos[2] = "Fiorino"
#8
def dobles():
    dobles = []
    dobles.append(5*2)
    dobles.append(10*2)
    dobles.append(15*2)
    print(dobles)
#9
def compras():
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
    compras[2].append("jugo")
    compras[1][1] = "tallarines"
    compras.remove(compras[0][0])
    print(compras)
#10
def lista_anidada():
    lista_anidada = [
        15, True,[25.5,57.9,30.6],False
    ]
    print(lista_anidada)