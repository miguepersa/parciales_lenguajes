#include "Cola.hpp"

template <typename T> Cola<T>::Cola() : Secuencia()
{
}

template <typename T> Cola<T>::~Cola()
{
}

template <typename T> void Cola<T>::agregar(T elemento){
    elementos.push_back(elemento);
    n_elementos++;
}

template <typename T> T Cola<T>::remover(){
    if (n_elementos > 0){
        T elem = elementos[0];
        n_elementos--;
        elementos.erase(elementos.begin())
        return elem;
    }

    return (T)-1;
}
