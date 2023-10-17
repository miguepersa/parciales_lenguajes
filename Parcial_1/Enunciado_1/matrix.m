:- module matrix.
:- interface.
:- import_module io.
:- import_module list.
:- import_module int.

% Declaracion de la interfaz de las funciones y predicados
:- func producto_filas(list(int), list(int)) = int is det.
:- func multiply_row_with_matrix(list(int), list(list(int))) = list(int).
:- func by_transpose(list(list(int)), list(list(int))) = list(list(int)).
:- pred mult_matrix_transpose(list(list(int)), list(list(int))).
:- mode mult_matrix_transpose(in, out) is det.
:- pred main(io::di, io::uo) is det.
:- pred print_matrix(list(list(int))::in , io::di, io::uo) is det.

:- implementation.

% Funcion que calcula el producto de dos vectores
% Se utiliza para el calculo de cada termino de la matriz resultante
producto_filas([], []) = 0.
producto_filas([H1 | T1], [H2 | T2]) = H1 * H2 + producto_filas(T1, T2).
producto_filas([_ | T1], []) = producto_filas(T1, []).
producto_filas([], [_ | T2]) = producto_filas([], T2).

% Funcion que multiplica una fila por una matriz, dando como resultado
% un vector de elementos que componene la matriz resultante
multiply_row_with_matrix(_, []) = [].
multiply_row_with_matrix(Fila, [Columna | Columnas]) = [ producto_filas(Fila, Columna) | multiply_row_with_matrix(Fila, Columnas)].

% Funcion que calcula el producto de una matriz por su transpuesta
% y produce el resultado en un formato de listas de listas de enteros
by_transpose([], _) = [[]].
by_transpose([Head | Tail], Mat) = [multiply_row_with_matrix(Head, Mat) | by_transpose(Tail, Mat)].

% Predicado utilizado como interfaz 
% para calcular el producto de la matriz por su transpuesta
mult_matrix_transpose(M1, by_transpose(M1, M1)).

% Funcion que imprime la matriz en un formato legible
print_matrix([], !IO) :- 
    io.write_string("\n", !IO).
print_matrix([H | T], !IO) :- 
    (
        if H = [] then 
            io.write_string("\n", !IO)
        else
            io.write(H, !IO), 
            io.write_string("\n", !IO), 
            print_matrix(T, !IO)
    ).

% Punto inicial de ejecucion del programa
main(!IO) :-
    io.write_string("La matriz es:\n", !IO),
    Matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    print_matrix(Matrix1, !IO),
    mult_matrix_transpose(Matrix1, Res),
    io.write_string("El producto de la matriz por su transpuesta es:\n", !IO),
    print_matrix(Res, !IO).