#ifndef SECUENCIA_HPP
#define SECUENCIA_HPP

#include <vector>
#include <iostream>

class Secuencia
{
protected:
    
    std::vector<int> elementos;
    int n_elementos;

public:
    Secuencia();
    ~Secuencia();

    virtual void agregar(int elemento) = 0;
    virtual int remover() = 0;
    bool vacio();

};


#endif