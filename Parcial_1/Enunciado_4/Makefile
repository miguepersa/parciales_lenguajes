OBJ= Vector3D.o main.o
CC= g++
CFLAGS= -Wall

all: $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o vector3

main.o: main.cpp
	$(CC) -c $(CFLAGS) $< -o $@

Vector3D.o: Vector3D.cpp
	$(CC) -c $(CFLAGS) $< -o $@

clean:
	rm -rf *.o vector3