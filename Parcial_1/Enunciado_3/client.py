import sys

from BuddySystem import BuddySystem

if len(sys.argv) != 2:
    print("Cantidad de memoria no especificada. Debe invocar el programa de la siguiente manera:")
    print("$ python client.py [CANTIDAD_DE_MEMORIA]")

else:
    try:
        bs = BuddySystem(int(sys.argv[1]))
        print("Sistema iniciado. Ingrese un comando")
        while(True):
            comando = input("SYS_BUDDY > ").split(' ')
            if len(comando) == 3 and comando[0].upper() == "RESERVAR":
                try:
                    print(bs.reservar(comando[2], int(comando[1])))
                
                except ValueError as ve:
                    print(f"Error en argumento: ingrese un numero entero positivo en la cantidad de memoria")

                except Exception as e:
                    print(f"Error en comando: {str(e)}")

            elif len(comando) == 2 and comando[0].upper() == "LIBERAR":
                print(bs.liberar(comando[1]))

            elif len(comando) == 1 and comando[0].upper() == "MOSTRAR":
                print(bs)

            elif len(comando) == 1 and comando[0].upper() == "SALIR":
                break

            else:
                print("Error de sintaxis.")
                print("Comandos:\n")
                print("\tRESERVAR <cantidad> <nombre>")
                print("\tLIBERAR <nombre>")
                print("\tMOSTRAR")
                print("\tSALIR")

    except Exception as e:
        print(f"error en argumentos: {str(e)}")
