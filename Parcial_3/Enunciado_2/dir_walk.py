import os
from threading import Thread, Lock

lock_threads = Lock()
lock_results = Lock()

result = 0
threads = []

def contador(path='.'):
    print(path)
    if not os.path.isdir(path):
        raise Exception("la direccion dada no es un directorio")

    folders = []
    files = []

    for f in os.listdir(path):

        if os.path.isfile(f):
            files.append(f)
        else:
            folders.append(f)

    print(folders)
    print(files)

    # for f in folders:
    #     t = Thread(target=contador, args=(os.path.join(path,f),))
    #     lock_threads.acquire()
    #     threads.append(t)
    #     lock_threads.release()
    #     t.start()
    #     t.join()

    # lock_results.acquire()
    # result += len(files)
    # lock_results.release()


contador("../../Parcial_2/Enunciado_1/")

print(result)
    
