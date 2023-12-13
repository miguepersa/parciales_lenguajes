#include "Secuencia.hpp"

Secuencia::Secuencia() : n_elementos(0)
{
}

Secuencia::~Secuencia()
{
}

bool Secuencia::vacio(){
    return n_elementos == 0;
}