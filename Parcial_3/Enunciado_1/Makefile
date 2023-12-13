OBJ= Secuencia.o Pila.o Cola.o Grafo.o Busqueda.o BFS.o DFS.o main.o
CC= g++
CFLAGS= -Wall -g

all: $(OBJ)
	$(CC) $(OBJ) -o grafos_walk

BFS.o: BFS.cpp
	$(CC) $(CFLAGS) -c $< -o $@

Busqueda.o: Busqueda.cpp
	$(CC) $(CFLAGS) -c $< -o $@

Cola.o: Cola.cpp
	$(CC) $(CFLAGS) -c $< -o $@

DFS.o: DFS.cpp
	$(CC) $(CFLAGS) -c $< -o $@

Grafo.o: Grafo.cpp
	$(CC) $(CFLAGS) -c $< -o $@

Pila.o: Pila.cpp
	$(CC) $(CFLAGS) -c $< -o $@

Secuencia.o: Secuencia.cpp
	$(CC) $(CFLAGS) -c $< -o $@

main.o: main.cpp
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf *.o