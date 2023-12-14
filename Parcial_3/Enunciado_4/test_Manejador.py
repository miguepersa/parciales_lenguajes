import pytest
from Tipos import Tipo
from Manejador import Manejador

def test_tipo_str():
    tipo = Tipo("ClaseA")
    assert str(tipo) == "<class: 'ClaseA'>"

def test_manajador_add_class_success():
    manejador = Manejador()
    result = manejador.add_class("ClaseA")
    assert result == "Clase <class: 'ClaseA'> creada con exito"

def test_manajador_add_class_already_exists():
    manejador = Manejador()
    manejador.add_class("ClaseA")
    result = manejador.add_class("ClaseA")
    assert result == "Error: la clase ClaseA ya existe"

def test_manajador_add_class_parent_not_exists():
    manejador = Manejador()
    result = manejador.add_class("ClaseA", parent="ClaseB")
    assert result == "Error: la clase ClaseB no existe"

def test_manajador_add_class_duplicate_methods():
    manejador = Manejador()
    result = manejador.add_class("ClaseA", metodos=["metodo1", "metodo1"])
    assert result == "Error: metodos duplicados en la lista"

def test_manajador_describe_class_not_exists():
    manejador = Manejador()
    result = manejador.describe_class("ClaseA")
    assert result == "La clase ClaseA no existe"

def test_manajador_describe_class_empty_name():
    manejador = Manejador()
    result = manejador.describe_class("")
    assert result == "Debe proporcionar un nombre valido"

def test_manajador_describe_class_success():
    manejador = Manejador()
    manejador.add_class("ClaseA", metodos=["metodo1"])
    result = manejador.describe_class("ClaseA")
    assert result == "metodo1 -> ClaseA :: metodo1\n"
