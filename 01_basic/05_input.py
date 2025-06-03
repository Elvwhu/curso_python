###
# 05 - input
# Python permite recibir datos del usuario a través de la consola.
###

name = input("Hola, ¿cuál es tu nombre?\n")  # input() is used to take input from the user.
age = input(f"Perfecto {name}!, ¿cuántos años tienes?\n")  
print(f"Genial {name}, tienes {age} años y ya estás aprendiendo Python!\n")

country, city = input("¿En qué país y ciudad vives?\n").split()  # split() is used to separate the input by comma.
print(f"Vives en {city}, {country}.\n") 
