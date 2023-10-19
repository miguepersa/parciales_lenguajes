from Grafo import *
from Programa import Programa
from Interprete import Interprete
from Traductor import Traductor

programas = {} # Diccionario de programas con sus nombres { str : Programa }
interpretes = {} # Diccionario de interpretes con  de sus lenguajes { str : Interprete }
traductores = {} # Diccionario de traductores con  de sus lenguajes { str : Traductor }
lenguajes = ['LOCAL'] # Arreglo de lenguajes de la maquina

# Ciclo principal del programa
while True:
    entrada = input("$> ").split()
    
    # Manejo de la entrada por casos
    if entrada[0].upper() == 'DEFINIR':
        
        tipo = entrada[1]
        
        if tipo == "PROGRAMA": # Definicion de un programa
            nombre = entrada[2]
            lenguaje = entrada[3]
            if not lenguaje in lenguajes:
                lenguajes.append(lenguaje)

            if nombre not in programas:
                programas[nombre] = Programa(nombre, lenguaje)
                if lenguaje not in lenguajes:
                    lenguajes.append(lenguaje)
                print(f"Se definio el programa \'{nombre}\', ejecutable en en \'{lenguaje}\'.")
            else:
                print(f"Error: El programa {nombre} ya está definido.")

        elif tipo == "INTERPRETE": # Definicion de un interprete
            lenguaje_base = entrada[2]
            if lenguaje_base not in lenguajes:
                lenguajes.append(lenguaje_base)

            lenguaje = entrada[3]
            if lenguaje not in lenguajes:
                lenguajes.append(lenguaje)

            if not lenguaje in interpretes:
                interpretes[lenguaje] = [Interprete(lenguaje_base, lenguaje)]
            else:
                interpretes[lenguaje].append(Interprete(lenguaje_base, lenguaje) )
            print(f"Se definio un interprete para \'{lenguaje}\' escrito en \'{lenguaje_base}\'.")

        elif tipo == "TRADUCTOR": # Definicion de un traductor
            lenguaje_base = entrada[2]
            if lenguaje_base not in lenguajes:
                lenguajes.append(lenguaje_base)

            lenguaje_origen = entrada[3]
            if lenguaje_origen not in lenguajes:
                lenguajes.append(lenguaje_origen)

            lenguaje_destino = entrada[4]
            if lenguaje_destino not in lenguajes:
                lenguajes.append(lenguaje_destino)

            if lenguaje_origen in traductores:
                traductores[lenguaje_origen].append(Traductor(lenguaje_base, lenguaje_origen, lenguaje_destino))
            else:
                traductores[lenguaje_origen] = [Traductor(lenguaje_base, lenguaje_origen, lenguaje_destino)]
            print(f"Se definio un traductor de \'{lenguaje_origen}\' hacia \'{lenguaje_destino}\', escrito en \'{lenguaje_base}\'.")
        else:
            print("Error: Acción no válida.")

    elif entrada[0].upper() == 'EJECUTABLE': # Comprobacion de ejecutabilidad

        if entrada[1] in programas:

            # Creacion de vertices del grafo. Cada lenguaje es una vertice
            vertices = {lenguajes[i]: Vertice(lenguajes[i], i) for i in range(len(lenguajes))}
            
            # Creacion del grafo con las vertices creadas anteriormente
            g = Grafo(list(vertices.values()))
            
            # Arreglo auxiliar de traductores que no son agregados en un primer intento
            no_agregados = []

            for lenguaje in lenguajes:

                # Si hay un interprete de A escrito en B, entonces hay un lado A -> B
                if lenguaje in interpretes:
                    for interprete in interpretes[lenguaje]:
                        g.addLado(vertices[interprete.lenguaje], vertices[interprete.lenguaje_base])

                # Si hay un traductor de A a B escrito en C y C es ejecutable en la maquina,
                # se agrega un lado A -> B
                if lenguaje in traductores:
                    for traductor in traductores[lenguaje]:
                        if g.hayCamino(vertices[traductor.lenguaje_base]):
                            g.addLado(vertices[traductor.lenguaje_origen], vertices[traductor.lenguaje_destino])
                        else:
                            # Traductores no agregados se agregan a la lista
                            no_agregados.append(traductor)
                    
                # Se revisan los traductores que no fueron agregados por si requerian de un traductor
                # que fue agregado luego para funcionar.
                for traductor in no_agregados:
                    if g.hayCamino(vertices[traductor.lenguaje_base]):
                        g.addLado(vertices[traductor.lenguaje_origen], vertices[traductor.lenguaje_destino])
                        no_agregados.remove(traductor)

            # Si existe un camino de Programa.Lenguaje -> LOCAL, es ejecutable
            if g.hayCamino(vertices[programas[entrada[1]].lenguaje]):
                print(f"Si, es posible ejecutar el programa \'{entrada[1]}\'")

            else:
                print(f"No es posible ejecutar el programa \'{entrada[1]}\'")

        else:
            print(f"El programa {entrada[1]} no existe en la maquina.")


    elif entrada[0].upper() == 'SALIR':
        break

    else:
        print("Entrada invalida. Los comandos validos son:\n$> DEFINIR <tipo> [<argumentos>]\n$> EJECUTABLE <nombre>\n$> SALIR")