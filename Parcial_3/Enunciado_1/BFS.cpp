#include "BFS.hpp"

BFS::BFS(Grafo* g): Busqueda(g)
{   
}

BFS::~BFS()
{
}

int BFS::buscar(int a, int v) {

    vector<bool> visitados(grafo->get_nodos(), false);
    Cola q = Cola();
    vector<vector<int>> ady = grafo->get_adyacencias();
    int s;
    int recorridos = 0;


    visitados[a] = true;
    q.agregar(a);

    while(!q.vacio() && !visitados[v]) {
        
        s = q.remover();
        recorridos++;

        for (size_t i = 0; i < ady[s].size(); i++) {
        
            if (!visitados[ady[s][i]]) {
                visitados[ady[s][i]] = true;
                q.agregar(ady[s][i]);
            }

        }
    }

    if (visitados[v]) return recorridos;
    else return -1;

}