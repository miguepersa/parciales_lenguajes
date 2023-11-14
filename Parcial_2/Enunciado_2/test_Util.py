from Util import *
import pytest

def test_es_numero():
    assert es_numero("112") and es_numero("-52") and not es_numero("asd123") and not es_numero("+-*/") and es_numero("0")

def test_build_preorder():
    arbol = build_preorder(['+', '*', '+', '3', '4', '5', '7'])
    assert arbol.preorder() == "+ * + 3 4 5 7"

def test_build_postorder():
    arbol = build_postorder(['8', '3', '-', '8', '4', '4', '+', '*', '+'])
    assert arbol.postorder() == "8 3 - 8 4 4 + * +"

def test_eval():
    arbol1 = build_preorder(['+', '*', '+', '3', '4', '5', '7'])
    arbol2 = build_postorder(['8', '3', '-', '8', '4', '4', '+', '*', '+'])

    assert evaluar(arbol1) == 42 and evaluar(arbol2) == 69

def test_mostrar():
    arbol = build_preorder(['+', '*', '+', '3', '4', '5', '7'])
    assert mostrar(arbol) == "(3 + 4) * 5 + 7"


def test_validar_expresion():
    assert validar_expresion("+ * + 3 4 5 7") and validar_expresion("8 3 - 8 4 4 + * +") and not validar_expresion("1 1 1") and not validar_expresion("* 1 1 1") and not validar_expresion("+ * 1 1")
