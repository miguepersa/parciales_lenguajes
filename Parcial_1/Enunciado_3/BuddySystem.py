"""
    Autor: Miguel Perez
    Carnet: 15-11126
    Clase de BuddySystem
"""

from MemBlock import MemBlock
import math

class BuddySystem(object):
    """
        Implementacion del Buddy System
    """


    def __init__(self, nbloques: int):
        """
            Constructor de la clase

            Input:
                - nbloques: cantidad de bloques que manejara el sistema.      

        """

        # diccionario que lleva los bloques ocupados y sus nombres
        self.ocupados = {}

        # cantidad de bloques de memoria disponibles
        self.nbloques = math.floor(math.log2(nbloques))

        # Lista de bloques de memoria libres
        self.mem_libre = [ [] for i in range(self.nbloques+1) ]
        self.mem_libre[-1].append(MemBlock(0, 2**self.nbloques - 1))

    def reservar(self, nombre, cant):
        """
            Metodo para reservar la memoria del sistema

            Input: 
                - nombre: nombre del bloque
                - cant: cantidad de memoria del bloque
        """

        if nombre in self.ocupados.keys():
            return (f"El nombre \"{nombre}\" ya esta reservado")
        
        # posicion del bloque en la lista
        p_bloque = math.ceil(math.log2(cant))

        # si la posicion esta disponible, se usa
        if len(self.mem_libre[p_bloque]) > 0:
            block = self.mem_libre[p_bloque].pop(0)

            self.ocupados[nombre] = block

            return(f"\"{nombre}\" se alojo en el bloque {block}")
        
        # Si no hay bloques libres, se itera hacia los de mayor tamanio
        i = p_bloque + 1 

        while (i != len(self.mem_libre)):

            if len(self.mem_libre[i]) > 0:
                break

            i += 1

        # Si se tiene que i es el final de la lista, no hay memoria libre
        if (i == len(self.mem_libre)):
            return ("No hay espacio disponible")
        
        # Por el contrario, se divide el bloque hasta que sea el tamanio correcto
        div_bloque = self.mem_libre[i].pop(0)

        while (i-1 >= p_bloque):

            b0, b1 = div_bloque.divide()

            self.mem_libre[i-1].append(b1)

            div_bloque = b0
            i -= 1

        
        self.ocupados[nombre] = div_bloque

        return(f"\"{nombre}\" se alojo en el bloque {div_bloque}")
    
    def liberar(self, nombre):
        """
            Metodo para liberar memoria

            Input:
                - nombre: nombre del bloque a ser liberado
        """

        bloque = self.ocupados.get(nombre, None)

        if not bloque:
            return (f"No existe bloque con nombre \"{nombre}\"")
        

        p_bloque = math.ceil(math.log2(bloque.capacidad))
        self.mem_libre[p_bloque].append(bloque)

        self.unir(bloque)

        del self.ocupados[nombre]
        return (f"Se libero el bloque \"{nombre}\"")
    
    def unir(self, bloque):
        """
            Funcion que combina los bloques siempre que se puedan combinar.
            Al unir 2 bloques se intenta unir con otros de igual capacidad.

            Input:
                - bloque: bloque que se intenta unir a su buddy
        """

        if not bloque:
            return
        
        # Posicion de la lista correspondiente al bloque
        p_bloque = math.ceil(math.log2(bloque.capacidad))

        # Numero de buddy del bloque agregado
        buddy = bloque.inicio() / bloque.capacidad

        if buddy % 2 != 0:
            dir_buddy = bloque.inicio() - bloque.capacidad
        
        else:
            dir_buddy = bloque.inicio() + bloque.capacidad

        unido = None

        for i, b in enumerate(self.mem_libre[p_bloque]):
            if b.inicio() == dir_buddy:

                if buddy % 2 == 0:
                    unido = MemBlock(bloque.inicio(), b.final())
                else:
                    unido = MemBlock(b.inicio(), bloque.final())
                
                self.mem_libre[p_bloque+1].append(unido)
                self.mem_libre[p_bloque].pop()
                self.mem_libre[p_bloque].pop(i)

        
        self.unir(unido)

    def __str__(self):
        """
            funcion que muestra el estado actual del sistema de memoria
        """
        libres = []

        for l in self.mem_libre:
            libres += l

        libres.sort(key= lambda x : x.inicio())

        ocupados = sorted(list(self.ocupados.values()), key= lambda x: x.inicio())

        out = ""
        out += "Bloques libres:\n" + " ".join(map(str,libres)) + "\n\n" + "Bloques ocupados:\n"
        
        for k in self.ocupados.keys():
            out += f"- {k} : {self.ocupados[k]}\n"

        return out