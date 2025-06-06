###
# EJERCICIOS
###
# import os
# os.system("clear") # Limpia la consola

# # Ejercicio 1: Determinar el mayor de dos números
# print("Ejercicio 1: Determinar el mayor de dos números")
# num1  = float(input("Introduce el primer número: "))
# num2 = float(input("Introduce el segundo número: "))
# if num1 > num2:
#     print(f"El mayor es: {num1}")
# elif num2 > num1:
#     print(f"El mayor es: {num2}")
# else:
#     print("Los números son iguales")


# import os 
# os.system("clear") # Limpia la consola

# # Ejercicio 2: Calculadora simple
# print("Ejercicio 2: Calculadora simple")
# print("Selecciona una operación:")
# print("1. Suma")
# print("2. Resta")
# print("3. Multiplicación")
# print("4. División")
# opcion = input("\nIntroduce el número de la operación: ")
# num1 = float(input("Introduce el primer número: "))
# num2 = float(input("Introduce el segundo número: "))

# # Aplicación de la operación
# if opcion == "1":
#     resultado = num1 + num2
#     print(f"El resultado de la suma es: {resultado}")
# elif opcion == "2":
#     resultado = num1 - num2
#     print(f"El resultado de tu resta es: {resultado}")
# elif opcion == "3":
#     resultado = num1 * num2
#     print(f"El resultado de la Multiplicación es: {resultado}")
# else:
#     resultado = num1 / num2
#     print(f"El resultado de la División es: {resultado}")

# import os 
# os.system("clear") # Limpia la consola

# ### Ejercicio 3: Año bisiesto
# print("Ejercicio 3: Año bisiesto")
# # Pide al usuario que introduzca un año y determina si es bisiesto.
# # Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# year = int(input("Ingresa un año para determinar si es bisiesto o no: "))
# if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
#     print("El año es bisiesto")
# else:
#     print("El año no es bisiesto")


import os
os.system("clear") # Limpia la consola

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

# age = int(input("Ingresa la edad para clasificarte: "))
# if age <= 2:
#     print("You are a baby")
# elif age <= 12:
#     print("You are a kid")
# elif age <= 17:
#     print("You are a teenager")
# elif age <= 64:
#     print("You are an adult")
# else:
#     print("You are a senior adult")
