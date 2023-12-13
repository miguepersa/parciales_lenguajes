#ifndef GRAFO_HPP
#define GRAFO_HPP

#include <vector>

using namespace std;

class Grafo
{
private:
    vector<vector<int>> adyacencias;
    int nodos;
public:
    Grafo(int nodos);
    ~Grafo();

    vector<vector<int>> get_adyacencias();
    bool is_ady(int, int);
    void add_edge(int, int);
    int get_nodos();
};


#endif