#include "DFS.hpp"

DFS::DFS(Grafo* g): Busqueda(g)
{   
}

DFS::~DFS()
{
}

int DFS::buscar(int a, int v) {

    vector<bool> visitados;
    Pila<int> pila;
    pila.agregar(a);

    int recorridos = 0;

    while (!pila.vacio() && !visitados[v]) {

        int s = pila.remover();
        
        if (!visitados[s]) recorridos++;

    }

}