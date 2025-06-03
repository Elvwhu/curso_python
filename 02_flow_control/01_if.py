###
# 01 - if
# Python permite ejecutar código si se cumplen ciertas condiciones.
###
import os
os.system("clear") # Limpia la consola

print("Condicionales en Python")
print("=====================================")
print("Ejemplo if")

age = 20
if age > 18:
    print("Eres mayor de edad")

print ("\nCondiciones múltiples")
print("=====================================")
print ("\nOperador AND")
age = 16
tiene_novia = True
if age > 18 and tiene_novia:
    print("Eres mayor de edad y tienes novia")
else:
    print("Anda a buscar una novia PESADOOO")

print ("====================================")
print ("\nOperador OR")
tienes_carnet = False
if age >= 18 or tienes_carnet:
    print("Puedes conducir en la isla")
else:
    print("No tienes ninguno, no puedes conducir")

print ("\n Anidar condicionales")
print ("====================================")
tienes_dinero = True
if age > 18:
    if tienes_dinero:
        print ("Puedes ir a la discoteca")
    else:
        print ("No tienes dinero para ir a la discoteca")
else :
    print ("No puedes ir a la discoteca, eres menor de edad")

# Operadores de comparación
print ("\nOperadores de comparación")
print ("====================================")
print ("5 > 3:", 5 > 3) # True
print ("5 < 3:", 5 < 3) # False
print ("5 >= 3:", 5 >= 3) # True (mayor o igual)
print ("5 <= 3:", 5 <= 3) # False (menor o igual)
print ("5 == 3:", 5 == 3) # False (igual)   
print ("5 != 3:", 5 != 3) # True (diferente)

# Operadores lógicos (AND, OR, NOT)
print ("\nOperadores lógicos")
print ("====================================")
print ("True and True:", True and True) # True
print ("True and False:", True and False) # False
print ("False and True:", False and True) # False
print ("False and False:", False and False) # False
print ("True or True:", True or True) # True
print ("True or False:", True or False) # True
print ("False or True:", False or True) # True
print ("False or False:", False or False) # False
print ("not True:", not True) # False
print ("not False:", not False) # True

