class Institucion:
    estudiantes_totales = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        estudiante.institucion = self
        Institucion.estudiantes_totales += 1



class Estudiante:
    def __init__(self, nombre, nota1, nota2, institucion):
        self._nombre = nombre
        self._nota1 = self._validar_nota(nota1)
        self._nota2 = self._validar_nota(nota2)
        self.institucion = institucion
        institucion.agregar_estudiante(self)

    def _validar_nota(self, nota):
        if nota > 0 & nota <=5:
            return nota
        else:
            print("Las notas deben ser menores que 0 y mayores de 5")

   

    def mostrar_informacion(self):
        promedio = (self._nota1 + self._nota2) / 2
        print(f"Nombre: {self._nombre}")
        print(f"Nota 1: {self._nota1}")
        print(f"Nota 2: {self._nota2}")
        print(f"Nota Promedio: {promedio}")
        print(f"Institución: {self.institucion.nombre}")

    def set_nota1(self, nota):
        if 0 < nota <= 5:
            self._nota1 = nota
        else:
            print("Nota 1 debe estar entre 1 y 5")

    def set_nota2(self, nota):
        if 0 < nota <= 5:
            self._nota2 = nota
        else:
            print("Nota 2 debe estar entre 1 y 5")

    @classmethod
    def ver_escala(cls):
        escala = [
            ["0 a 2.9", "BAJA"],
            ["3 a 3.9", "MEDIA"],
            ["4 a 4.5", "ALTA"],
            ["4.6 a 5", "SOBRESALIENTE"]
        ]
        print(escala)