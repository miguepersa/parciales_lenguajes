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
    io.write_string("Se rotará la palabra \"lenguaje\" 3 posiciones: ", !IO),
    Rotada1 = rotar("lenguaje", 3),
    io.write_string(Rotada1 ++ "\n", !IO),
    io.write_string("Se rotará la palabra \"telefono\" 5 posiciones: ", !IO),
    Rotada2 = rotar("telefono", 5),
    io.write_string(Rotada2 ++ "\n", !IO).