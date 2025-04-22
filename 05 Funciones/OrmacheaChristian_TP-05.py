import math

def imprimir_hola_mundo():
    print("Hola mundo")

def saludar_usuario(nombre):
    print(f"Hola {nombre}")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Hola soy {nombre} {apellido}, tengo {edad} años, y vivo en {residencia}")

def calcular_area_circulo(radio):
    print(f"El area del circulo es: {radio**2 * math.pi}")

def calcular_perimetro_circulo(radio):
    print(f"El perimetro del circulo es: {2 * math.pi * radio}")

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

def tabla_multiplicar(numero):
    for index in range(1,10,1):
        print(f"La tabla del {numero} por {index} es: {numero * index}")

def operaciones_basicas(a, b):
    print(f"(Suma: {a + b} ,Resta: {a - b})")
    print(f"(Multiplicacion: {a * b}, Division: {a / b})")

def calcular_imc(peso, altura):
    return peso / altura

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

def main():
    num1 = int(input("ingrese el primer numero: \n"))
    num2 = int(input("Ingrese el segundo numero: \n"))
    num3 = int(input("Ingrese el tercer numero: \n"))
    print("El promedio de los 3 numeros es: " + calcular_promedio(num1,num2,num3))

if __name__ == "__main__":
    main()




