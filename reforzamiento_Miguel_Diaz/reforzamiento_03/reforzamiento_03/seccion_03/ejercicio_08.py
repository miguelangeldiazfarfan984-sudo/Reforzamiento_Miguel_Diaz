"""Ejercicio 08 - Registro de alumnos"""

class Alumno:
    def __init__(self, nombre, edad, nota_final):
        self.nombre, self.edad, self.nota_final = nombre, edad, nota_final

    # Muestra los datos del alumno
    def mostrar_datos(self):
        print("Nombre: {} | Edad: {} | Nota final: {}".format(self.nombre, self.edad, self.nota_final))

    # Retorna la condición académica
    def condicion(self):
        return "Aprobado" if self.nota_final >= 11 else "Desaprobado"

# Lista de objetos Alumno recorrida para mostrar a todo el grupo
alumnos = [Alumno("Diego", 21, 15), Alumno("Sofía", 19, 8), Alumno("Mateo", 22, 12)]
for alumno in alumnos:
    alumno.mostrar_datos()
    print("Condición:", alumno.condicion())
