class Interprete:
    def __init__(self, lenguaje_base, lenguaje):
        self.lenguaje_base = lenguaje_base
        self.lenguaje = lenguaje

    def __str__(self) -> str:
        return f"{self.lenguaje} -> {self.lenguaje_base}"