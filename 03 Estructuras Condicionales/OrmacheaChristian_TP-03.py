# 1 - Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
def edad_usuario():
    edad_ingresada = int(input("Ingrese la edad del usuario: \n"))
    if edad_ingresada > 18:
        print("Es mayor de edad")

#2 - Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

def nota_usuario():
    nota_usuario = int(input("Ingrese la nota del usuario: \n"))
    if nota_usuario >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

# 3 - Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el 
# uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

def solo_pares():
    numero_ingresado = int(input("Ingrese un numero par: \n"))
    if numero_ingresado % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")

# 4 - Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de
# las siguientes categorías pertenece

def edad_usuario():
    edad_usuario = int(input("Ingrese la edad del usuario: \n"))
    if edad_usuario < 12:
        print("Niño/a")
    elif (edad_usuario >= 12 or edad_usuario < 18):
        print("Adolescente")
    elif (edad_usuario >= 18 or edad_usuario < 30):
        print("Adulto/a Joven")
    else:
        print("Adulto/a")

# 5 

def contras():
    contra = input("Ingrese su contraseña: \n")
    if(contra.len() >= 8 or contra.len() <= 14):
        print("Ha ingresado una contraseña correcta. ")
    else:
        print("Porfavor, ingrese una contraseña entre 8 y 14 caracteres")

# 6

from statistics import mode, median, mean
import random

def la_mediana():
    numero_aleatorio = [random.randint(1,100) for i in range(50)] 
    moda = numero_aleatorio.mode()
    mediana = numero_aleatorio.median()
    media = numero_aleatorio.mean()
    
    if(media > mediana and mediana > moda):
        print("Sesgo positivo a la derecha")
    elif(media < mediana and mediana < moda):
        print("Sesgo negativo a la izquierda")
    else: 
        print("Sin sesgo")
    
# 7

def termina_vocal():
    frase_palabra = input("Ingrese una frase o palabra: \n").capitalize()
    if(frase_palabra[-1] == 'a' or frase_palabra[-1] == 'e' or frase_palabra[-1] == 'i' or frase_palabra[-1] == 'o' frase_palabra[-1] == 'u')
        frase_palabra = frase_palabra + '!'
    
    print(frase_palabra)

#8

def nombre_opcion():
    nombre = input("Ingrese su nombre: \n")
    print("1. Mayusculas")
    print("2. Minusculas")
    print("3. Solo la primera mayuscula")
    opcion = int(input("Ingrese una opcion: \n"))
    
    if(opcion == 1):
        nombre.upper()
    elif(opcion == 2):
        nombre.lower()
    else:
        nombre.title()
    
    print(nombre)
    
# 9 

def magnitud_terremoto():
    magnitud = int(input("Ingrese la magnitud"))
    if(magnitud < 3):
        print("Muy leve")
    elif(magnitud >= 3 or magnitud < 4):
        print("Leve")
    elif(magnitud >= 4 or magnitud < 5):
        print("Moderado")
    elif(magnitud >= 5 or magnitud < 6):
        print("Fuerte")
    elif(magnitud >= 6 or magnitud < 7):
        print("Muy fuerte")
    else:
        print("Extremo")
        
# 10

def estacion_anio():
    hemisferio = input("En que hemisferio se encuentra? (N para norte, S para sur): \n ")
    if hemisferio.upper() not in ['N', 'S']:
        print("Error: Hemisferio debe ser N (Norte) o S (Sur)")
        return

    mes = int(input("En que mes se encuentra? (1-12): "))
    
    if mes < 1 or mes > 12:
        print("Error: Mes debe estar entre 1 y 12")
        return
    
    dia = int(input("En que dia se encuentra? (1-31): "))
    
    if dia < 1 or dia > 31:
        print("Error: Día debe estar entre 1 y 31")
        return
    
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion_norte = "invierno"
        estacion_sur = "verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion_norte = "primavera"
        estacion_sur = "otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion_norte = "verano"
        estacion_sur = "invierno"
    else:  # 21 sep - 20 dic
        estacion_norte = "otoño"
        estacion_sur = "primavera"
        
    if hemisferio == 'N':
        print(f"Actualmente es {estacion_norte} en el hemisferio norte.")
    else:
        print(f"Actualmente es {estacion_sur} en el hemisferio sur.")