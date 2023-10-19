class Vertice:
    '''
        Vertices del grafo.

        Input:
            - data: Nombre del lenguaje
            - n: valor auxiliar de posicion en el grafo
    '''
    def __init__(self, data, n):
        self.data = data
        self.numero = n
        self.vecinos = []

class Lado:
    '''
        Lado del grafo v1 -> v2

        Input:
            - v1: Vertice inicial
            - v2: Vertice final            
    '''
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

class Grafo:
    def __init__(self, vertices):
        '''
            Constructor del grafo

            Input: 
                - vertices: lista de vertices del grafo
        '''

        self.nvertices = len(vertices) # Numero de vertices del grafo
        self.lados = [] # Lados del grafo
        self.vertices = vertices # Vertices del grafo
        self.adyacencias = {v : [] for v in vertices} # Lista de adyacencias del grafo

    def addLado(self, v1, v2):
        # Agregar un lado v1 -> v2 al grafo
        l = Lado(v1,v2)
        self.lados.append(l)
        self.adyacencias[v1].append(v2)

    def hayCamino(self, s, d="LOCAL"):
        # BFS que verifica si hay camino de s -> d
    
        # Se marcan todas las vertices como no visitadas
        visited = [False for i in range(self.nvertices)]
  
        # Cola del BFS
        q = []
  
        q.append(s)
        visited[s.numero] = True
  
        while q:
 
            n = q.pop(0)
             
            if n.data == d:
                   return True
 
            for i in self.adyacencias[n]:
                if visited[i.numero] == False:
                    q.append(i)
                    visited[i.numero] = True
        return False