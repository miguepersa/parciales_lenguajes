#ifndef BFS_HPP
#define BFS_HPP

#include "Busqueda.hpp"
#include "Secuencia.hpp"
#include "Cola.hpp"

using namespace std;

class BFS : public Busqueda
{
private:

public:
    BFS(Grafo*);
    ~BFS();
    int buscar(int, int);
};


#endif