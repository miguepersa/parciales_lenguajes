#include "Pila.hpp"

Pila::Pila() : Secuencia()
{
}

Pila::~Pila()
{
}

void Pila::agregar(int elemento){
    this->elementos.push_back(elemento);
    this->n_elementos++;
}

int Pila::remover(){
    if (this->n_elementos > 0){
        int out = this->elementos[this->n_elementos-1];
        this->elementos.pop_back();
        this->n_elementos--;
        return out;
    }

    cout << "Pila Vacia" << endl;
    return -1;
}
