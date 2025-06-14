#Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero*factorial(numero-1)
def mostrar_pantalla():
    num=int(input("Ingrese el numero a calcular el factorial de todos los numeros enteros entre el 0 y el numero ingresado"))
    for i in range(num):
        print(f"El factorial del numero {i} es: { factorial(i) }")
        
#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def posicion():
    pos = int(input("Hasta que posicion queres ver la serie de Fibonacci? "))

    print("Serie de Fibonacci hasta la posición", pos, "es:")
    for i in range(pos + 1):
        print(fibonacci(i), end=" ")

#Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
#algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def prueba():
    base = int(input("Introduce la base: "))
    exponente = int(input("Introduce el exponente: "))

    resultado = potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")

#Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
def prueba_decimal_a_binario():
    numero = int(input("Introduce un número entero positivo: "))
    
    if numero == 0:
        print("0")
    else:
        print(decimal_a_binario(numero))
