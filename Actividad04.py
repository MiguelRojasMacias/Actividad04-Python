'''
Actividad 04 - Elaborar un código donde implementemos funciones, 
condicionales, ciclos, uso de clases y funciones
'''
# -- Declaracion de clase --
class operaciones:

    def _init_(self,L,B,A,R): # declaramos nuestro constructor
        self.L = L
        self.B = B
        self.A = A
        self.R = R

    def Cuadrado(self): #función para sacar el área del cuadrado
        self.L = float(input("Ingresa un lado del cuadrado para sacar su área: "))
        areaCuadrado = self.L*4; #Lado * 4
        print(f"El area del cuadrado con los lados {self.L} es -> {areaCuadrado:.2f}") #El :.2F es para que simplemente nos imprima dos decimales

    def Triangulo(self): #función para sacar el área de un triángulo
        self.B = float(input("Ingresa el tamaño de la base: "))
        self.A = float(input("Ingresa el tamaño de la altura: "))
        areaTriangulo = self.B * self.A/2; #Base * Altura / 2
        print(f"El área del triángulo con base {self.B} y altura {self.A} es -> {areaTriangulo:.2f}") #El :.2F es para que simplemente nos imprima dos decimales

    def Circulo(self):
        self.R = float(input("Ingresa el radio del círculo: "))
        areaCirculo = math.pi * self.R**2; # Pi * R^2
        print(f"El área del circulo con radio {self.R} es -> {areaCirculo:.2f}") #El :.2F es para que simplemente nos imprima dos decimales

# -- Declaracion de funcion Zodiacal --
def Zodiacal():
    dia = int(input("Digita el día de tu nacimiento: "))
    mes  = input("Digita el mes de tu nacimiento: ").upper() #con la funcion upper convertimos a mayusculas la cadena para evitar errores

    if((dia >= 1 and dia <= 19) and (mes == 'ENERO')):
        print("Eres Capricornio / Diciembre 22 - Enero 19")
    elif((dia >= 20 and dia <= 30) and (mes == 'ENERO')):
        print("Eres Acuario / Enero 20 - Febrero 18")
    elif((dia >= 1 and dia <= 18) and (mes == 'FEBRERO')):
        print("Eres Acuario / Enero 20 - Febrero 18")
    elif((dia >= 19 and dia <= 30) and (mes == 'FEBRERO')):
        print("Eres Piscis / Febrero 19 - Marzo 20")
    elif((dia >= 1 and dia <= 20) and (mes == 'MARZO')):
        print("Eres Piscis / Febrero 19 - Marzo 20")
    elif((dia >= 21 and dia <= 30) and (mes == 'MARZO')):
        print("Eres Aries / Marzo 21 - Abril 19")
    elif((dia >= 1 and dia <= 19) and (mes == 'ABRIL')):
        print("Eres Aries / Marzo 21 - Abril 19")
    elif((dia >= 20 and dia <= 30) and (mes == 'ABRIL')):
        print("Eres Tauro / Abril 20 - Mayo 20")
    elif((dia >= 1 and dia <= 20) and (mes == 'MAYO')):
        print("Eres Tauro / Abril 20 - Mayo 20")
    elif((dia >= 21 and dia <= 30) and (mes == 'MAYO')):
        print("Eres Géminis / Mayo 21 - Junio 20")
    elif((dia >= 1 and dia <= 20) and (mes == 'JUNIO')):
        print("Eres  Géminis / Mayo 21 - Junio 20")
    elif((dia >= 21 and dia <= 30) and (mes == 'JUNIO')):
        print("Eres Cáncer / Junio 21 - Julio 22")
    elif((dia >= 1 and dia <= 22) and (mes == 'JULIO')):
        print("Eres Cáncer / Junio 21 - Julio 22")
    elif((dia >= 23 and dia <= 30) and (mes == 'JULIO')):
        print("Eres Leo / Julio 23 - Agosto 22")
    elif((dia >= 1 and dia <= 22) and (mes == 'AGOSTO')):
        print("Eres Leo / Julio 23 - Agosto 22")
    elif((dia >= 23 and dia <= 30) and (mes == 'AGOSTO')):
        print("Eres Virgo / Agosto 23 - Septiembre 22")
    elif((dia >= 1 and dia <= 22) and (mes == 'SEPTIEMBRE')):
        print("Eres Virgo / Agosto 23 - Septiembre 22")
    elif((dia >= 23 and dia <= 30) and (mes  == 'SEPTIEMBRE')):
        print("Eres Libra / Septiembre 23 - Octubre 22")
    elif((dia >= 1 and dia <= 22) and (mes == 'OCTUBRE')):
        print("Eres Libra / Septiembre 23 - Octubre 22")
    elif((dia >= 23 and dia <= 30) and ( mes == 'OCTUBRE')):
        print("Eres Escorpio / Octubre 23 - Noviembre 21")
    elif((dia >= 1 and dia <= 21) and (mes == 'NOVIEMBRE')):
        print("Eres Escorpio / Octubre 23 - Noviembre 21")
    elif((dia >= 22 and dia <= 30) and (mes  == 'NOVIEMBRE')):
        print("Eres Sagitario / Noviembre 22 - Diciembre 21")
    elif((dia >= 1 and dia <= 21) and (mes == 'DICIEMBRE')):
        print("Eres Sagitario  / Noviembre 22 - Diciembre 21")
    elif((dia >= 22 and dia <= 30) and (mes == 'DICIEMBRE')):
        print("Eres Capricornio / Diciembre 22 - Enero 19")
    else:
        print("ERROR -> Algo Salio mal...")

# -- Declaracion de funcion Factorial --
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# --  Declaracion de la  funcion Calcular e --
def Calcular_e():# declaramos las variables
    limite = 4
    e = 0
    n = 0
    while n < limite: # inicio del ciclo while
        e += 1/factorial(n)
        n = n + 1
    
    print(f"El valor de e es -> {e}")

import math #Esta importacion nos ayuda para poder importar el valor de pi y que sea mas exacto el dato

# -- Declaración de Menú --
print("\n\t.:Menú:.\n"
      "1. Sacar el área a un cuadrado\n"
      "2. Sacar el área a un triángulo\n"
      "3. Sacar el área a un círculo\n"
      "4. Conocer tu signo zodiacal\n"
      "5. Cálculo del Número e\n"
      "6. Salir\n")
menu = int(input("Eliga una opción -> "))

obj = operaciones() # creammos la estancia del objeto

if menu == 1:
    print("\n.:Sacar el área a un cuadrado:.\n\n")
    obj.Cuadrado()
elif menu == 2:
    print("\n.:Sacar el área a un triangulo:.\n\n")
    obj.Triangulo()
elif menu == 3:
    print("\n.:Sacar el área a un círculo:.\n\n")
    obj.Circulo()
elif menu == 4:
    print("\n.:Conocer tu signo zodiacal:.\n\n")
    Zodiacal()
elif menu == 5:
    print(".:Cálculo del Número e:.\n\n")
    Calcular_e()
elif menu == 6:
    print(".:Salir:.\n\n"
          "HASTA PRONTO, GRACIAS POR USAR EL SOFTWARE :)\n\n")
else:
    print("ERROR -> No es una opción del menú")
