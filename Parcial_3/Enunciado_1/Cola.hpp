#ifndef COLA_HPP
#define COLA_HPP

#include "Secuencia.hpp"

template <typename T> class Cola: Secuencia<T>
{
private:
    /* data */
public:
    Cola(/* args */);
    ~Cola();

    void agregar(T elemento);
    T remover();
};

#endif