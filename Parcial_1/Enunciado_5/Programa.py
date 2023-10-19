class Programa:
    def __init__(self, nombre, lenguaje):
        self.nombre = nombre
        self.lenguaje = lenguaje

    def __str__(self) -> str:
        return f"{self.nombre}: {self.lenguaje}"