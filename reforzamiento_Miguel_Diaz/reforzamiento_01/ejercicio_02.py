# Miguel Angel Diaz Farfan
# Reforzamiento 01 - Ejercicio 02: Operaciones y conversiones de tipos de datos
# 1. Variable int con un valor positivo mayor que 10
valor_inicial = 47

# 2. Multiplicar el valor inicial por 10
multiplicacion = valor_inicial * 10

# 3. Restar 10 al resultado anterior
resta = multiplicacion - 10

# 4. Convertir el resultado final a float
valor_convertido = float(resta)

# 5. Dividir el valor convertido entre 3
division = valor_convertido / 3

# 6. Obtener el residuo de la división entre 3
residuo = valor_convertido % 3

# 7. Mostrar los resultados
print(f"Valor inicial: {valor_inicial}")
print(f"Multiplicación por 10: {multiplicacion}")
print(f"Resta de 10: {resta}")
print(f"Conversión a float: {valor_convertido}")
print(f"División entre 3: {division:.2f}")
print(f"Residuo de la división: {residuo}")
print(f"Tipo de dato convertido: {type(valor_convertido)}")
