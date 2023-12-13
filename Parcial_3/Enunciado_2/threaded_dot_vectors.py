from threading import Thread, Lock

lock = Lock()

def dot_product(vec1, vec2, index, results):
    """
    Calculates the dot product of two vectors.
    """
    result = 0
    for i in range(len(vec1)):
        result += vec1[i] * vec2[i]
    
    lock.acquire()
    results[index] = result
    lock.release()

def threaded_dot_product(vec1: list, vec2: list, n_threads = 1):
    """
    Calculates the dot product using two threads.
    """

    if len(vec1) != len(vec2):
        return "Error de dimensiones. |Vector1| !+ |Vector2|"

    threads = []

    results = [0 for i in range(n_threads)]

    if n_threads >= len(vec1):
        threads = [Thread(target=dot_product, args=(vec1[i:i+1], vec2[i:i+1], i, results)) for i in range(len(vec1))]
    
    else:
        if len(vec1) % n_threads == 0:
            threads = [Thread(target=dot_product, args=(vec1[i:i+n_threads], vec2[i:i+n_threads], i%n_threads, results)) for i in range(0, len(vec1), n_threads)]

        else:
            threads = [Thread(target=dot_product, args=(vec1[i:i+n_threads], vec2[i:i+n_threads], i%n_threads, results)) for i in range(0, len(vec1), n_threads)]
            threads.append(Thread(target=dot_product, args=(vec1[n_threads*len(threads):], vec2[n_threads*len(threads):], n_threads-1, results)))

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for the threads to finish
    for thread in threads:
        thread.join()

    # Combine the results
    return sum(results)

# Example usage
vec1 = [1, 2, 3]
vec2 = [4, 5, 6]

result = threaded_dot_product(vec1, vec2, 3)
print("Dot product:", result)
