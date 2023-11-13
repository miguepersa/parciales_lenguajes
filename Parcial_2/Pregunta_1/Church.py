class Church(object):

    def __init__(self, n: int = 0, other=None):
        try:
            assert(n >= 0)

            if other is not None:
                if not isinstance(other, Church):
                    raise TypeError("La entrada debe ser de tipo Church tambien")

                self.val = other
                self.n = other.n + 1

            else:
                self.n = n
                self.val = None
                if (n > 0):
                    self.val = Church(n=n-1)

        except AssertionError as ae:
            raise ValueError("La entrada debe ser positiva")

    def __add__(self, other):
        k = other.n + self.n
        return Church(n=k)
    
    def __mul__(self, other):
        k = other.n * self.n
        return Church(n=k)