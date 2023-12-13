#ifndef PILA_HPP
#define PILA_HPP

#include "Secuencia.hpp"

using namespace std;

class Pila: public Secuencia
{
private:

public:
    Pila();
    ~Pila();

    void agregar(int elemento);
    int remover();
};


#endif