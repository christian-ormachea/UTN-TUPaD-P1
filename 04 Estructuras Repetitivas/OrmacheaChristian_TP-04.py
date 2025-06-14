for cont in range(10,5,-1):
    print(cont, "Debo aprender ciclos")
    #for que va de 10 a 5 en decremento de -1
    #for cont in range(5):
    # el de arriba es un for que va de 0 a 5 (normal)
cont = 1
while cont <= 5:
    print(cont, "Debo aprender ciclos")
    cont = cont + 1
    
# 1 
def numeros():    
    for index in range(100):
        print("numero: ", index)
# 2
def cantidadDigitos():
    numero_usuario = input("Ingrese un numero: \n")
    cont = 0
    for digito in numero_usuario:
        if digito.isdigit():
            cont += 1    
    print(f"La cantidad de digitos es: {cont}")
    
# 3
def sumatoria():
    numero_rango1 = int(input("Ingrese el numero donde quiere iniciar a sumar: \n"))
    numero_rango2 = int(input("Ingrese el numero donde quiere parar de sumar: \n"))
    sumatoria = 0
    while numero_rango2 != numero_rango1:
        sumatoria += numero_rango2
        numero_rango2 -= 1
    print(f"La cantidad total entre esos dos valores es: {sumatoria}")
# 4
def hasta0():
    numero_usuario = int(input("Ingrese un numero \n"))
    sumatoria = 0 + numero_usuario
    while numero_usuario != 0:
        print("Hasta que no presione 0 no se detendra. \n")
        numero_usuario = int(input("Ingrese un numero \n"))
        sumatoria += numero_usuario
print(f"El total ingresado fue {sumatoria}")
# 5
from random import randint
def juego_num():
    numero_aleatorio = randint(0,9)
    numero_usuario = int(input("Ingrese un numero para adivinar (Entre 0 y 9)"))
    while numero_usuario != numero_aleatorio:
        numero_usuario = int(input("Lo lamento intente devuelta! (Entre 0 y 9)"))
    print(f"Felicidades! el numero es {numero_usuario}")    
#6
def imprimir_numeros():
    for index in range(100,0,-1):
        if(index % 2 == 0):
            print(index)
#7
def suma_numeros():
    numero_usuario = int(input("Ingrese un numero hasta donde quiere sumar"))
    num_actual = 0
    sumatoria = 0
    while num_actual != numero_usuario:
        sumatoria += num_actual
        num_actual += 1
#8
def contar_usuario():
    numeros_pares = []
    numeros_impares = []
    numeros_negativos = []
    numeros_positivos = []
    for index in range(100,0,-1):
        numero_usuario = int(input("Ingrese un numero: \n"))
        if numero_usuario % 2 == 0:
            numeros_pares.append(numero_usuario)
        else:
            numeros_impares.append(numero_usuario)
        if numero_usuario > 0:
            numeros_positivos.append(numero_usuario)
        else:
            numeros_negativos.append(numero_usuario)
        
    print(f"La cantidad de numeros pares es: {len(numeros_pares)}\n")
    print(f"La cantidad de numeros impares es: {len(numeros_impares)} \n")
    print(f"La cantidad de numeros positivos es: {len(numeros_positivos)} \n")
    print(f"La cantidad de numeros negativos es: {len(numeros_negativos)} \n")
#9
def numeros_media():
    sumatoria = 0
    for numero in range(100,0,-1):
        numero_usuario = int(input("Ingrese un numero: \n"))
        sumatoria += numero_usuario
    promedio = sumatoria / 100
    print(f"El promedio de los numeros ingresados es: {promedio}")
#10
def numero_dadovuelta():
    numero = input("Ingrese un número: ")
    invertido = ""

    for digito in numero:
        invertido = digito + invertido
    print("El numero invertido es: ", invertido)
    