class TipoAtomico:
    def __init__(self, nombre, representacion, alineacion):
        self.nombre = nombre
        self.representacion = representacion
        self.alineacion = alineacion

class TipoRegistro:
    def __init__(self, nombre, campos):
        self.nombre = nombre
        self.campos = campos

class TipoRegistroVariante:
    def __init__(self, nombre, campos):
        self.nombre = nombre
        self.campos = campos