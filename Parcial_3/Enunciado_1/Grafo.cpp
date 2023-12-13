#include "Grafo.hpp"

Grafo::Grafo(int n)
{
    nodos = n;

    for (int i = 0; i < n; i++)
    {
        vector<int> v;
        adyacencias.push_back(v);
    }
    
}

Grafo::~Grafo()
{
}

vector<vector<int>> Grafo::get_adyacencias() {
    return adyacencias;
}

bool Grafo::is_ady(int a, int b) {

    if (a >= nodos || b >= nodos) return false;

    vector<int> ad = adyacencias[a];

    for (int i: ad) {
        if (i == b) {
            return true;
        }
    }

    return false;

}

void Grafo::add_edge(int a, int b) {

    if (!is_ady(a,b)){
        adyacencias[a].push_back(b);
    }

}

int Grafo::get_nodos() {
    return nodos;
}