from Arbol import *
from Util import *

# Comandos validos del programa
comandos = {
    "MOSTRAR": mostrar,
    "EVAL": evaluar
}

# Tipos de expresiones admitidos en el programa
tipo_exp = {
    "PRE" : build_preorder,
    "POST" : build_postorder
}


# Ciclo principal del programa
while True:
    linea = input("> ")
    
    s_com = linea.split(" ")[0]
    
    if s_com.upper() == "SALIR":
        break
    
    s_build = linea.split(" ")[1]


    # Validacion de la entrada
    if not s_com.upper() in comandos.keys():
        print("Comando invalido.")
        continue

    if not s_build.upper() in tipo_exp.keys():
        print("Tipo de expresion invalida.")
        continue


    comando = comandos[s_com.upper()]
    build = tipo_exp[s_build.upper()]
    exp = linea[len(s_com)+len(s_build)+2:].split(" ")

    # Validacion de la expresion
    if validar_expresion(exp):
        print(comando(build(exp)))

    else:
        print("Expresion invalida.")