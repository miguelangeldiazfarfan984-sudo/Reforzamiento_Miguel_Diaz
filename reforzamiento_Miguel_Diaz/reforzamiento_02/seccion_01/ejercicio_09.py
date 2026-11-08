# Nombre: Miguel Angel Diaz Farfan
# Reforzamiento 02 - Ejercicio 09: Cálculo del Índice de Masa Corporal (IMC)

# 1. Datos de la persona
nombre = "Miguel Diaz"
peso = 78.5        # kilogramos
estatura = 1.72    # metros

# 2. Cálculo del IMC
imc = peso / (estatura ** 2)

# 3. Clasificación según el IMC
if imc < 18.5:
    clasificacion = "Bajo peso"
elif imc < 25:
    clasificacion = "Peso normal"
elif imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

# 4. Mostrar resultados
print(f"Nombre: {nombre}")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"IMC calculado: {imc:.2f}")
print(f"Clasificación: {clasificacion}")
