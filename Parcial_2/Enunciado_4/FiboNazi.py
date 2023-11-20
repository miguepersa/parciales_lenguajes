import csv, time

X = 1
Y = 2
Z = 6

alfa = ((X + Y) % 5) + 3
beta = ((Y + Z) % 5) + 3

def FiboNazi(n):
    if n < 0:
        return "Ingrese un n >= 0"
        
    if n >= 0 and n < alfa * beta:
        return n
    
    return sum([FiboNazi(n - beta * i) for i in range(1, alfa+1)])


def FiboNaziTail(n, step = alfa*beta - 1, tail=[i for i in range(alfa*beta)]):
    if n < 0:
        return "Ingrese un n >= 0"
        
    if n >= 0 and n < alfa * beta:
        return n
    
    if step == n:
        return tail[-1]

    val = sum([tail[len(tail) - beta*i] for i in range(1, alfa+1)])
    return FiboNaziTail(n, step + 1, tail + [val])

def FiboNaziIter(n):
    if n < 0:
        return "Ingrese un n >= 0"
        
    if n < alfa*beta:
        return n
    
    arr = [i for i in range(alfa*beta)]
    
    for i in range(alfa*beta, n+1):
        arr.append(sum([arr[len(arr) - beta*i] for i in range(1, alfa+1)]))

    return arr[-1]

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time