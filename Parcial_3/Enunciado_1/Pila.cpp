#include "Pila.hpp"

template <typename T> Pila<T>::Pila() : Secuencia()
{
}

template <typename T> Pila<T>::~Pila()
{
}

template <typename T> void Pila<T>::agregar(T elemento){
    elementos.push_back(elemento);
    n_elementos++;
}

template <typename T> T Pila<T>::remover(){
    if (n_elementos > 0){
        T out = elementos[n_elementos];
        elementos.pop_back();
        n_elementos--;
        return out;
    }

    cout << "Pila Vacia" << endl;
    return (T)-1;
}
