#include "Cola.hpp"

Cola::Cola() : Secuencia()
{
}

Cola::~Cola()
{
}

void Cola::agregar(int elemento){
    this->elementos.push_back(elemento);
    this->n_elementos++;
}

int Cola::remover(){
    if (this->n_elementos > 0){
        int elem = this->elementos[0];
        this->n_elementos--;
        this->elementos.erase(this->elementos.begin());
        return elem;
    }

    cout << "Pila Vacia" << endl;
    return (int)-1;
}
