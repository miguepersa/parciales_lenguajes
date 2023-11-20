import pytest
from Manejador import *

def testCrearTipoAtomico():
    manejadorTipos = Manejador()
    manejadorTipos.crearTipoAtomico("char", 1, 2)
    tipoChar = manejadorTipos.tipos["char"]
    assert tipoChar.nombre == "char"
    assert tipoChar.representacion == 1
    assert tipoChar.alineacion == 2

def testCrearTipoRegistro():
    manejadorTipos = Manejador()
    manejadorTipos.crearTipoAtomico("int", 4, 4)
    manejadorTipos.crearTipoAtomico("char", 1, 2)
    manejadorTipos.crearTipoRegistro("foo", ["char", "int"])
    tipoFoo = manejadorTipos.tipos["foo"]
    assert tipoFoo.nombre == "foo"
    assert tipoFoo.campos == ["char", "int"]

def testCrearTipoRegistroVariante():
    manejadorTipos = Manejador()
    manejadorTipos.crearTipoAtomico("int", 4, 4)
    manejadorTipos.crearTipoAtomico("char", 1, 2)
    manejadorTipos.crearTipoRegistro("foo", ["char", "int"])
    manejadorTipos.crearTipoRegistroVariante("bar", ["int", "foo", "int"])
    tipoBar = manejadorTipos.tipos["bar"]
    assert tipoBar.nombre == "bar"
    assert tipoBar.campos == ["int", "foo", "int"]

def testDescribirTipoError():
    manejadorTipos = Manejador()

    # Capturar la salida estándar para verificar el mensaje de error
    import io
    import sys
    sys.stdout = io.StringIO()

    manejadorTipos.describirTipo("undefinedType")
    output = sys.stdout.getvalue()
    expectedOutput = "Error: El tipo 'undefinedType' no ha sido definido.\n"
    assert output == expectedOutput

    # Restaurar la salida estándar
    sys.stdout = sys.__stdout__

# Ejecutar las pruebas con Pytest
if __name__ == "__main__":
    pytest.main()
