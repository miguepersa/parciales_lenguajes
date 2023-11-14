from Arbol import *
import pytest

def test_CREAR_0():
    arbol = Arbol(1, Arbol(2), Arbol(3))
    assert arbol.preorder() == "1 2 3"

def test_CREAR_1():
    arbol = Arbol(1, Arbol(2, Arbol(1)), Arbol(3, None, Arbol(2)))
    assert arbol.preorder() == "1 2 1 3 2"

def test_CREAR_2():
    arbol = Arbol(1, Arbol(2), Arbol(1, Arbol(2, Arbol(1)), Arbol(3, None, Arbol(2))))
    assert arbol.preorder() == "1 2 1 2 1 3 2"

def test_CREAR_3():
    arbol = Arbol(1, Arbol(2, Arbol(1)), Arbol(3, None, Arbol(2)))
    assert arbol.postorder() == "1 2 2 3 1"