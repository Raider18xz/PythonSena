class Estudiante:
    def __init__(self, nombre, nota1, nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2

    def obtener_nota_promedio(self):
 
        return (self.nota1 + self.nota2) / 2
 

    def mostrar_informacion(self):
     if self.nota1 > 0 and self.nota2 > 0:
            promedio = self.obtener_nota_promedio()
            print(f"Nombre: {self.nombre}")
            print(f"Nota 1: {self.nota1}")
            print(f"Nota 2: {self.nota2}")
            print(f"Nota Promedio: {promedio}")
     else:
        print("Las notas no pueden ser negativas o un 0")
