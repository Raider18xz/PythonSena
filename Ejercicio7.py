from Estudiantes7 import Estudiante
from Estudiantes7 import Institucion

nombre_institucion = input("Ingrese el nombre de la institución: ")
institucion_principal = Institucion(nombre_institucion)

while True:
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    nota1 = float(input("Ingrese la primera nota mayor que 0: "))
    nota2 = float(input("Ingrese la segunda nota mayor que 0: "))

   
    estudiante = Estudiante(nombre_estudiante, nota1, nota2, institucion_principal)
    estudiante.mostrar_informacion()

    continuar = input("¿Desea continuar? Ingrese 0 para continuar o 1 para salir: ")
    if continuar == "1":
        break

print("Estudiantes totales:", Institucion.estudiantes_totales)