class Arbol(object):
    """
    Esta clase representa un nodo de árbol binario.
    """

    def __init__(self, val, l=None, r=None):
        """
        Constructor de la clase Arbol.

        Args:
            val (int): El valor del nodo.
            l (Arbol): El hijo izquierdo del nodo.
            r (Arbol): El hijo derecho del nodo.
        """

        # Verifica si los hijos izquierdo y derecho son instancias de la clase Arbol.
        if (l is not None and not isinstance(l, Arbol)) or (r is not None and not isinstance(r, Arbol)):
            raise TypeError("Los valores de las ramas deben ser instancias de la clase Arbol")
        
        # Establece los atributos izquierdo, derecho y valor del nodo.
        self.l = l
        self.r = r
        self.val = val
        
    def preorder(self):
        """
        Realiza un recorrido preorder del árbol.

        Retorna:
            str: Una representación de cadena del recorrido preorder.
        """

        # Si existen ambos hijos izquierdo y derecho, visita la raíz, luego recorre el subárbol izquierdo y el subárbol derecho.
        if self.l is not None and self.r is not None:
            return f"{self.val} {self.l.preorder()} {self.r.preorder()}"
        
        # Si solo existe el hijo izquierdo, visita la raíz, luego recorre el subárbol izquierdo.
        elif self.l is not None and self.r is None:
            return f"{self.val} {self.l.preorder()}"
        
        # Si solo existe el hijo derecho, visita la raíz, luego recorre el subárbol derecho.
        elif self.l is None and self.r is not None:
            return f"{self.val} {self.r.preorder()}"
        
        # Si no existen ni el hijo izquierdo ni el derecho, simplemente visita la raíz.
        else:
            return f"{self.val}"
        
    def postorder(self):
        """
        Realiza un recorrido postorder del árbol.

        Retorna:
            str: Una representación de cadena del recorrido postorder.
        """

        # Si existen ambos hijos izquierdo y derecho, recorre el subárbol izquierdo, luego el subárbol derecho, y finalmente visita la raíz.
        if self.l is not None and self.r is not None:
            return f"{self.l.postorder()} {self.r.postorder()} {self.val}"
        
        # Si solo existe el hijo izquierdo, recorre el subárbol izquierdo, luego visita la raíz.
        elif self.l is not None and self.r is None:
            return f"{self.l.postorder()} {self.val}"
        
        # Si solo existe el hijo derecho, recorre el subárbol derecho, luego visita la raíz.
        elif self.l is None and self.r is not None:
            return f"{self.r.postorder()} {self.val}"
        
        # Si no existen ni el hijo izquierdo ni el derecho, simplemente visita la raíz.
        else:
            return f"{self.val}"
        