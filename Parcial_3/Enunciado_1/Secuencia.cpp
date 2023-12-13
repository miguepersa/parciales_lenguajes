#include "Secuencia.hpp"

template <typename T> Secuencia<T>::Secuencia(/* args */) : n_elementos(0)
{
}

template <typename T> Secuencia<T>::~Secuencia()
{
}

template <typename T> bool Secuencia<T>::vacio(){
    return n_elementos == 0;
}