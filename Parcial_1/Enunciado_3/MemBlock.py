"""
    Autor: Miguel Perez
    Carnet: 15-11126
    Clase de MemBlock
"""

class MemBlock(object):
    """
        Clase que representa un bloque de memoria

        Atributos:
            - rango: Rango de direcciones del bloque
            - capacidad: Capacidad del bloque
    """

    def __init__(self, inicio, final):
        """
            Constructor de la clase
            Input:
                - inicio: Primera direccion del bloque
                - final: ultima direccion del bloque
        """

        self.rango = (inicio, final)
        self.capacidad = final - inicio + 1


    def inicio(self):
        """
            Retorna la direccion inicial del bloque
        """
        return self.rango[0]
    
    def final(self):
        """
            Retorna la direccion final del bloque
        """
        return self.rango[1]
    
    def divide(self):
        """
            Metodo que divide un bloque en dos bloques de igual capacidad 
            y que estan contiguos uno del otro..

            Output:
                - MemBlock(1):  MemBlock que comienza en la direccion inicial
                                y termina en el punto medio de este MemBlock.
                
                - MemBlock(2):  MemBlock que comienza en el punto medio
                                y termina en la direccion final de este MemBlock.
        """
        medio = self.inicio() + (self.capacidad // 2) 
        return MemBlock(self.inicio(), medio - 1), MemBlock(medio, self.final())
    
    def __str__(self):
        return str(self.rango)