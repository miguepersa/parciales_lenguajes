#ifndef DFS_HPP
#define DFS_HPP

#include "Busqueda.hpp"
#include "Pila.hpp"

using namespace std;

class DFS : public Busqueda
{
private:

public:
    DFS(Grafo*);
    ~DFS();
    int buscar(int, int);
};


#endif