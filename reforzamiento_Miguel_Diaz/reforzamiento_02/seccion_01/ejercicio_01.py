# Nombre: Miguel Angel Diaz Farfan
# Reforzamiento 02 - Ejercicio 01: Manipulación de cadenas de texto

# 1. Variables con nombre, apellido paterno y apellido materno
nombre = "Miguel"
apellido_paterno = "Diaz"
apellido_materno = "Farfan"

# 2. Concatenar los tres datos con espacios
nombre_completo = nombre + " " + apellido_paterno + " " + apellido_materno

# 3. Crear el saludo
mi_saludo = "¡HI " + nombre_completo + "!"

# 4. Cantidad de caracteres (incluye espacios)
cantidad_caracteres = len(nombre_completo)

# 5. Mostrar resultados
print(f"Saludo: {mi_saludo}")
print(f"Nombre completo: {nombre_completo.upper()}")
print(f"Cantidad de caracteres: {cantidad_caracteres}")
