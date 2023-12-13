#include <iostream>
#include "Grafo.hpp"
#include "DFS.hpp"
#include "BFS.hpp"

using namespace std;

int main(int argc, char const *argv[])
{

    Grafo g = Grafo(6);
    g.add_edge(0,1);
    g.add_edge(0,4);
    g.add_edge(1,4);
    g.add_edge(1,2);
    g.add_edge(4,3);
    g.add_edge(2,3);
    g.add_edge(3,5);

    BFS bfs = BFS(&g);
    DFS dfs = DFS(&g);

    cout << "BFS: " << bfs.buscar(1,5) << endl;
    cout << "DFS: " << dfs.buscar(1,5) << endl;

    return 0;
}
