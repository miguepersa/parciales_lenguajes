class Tipo(object):

    def __init__(self, nombre: str, metodos: list[str] = [], parent: object = None):
        self.nombre = nombre
        self.metodos = metodos
        self.parent = parent

    def __str__(self):
        return f"<class: \'{self.nombre}\'>"