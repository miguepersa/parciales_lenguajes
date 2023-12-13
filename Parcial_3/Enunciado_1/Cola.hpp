#ifndef COLA_HPP
#define COLA_HPP

#include "Secuencia.hpp"

using namespace std;

class Cola: public Secuencia
{
private:

public:
    Cola();
    ~Cola();

    void agregar(int elemento);
    int remover();
};

#endif