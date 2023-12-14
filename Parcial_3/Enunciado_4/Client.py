from Manejador import *

if __name__ == "__main__":
    h = Manejador()

    while True:

        comando = input("$> ")
        c = comando.split(" ")
        if c[0].lower() == "class":
            if ":" in c and c[2] == ":":
                nombre = c[1]
                parent = c[3]
                metodos = c[4:]
                print(h.add_class(nombre, parent=parent, metodos=metodos))

            else:
                nombre = c[1]
                metodos = c[2:]
                print(h.add_class(nombre, metodos=metodos))

        elif c[0].lower() == "describir" and len(c) == 2:
            print(h.describe_class(c[1]))

        elif comando.lower() == "salir":
            break