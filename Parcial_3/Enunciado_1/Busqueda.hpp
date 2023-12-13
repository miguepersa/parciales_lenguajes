#ifndef BUSQUEDA_HPP
#define BUSQUEDA_HPP

#include "Grafo.hpp"

using namespace std;

class Busqueda
{
protected:
    Grafo *grafo;
public:
    Busqueda(Grafo*);
    ~Busqueda();
    
    virtual int buscar(int, int) = 0;
};


#endif