class Traductor:
    def __init__(self, lenguaje_base, lenguaje_origen, lenguaje_destino):
        self.lenguaje_base = lenguaje_base
        self.lenguaje_origen = lenguaje_origen
        self.lenguaje_destino = lenguaje_destino

    def __str__(self) -> str:
        return f"{self.lenguaje_base}: {self.lenguaje_origen} -> {self.lenguaje_destino}"