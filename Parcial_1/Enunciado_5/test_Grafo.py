from Grafo import *
import pytest

def test_VERIFICAR_NUMERO_VERTICES():
    v = [Vertice(str(i), i) for i in range(5)]
    g = Grafo(v)
    assert(g.nvertices == len(v))

def test_AGREGAR_LADOS():
    v = [Vertice(str(i), i) for i in range(5)]
    g = Grafo(v)
    g.addLado(v[0], v[1])
    g.addLado(v[1], v[2])
    assert(g.hayCamino(v[0], '1') and g.hayCamino(v[1], '2'))

def test_VERIFICAR_CAMINO():
    v = [Vertice(str(i), i) for i in range(5)]
    g = Grafo(v)
    g.addLado(v[0], v[1])
    g.addLado(v[1], v[2])
    assert(g.hayCamino(v[0], '2'))

def test_VERIFICAR_NO_CAMINO():
    v = [Vertice(str(i), i) for i in range(5)]
    g = Grafo(v)
    g.addLado(v[0], v[1])
    g.addLado(v[1], v[2])
    assert(not g.hayCamino(v[0], '3'))

def test_VERIFICAR_NO_CAMINO_LARGO():
    v = [Vertice(str(i), i) for i in range(0,500)]
    g = Grafo(v)
    for i in range(len(v)-3):
        g.addLado(v[i], v[i+1])
    assert(not g.hayCamino(v[0], '499'))