#ifndef SECUENCIA_HPP
#define SECUENCIA_HPP

using namespace std;

#include <vector>
#include <iostream>

template <typename T> class Secuencia
{
protected:
    
    vector<T> elementos;
    int n_elementos;

public:
    Secuencia(/* args */);
    ~Secuencia();

    virtual void agregar(T elemento);
    virtual T remover();
    bool vacio();

};


#endif