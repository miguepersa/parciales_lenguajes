from FiboNazi import *
import matplotlib.pyplot as plt 

MAX_N = 150

funciones = [FiboNazi, FiboNaziTail, FiboNaziIter]

ns = [i for i in range(alfa*beta, MAX_N+1,5)]

tiempos = {
    'FiboNazi' : [], 
    'FiboNaziTail' : [], 
    'FiboNaziIter' : []
}

for f in funciones:
    name = f.__name__

    print(f"Executing \'{name}\'...")

    for n in ns:
        r, t = measure_time(f, n)
        tiempos[name].append(t)


    plt.plot(ns, tiempos[name], label = name, marker='o', linestyle='dashed')

plt.legend()
plt.show()