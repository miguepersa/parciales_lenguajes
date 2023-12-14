from Tipos import Tipo


class Manejador(object):

    def __init__(self):
        '''
            Constructor de la clase.
            Crea una tabla de simbolos vacia
        '''
        
        self.sym_table = {"" : None}

    def add_class(self, name: str, parent: str = "", metodos: list = []):
        '''
            Funcion que crea una clase nueva
        '''
        if (name not in self.sym_table.keys() and parent in self.sym_table.keys()
            and len(metodos) == len(set(metodos))):
            new = Tipo(nombre=name, parent=self.sym_table[parent], metodos=metodos)
            self.sym_table[name] = new
            return f"Clase {new} creada con exito"

        if name in self.sym_table.keys():
            return f"Error: la clase {name} ya existe"
        
        elif parent not in self.sym_table.keys():
            return f"Error: la clase {parent} no existe"
        
        elif len(metodos) != len(set(metodos)):
            return f"Error: metodos duplicados en la lista"
        
        return "Error desconocido"


    def describe_class(self, clase: str):
        if not clase in self.sym_table.keys():
            return f"La clase {clase} no existe"
        
        if clase == "":
            return f"Debe proporcionar un nombre valido"

        tipo = self.sym_table[clase]

        metodos = []
        metodos_tipo = []
        
        while tipo is not None:
            for m in tipo.metodos:
                if m not in metodos:
                    metodos_tipo.append(f"{m} -> {tipo.nombre} :: {m}")
                    metodos.append(m)

            tipo = tipo.parent


        final_str = ""
        for m in metodos_tipo:
            final_str += m + "\n"

        return final_str