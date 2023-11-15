from Arbol import *

def es_numero(string: str):
    """
    Comprueba si un string es un número entero o un número decimal.

    Args:
        string (str): String a evaluar.

    Retorna:
        bool: True si el string es un número entero o un número decimal, False en caso contrario.
    """
    return string.isnumeric() or string[1:].isnumeric()

def build_preorder(preorder):
    """
    Construye un árbol binario a partir de una lista de recorrido preorden.

    Args:
        preorder (list): La lista de recorrido preorden.

    Retorna:
        Arbol: El árbol binario construido.
    """

    if not preorder:
        return None

    operator = preorder.pop(0)
    root = Arbol(operator)

    if operator not in '+-*/':
        return root

    left_subtree = build_preorder(preorder)
    right_subtree = build_preorder(preorder)

    root.r = right_subtree
    root.l = left_subtree

    return root


def build_postorder(postorder):
    """
    Construye un árbol binario a partir de una lista de recorrido postorden.

    Args:
        postorder (list): La lista de recorrido postorden.

    Retorna:
        Arbol: El árbol binario construido.
    """

    stack = []

    for element in postorder:
        if es_numero(element):
            a = Arbol(element)
            stack.append(a)
        else:
            right_child = stack.pop()
            left_child = stack.pop()

            a = Arbol(element, left_child, right_child)

            stack.append(a)

    return stack.pop()


# Definición de las operaciones aritméticas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a // b


operadores = {
    '+' : suma,
    '-' : resta,
    '*' : multiplicacion,
    '/' : division
}

def evaluar(arbol: Arbol):
    """
    Evalúa el valor de una expresión aritmética representada por un árbol binario.

    Args:
        arbol (Arbol): El árbol binario que representa la expresión aritmética.

    Retorna:
        int: El valor de la expresión aritmética.
    """

    if es_numero(arbol.val):
        return int(arbol.val)

    op = operadores[arbol.val]
    return op(evaluar(arbol.l), evaluar(arbol.r))


def mostrar(arbol: Arbol):
    """
    Muestra la representación en string de un árbol binario.

    Args:
        arbol (Arbol): El árbol binario a representar.

    Retorna:
        str: La representación en string del árbol binario.
    """

    if es_numero(arbol.val):
        return arbol.val

    if es_numero(arbol.l.val) and es_numero(arbol.r.val):
        return f"({mostrar(arbol.l)} {arbol.val} {mostrar(arbol.r)})"

    return f"{mostrar(arbol.l)} {arbol.val} {mostrar(arbol.r)}"

def validar_expresion(string: str):
    '''
    Valida que la expresion sea solo de numeros u operadores binarios
    soportados por el programa (+, -, *, /) 


    Args:
        string (str): La expresion a ser evaluada

    Retorna:
        bool: La expresion es valida o no
    '''


    flag = sum(1 for i in string if i.isalnum()) -1 == sum(1 for i in string if i in "+-*/")
    
    return not any(i.isalpha() for i in string) and flag