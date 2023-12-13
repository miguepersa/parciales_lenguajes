#ifndef PILA_HPP
#define PILA_HPP

#include "Secuencia.hpp"

using namespace std;

template <typename T> class Pila: public Secuencia<T>
{
private:
    /* data */
public:
    Pila(/* args */);
    ~Pila();

    void agregar(T elemento);
    T remover();
};


#endif