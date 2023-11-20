from Tipos import *

class Manejador:
    def __init__(self):
        self.tipos = {}

    def crearTipoAtomico(self, nombre, representacion, alineacion):
        if nombre.lower() not in self.tipos:
            self.tipos[nombre.lower()] = TipoAtomico(nombre, representacion, alineacion)
        else:
            print(f"Error: El tipo '{nombre}' ya existe.")


    def crearTipoRegistro(self, nombre, campos):
        if nombre.lower() not in self.tipos:
            # Verificar si todos los tipos de los campos ya han sido definidos
            for campo in campos:
                if campo.lower() not in self.tipos:
                    print(f"Error: El tipo '{campo}' no ha sido definido.")
                    return
            self.tipos[nombre.lower()] = TipoRegistro(nombre, campos)
        else:
            print(f"Error: El tipo '{nombre}' ya existe.")


    def crearTipoRegistroVariante(self, nombre, campos):
        if nombre.lower() not in self.tipos:
            # Verificar si todos los tipos de los campos ya han sido definidos
            for campo in campos:
                if campo.lower() not in self.tipos:
                    print(f"Error: El tipo '{campo}' no ha sido definido.")
                    return
            self.tipos[nombre.lower()] = TipoRegistroVariante(nombre, campos)
        else:
            print(f"Error: El tipo '{nombre}' ya existe.")

    def getRep(self, tipo):
        if isinstance(tipo, str):
            t = self.tipos[tipo.lower()]
        else:
            t = tipo
        
        if isinstance(t, TipoAtomico):
            return t.representacion
        
        elif isinstance(t, TipoRegistro):
            tipos = [self.tipos[k] for k in t.campos]
            return sum([self.getRep(i) for i in tipos])
        
        else:
            tipos = [self.tipos[k] for k in t.campos]
            return max([self.getRep(i) for i in tipos])

    def calcularBytesSinEmpaquetar(self, tipo):
        return self.getRep(tipo)
        
    def calcularBytesEmpaquetado(self, tipo):
        return self.getRep(tipo) + (tipo.alineacion - self.getRep(tipo) % tipo.alineacion) % tipo.alineacion
        
    def calcularBytesReordenado(self, tipo):
        return self.getRep(tipo) + (tipo.alineacion - self.getRep(tipo) % tipo.alineacion) % tipo.alineacion
        
    def describirTipo(self, nombre):
        if nombre in self.tipos:
            tipo = self.tipos[nombre]
            print(f"Nombre: {tipo.nombre}")
            print(f"Representacion: {self.getRep(tipo)} bytes")
            print(f"Alineacion: {tipo.alineacion} bytes")
            
            # Describir sin empaquetar
            sin_empaquetar = self.calcularBytesSinEmpaquetar(tipo)
            print(f"Bytes sin empaquetar: {sin_empaquetar}")

            # Describir empaquetado
            empaquetado = self.calcularBytesEmpaquetado(tipo)
            print(f"Bytes empaquetados: {empaquetado}")

            # Describir reordenado
            reordenado = self.calcularBytesReordenado(tipo)
            print(f"Bytes reordenados: {reordenado}")
        else:
            print(f"Error: El tipo '{nombre}' no ha sido definido.")

