'''
Actividad 04 - Elaborar un código donde implementemos funciones, 
condicionales, ciclos, uso de clases y funciones
'''

# -- Declaracion de funciones --
def Cuadrado(): #función para sacar el área del cuadrado
    L = float(input("Ingresa un lado del cuadrado para sacar su área: "))
    areaCuadrado = L*4; #Lado * 4
    print(f"El area del cuadrado con los lados {L} es -> {areaCuadrado:.2f}") #El :.2F es para que simplemente nos imprima dos decimales

def Triangulo(): #función para sacar el área de un triángulo
    B = float(input("Ingresa el tamaño de la base: "))
    A = float(input("Ingresa el tamaño de la altura: "))
    areaTriangulo = B*A/2; #Base * Altura / 2
    print(f"El área del triángulo con base {B} y altura {A} es -> {areaTriangulo:.2f}") #El :.2F es para que simplemente nos imprima dos decimales

def Circulo():
    R = float(input("Ingresa el radio del círculo: "))
    areaCirculo = math.pi * R**2; # Pi * R^2
    print(f"El área del circulo con radio {R} es -> {areaCirculo:.2f}") #El :.2F es para que simplemente nos imprima dos decimales

import math #Esta importacion nos ayuda para poder importar el valor de pi y que sea mas exacto el dato

# declaramos nuestro menu
print("\n\t.:Menú:.\n"
      "1. Sacar el área a un cuadrado\n"
      "2. Sacar el área a un triángulo\n"
      "3. Sacar el área a un círculo\n"
      "4. Conocer tu signo zodiacal\n"
      "5. Cálculo del Número e\n"
      "6. Salir\n")
menu = int(input("Eliga una opción -> "))

if menu == 1:
    print("\n.:Sacar el área a un cuadrado:.\n\n")
    Cuadrado()
elif menu == 2:
    print("\n.:Sacar el área a un triangulo:.\n\n")
    Triangulo()
elif menu == 3:
    print("\n.:Sacar el área a un círculo:.\n\n")
    Circulo()
elif menu == 4:
    print("\n.:Conocer tu signo zodiacal:.\n\n")
elif menu == 5:
    print(".:Cálculo del Número e:.\n\n")
elif menu == 6:
    print(".:Salir:.\n\n"
          "HASTA PRONTO, GRACIAS POR USAR EL SOFTWARE :)\n\n")
else:
    print("ERROR -> No es una opción del menú")
