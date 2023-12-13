import os
from threading import Thread, Lock

lock_results = Lock()

results = []

def contador(path='.', results=results):
    #print(path)
    if not os.path.isdir(path):
        raise Exception("la direccion dada no es un directorio")

    folders = []
    files = []

    for f in os.listdir(path):

        if os.path.isfile(os.path.join(path,f)):
            files.append(f)
        elif os.path.isdir(os.path.join(path,f)):
            folders.append(f)

    for f in folders:
        t = Thread(target=contador, args=(os.path.join(path,f),results))
        t.start()
        t.join()

    lock_results.acquire()
    results.append(len(files))
    lock_results.release()


contador('../../', results)

print(sum(results))
    
