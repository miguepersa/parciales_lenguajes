class Arbol(object):

    def __init__(self, val: int, l=None, r=None):
        self.l = l
        self.r = r
        self.val = val

    def preorder(self):
        if self.l is not None and self.r is not None:
            return f"{self.val} {self.l.preorder()} {self.r.preorder()}"
        
        elif self.l is not None and self.r is None:
            return f"{self.val} {self.l.preorder()}"
        
        elif self.l is None and self.r is not None:
            return f"{self.val} {self.r.preorder()}"
        
        else:
            return f"{self.val}"
        
    def postorder(self):
        if self.l is not None and self.r is not None:
            return f"{self.l.postorder()} {self.r.postorder()} {self.val}"
        
        elif self.l is not None and self.r is None:
            return f"{self.l.postorder()} {self.val}"
        
        elif self.l is None and self.r is not None:
            return f"{self.r.postorder()} {self.val}"
        
        else:
            return f"{self.val}"
        

        
def esMaxHeap(arbol: Arbol):
    if Arbol is None:
        return True
    
    return (arbol.l is None or (arbol.val >= arbol.l.val and esMaxHeap(arbol.l))) and (arbol.r is None or (arbol.val >= arbol.r.val and esMaxHeap(arbol.r)))

def esMaxHeapSimetrico(arbol: Arbol):
    return esMaxHeap(arbol) and (arbol.preorder() == arbol.postorder())