#include "DFS.hpp"

DFS::DFS(Grafo* g): Busqueda(g)
{   
}

DFS::~DFS()
{
}

int DFS::buscar(int a, int v) {

    vector<bool> visitados(grafo->get_nodos(), false);
    Pila pila = Pila();
    pila.agregar(a);
    vector<vector<int>> ady = grafo->get_adyacencias();

    int recorridos = 0;

    while (!pila.vacio() && !visitados[v]) {

        int s = pila.remover();
        
        if (!visitados[s]){
            recorridos++;
            visitados[s] = true;
        }

        for (auto i = ady[s].begin(); i != ady[s].end(); i++) {

            if (!visitados[*i]) pila.agregar(*i);

        }

    }

    if (visitados[v]) return recorridos;
    else return -1;

}