from BuddySystem import BuddySystem
import pytest

bs = BuddySystem(55)

# Test de reserva
def test_RESERVAR_0():
    assert bs.reservar('a', 1) == '\"a\" se alojo en el bloque (0, 0)'

def test_RESERVAR_1():
    assert bs.reservar('a', 1) == 'El nombre \"a\" ya esta reservado'

def test_RESERVAR_2():
    assert bs.reservar('b', 20) == 'No hay espacio disponible'

def test_RESERVAR_3():
    assert bs.reservar('c', 2) == '\"c\" se alojo en el bloque (2, 3)'
    
def test_RESERVAR_3():
    assert bs.reservar('d', 16) == '\"d\" se alojo en el bloque (16, 31)'

# Test de liberar

def test_LIBERAR_0():
    assert bs.liberar('invalido') == 'No existe bloque con nombre \"invalido\"'

def test_LIBERAR_1():
    assert bs.liberar('d') == 'Se libero el bloque \"d\"'

def test_LIBERAR_2():
    assert bs.liberar('a') == 'Se libero el bloque \"a\"'