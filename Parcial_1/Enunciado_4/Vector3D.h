#ifndef VECTOR3D_H
#define VECTOR3D_H

#include <cmath>
#include <iostream>
#include <string>

using namespace std;

class Vector3D
{
private:

    // Valores de las coordenadas
    int x;
    int y;
    int z;

public:
    Vector3D(); // Constructor de la clase por defecto
    Vector3D(int, int, int); // Constructor de la clase con argumentos de entrada
    ~Vector3D(); // Destructor de la clase por defecto
    
    // Getters y setters de los valores de las coordenadas
    void setX(int); 
    int getX();
    void setY(int);
    int getY();
    void setZ(int);
    int getZ();

    // Sobrecarga de operadores de la clase
    Vector3D operator+(Vector3D const &other); // Suma con otro vector
    Vector3D operator*(Vector3D const &); // Producto cruz
    Vector3D operator*(int); // Producto de un vector por un escalar
    Vector3D operator*(float e); // Producto de un vector por un escalar
    Vector3D operator+(int); // Suma de un vector con un escalar
    Vector3D operator+(float e); // Suma de un vector con un escalar
    Vector3D operator-(int); // Resta de un vector con un escalar
    Vector3D operator-(float e); // Resta de un vector con un escalar
    Vector3D operator-(Vector3D const &other); // Resta con otro vector
    int operator%(Vector3D const &other); // Producto punto con otro vector
    friend ostream & operator<<(ostream &s, Vector3D v); // Salida a stream
    friend Vector3D operator*(float e, Vector3D v); // Producto de un escalar con un vector
    friend float operator&(Vector3D); // Norma de un vector
};

#endif