import math #Librería que nos permite utilizar pi

def calcular_area_cuadrado(lado): #Función para calcular el área del cuadrado
  try: #Bloque de código que se debe ejecutar si todo ocurre correctamente
    lado = float(lado) #Nuestra variable debe ser flotante
    if lado <= 0: #Validación para que el número no sea negativo
      return None #Sentencia para evitar que se ingresen datos que no sean números
    return lado ** 2 #Regresa el área del cuadrado
  except (ValueError, TypeError): #Bloque de código que se ejecuta si algo no está bien dentro del Try
    return None #Sentencia para evitar que se ingresen datos que no sean números

def calcular_area_circulo(radio): #Función para calcular el área del circulo
  try: #Bloque de código que se debe ejecutar si todo ocurre correctamente
    radio = float(radio) #Nuestra variable debe ser flotante
    if radio <= 0: #Validación para que el número no sea negativo
      return None #Sentencia para evitar que se ingresen datos que no sean números
    return math.pi * (radio ** 2) #Calculo del area mediante PI y el radio al cuadrado
  except (ValueError, TypeError): #Bloque de código que se ejecuta si algo no está bien dentro del Try
    return None #Sentencia para evitar que se ingresen datos que no sean números
  
def calcular_area_triangulo(base, altura): #Función para calcular el área del circulo
  try: #Bloque de código que se debe ejecutar si todo ocurre correctamente
    base = float(base) #Variable flotante de la base
    altura = float(altura) #Variable flotante de la altura
    if base <= 0 or altura <= 0: #Validacion para que ninguno de los valoreas sean negativos
      return None #Sentencia para evitar que se ingresen datos que no sean números
    return (base * altura) / 2 #Calculo del area del triángulo
  except (ValueError, TypeError): #Bloque de código que se ejecuta si algo no está bien dentro del Try
    return None #Sentencia para evitar que se ingresen datos que no sean números

#while True: #Utilizamos el while para crear una lista que le permita al usuario elegir la función

  #print("¡Bienvenido al programa para calcular áreas de figuras!") #Mensaje de bienvenida
  #print("Indique por favor la acción a realizar:") #Indicación al usuario
  #print("Opción 1: Calcular el área de un cuadrado") #Opción 1 para calcular el área del cuadrado
  #print("Opción 2: Calcular el área de un círculo") #Opción 2 para calcular el área del círculo
  #print("Opción 3: Calcular el área de un triángulo") #Opción 3 para cualcular el área del triángulo
  #print("Opción 4: Salir del programa ") #Opción para finalizar el programa

  #try: #Bloque de código que se debe ejecutar si todo ocurre correctamente
   # op = int(input())#Variable entero para seleccionar las opciones
  #except ValueError: #Bloque de código que se ejecuta si algo no está bien dentro del Try
  #  print("Opción inválida. Debe ingresar un número del 1 al 4.") #Mensaje de error
  #  continue #Continua el código

  #if op == 1: #Condicional para la opción 1
  #  lado = input("Ingrese la medida de un lado del cuadrado: ") #Se solicita el lado del cuadrado
  #  area = calcular_area_cuadrado(lado) #Meidante la variable area, mandamos a llamar la función
  #  if area is not None: #Si nuestra area tiene un valor procede a
  #      print(f"El área del cuadrado es: {area}") #Mensaje donde se imprime el área del cuadrado
  #  else: #Condicional que se usa en caso de que el if no se cumpla
  #      print("Entrada no válida. Debe ser un número mayor que cero.") #Mensaje de error
  #  continue #Funciona para que el programa se siga ejecutando después de se haya cumplido la primera opción

  #elif op == 2: #Plabra reservada para usar más condiciones dentro de un if
  #  radio = input("Ingrese el radio del círculo: ") #Se solicita el radio del circulo
  #  area = calcular_area_circulo(radio) #Mediante la variable area, mandamos a llamar a la función
  #  if area is not None: #Si nuestra area tiene un valor procede a
  #      print(f"El área del círculo es: {area}") #Mensaje donde se imprime el área del circulo
  #  else: #Condicional que se usa en caso de que el if no se cumpla
  #      print("Entrada no válida. Debe ser un número mayor que cero.") #Mensaje de error
  #  continue #Funciona para que el programa se siga ejecutando después de se haya cumplido la segunda opción
  
  #elif op == 3:#Plabra reservada para usar más condiciones dentro de un if
  #  base = input("Ingrese la base del triángulo: ") #Se solicita la base del triángulo
  #  altura = input("Ingrese la altura del triángulo: ") #Se solicita la altura del triángulo
  #  area = calcular_area_triangulo(base, altura) #Mediante la variable area, mandamos a llamar a la función
  #  if area is not None: #Si nuestra area tiene un valor procede a
  #      print(f"El área del triángulo es: {area}") #Mensaje donde se imprime el área del circulo
  #  else: #Condicional que se usa en caso de que el if no se cumpla
  #      print("Entradas no válidas. Ambos valores deben ser números mayores que cero.") 
  #  continue #Funciona para que el programa se siga ejecutando después de se haya cumplido la primera opción
  
  #elif op == 4:#Plabra reservada para usar más condiciones dentro de un if
  #  print("¡Gracias por usar el programa!")
  #  break #Funciona para romper el código y que se deje de ejecutar
  
  #else:
  #  print("La opción no es válida") #Opción inválida
  # continue #Continua el programa 