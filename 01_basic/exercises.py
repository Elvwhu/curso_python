###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

print("Hola me llamo Elvis, pero puedes decirme Jonathan \ny vivo en Quito, Ecuador")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print("El tipo de dato de a es:", type(a))
print("El tipo de dato de b es:", type(b))
print("El tipo de dato de c es:", type(c))
print("El tipo de dato de d es:", type(d))
print("El tipo de dato de e es:", type(e))

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

print(int("12345"))
print(float("12345"))
print(int(3.99))  # Esto redondea hacia abajo, el resultado es 3

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

name= "Elvis"
age = 20
height = 1.75

print(f"Hola! Me llano {name}, tengo {age} años, mido {height} metros")

