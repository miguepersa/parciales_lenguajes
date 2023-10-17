:- module rotate.
:- interface.
:- import_module string.
:- import_module io.

% Declaracion de las interfaces del programa
:- func rotar(string, int) = string.
:- pred main(io::di, io::uo) is det.

:- implementation.
:- import_module int.
:- import_module int8.
:- import_module list.

rotar(String, Nrotar) = StringRotado :-
    ( if Nrotar = 0 ; Nrotar mod length(String) = 0 then StringRotado = String
    else 
        Len = length(String),
        StartIndex = Nrotar mod Len,
        Inicio = string.substring(String, StartIndex, Len),
        Final = string.substring(String, 0, StartIndex),
        append_string_pieces([Inicio, Final], AuxString),
        StringRotado = AuxString
    ).

    
main(!IO) :-
    io.write_string("Indique la palabra que quiere rotar: ", !IO),
    io.read_line_as_string(Res, !IO),
    (
        if Res = ok(Palabra) then
            io.write_string("Indique el numero de espacios a rotar: ", !IO),
            io.read_binary_int8(Rotar, !IO),
            (if Rotar = ok(Nrot) then
                Rotada = rotar(string.left(Palabra, length(Palabra)-1), int8.cast_to_int(Nrot) - 48),
                io.write_string(Rotada ++ "\n", !IO)

            else
                io.write_string("Entrada invalida\n", !IO)

            )
        else
        io.write_string("Error\n", !IO)
    ).
    