###
# 04 - variables
# Python permite almacenar valores en variables
###

print("Variables:")

name = "Elvis"
age = 20

#Tipado dinámico: el tipo de dato se determina en tiempo de ejecución
# no tienes que declararlo explicitamente

#Tipado fuerte: no puedes hacer operaciones entre tipos de datos diferentes

#f-strings: permite interpolar variables dentro de cadenas de texto
print(f"Name: {name}, Age: {age}")

#No recomendada forma de asignar variables
name, age, city = "Elvis", 20, "Quito"

#Convenciones de nombres de variables
mi_nombre_de_variable = "Variable con guiones bajos" # snake_case
miNombreDeVariable = "Variable con mayusculas al inicio de cada palabra" # PascalCase
MINOMBREDEVARIABLE = "Variable en mayusculas" # UPPERCASE - constante

#Nombres no validos de variables
# 1nombre = "No valido" # No puede empezar con un numero
# nombre con espacios = "No valido" # No puede tener espacios
# nombre-con-guiones = "No valido" # No puede tener guiones
# nombre@con@simbolos = "No valido" # No puede tener simbolos especiales
