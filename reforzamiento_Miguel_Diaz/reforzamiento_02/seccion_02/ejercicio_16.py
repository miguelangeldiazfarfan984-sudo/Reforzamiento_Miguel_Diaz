# Nombre: Miguel Angel Diaz Farfan
# Reforzamiento 02 - Ejercicio 16: Reorganización de invitados

# 1. Lista original (datos obligatorios del enunciado)
invitados = ["Luis", "Ana", "Raúl", "Pedro", "Miguel", "Katherine", "Fiorella"]

# 2 al 5. Separar los nombres según su cantidad de letras (impar o par)
nombres_impares = []
nombres_pares = []
for invitado in invitados:
    if len(invitado) % 2 != 0:
        nombres_impares.append(invitado)   # longitud impar
    else:
        nombres_pares.append(invitado)     # longitud par

# 6 y 7. Unir: primero impares, luego pares, conservando el orden original
lista_reorganizada = nombres_impares + nombres_pares

# 8. Mostrar resultados
print(f"Lista original: {invitados}")
print(f"Nombres con longitud impar: {nombres_impares}")
print(f"Nombres con longitud par: {nombres_pares}")
print(f"Lista reorganizada: {lista_reorganizada}")
