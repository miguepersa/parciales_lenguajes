Evaluemos `misteriosa "abc" (gen 1)` paso a paso con orden de evaluacion normal:

1. `misteriosa "abc" (gen 1)`
2. `foldr what (const []) "abc" (gen 1)`
3. `what 'a' (foldr what (const []) "bc" (gen 1))`
4. `('a', '1') : (foldr what (const []) "bc" (gen 2))`
5. `('a', '1') : what 'b' (foldr what (const []) "c" (gen 2))`
6. `('a', '1') : ('b', '2') : (foldr what (const []) "c" (gen 3))`
7. `('a', '1') : ('b', '2') : what 'c' (foldr what (const []) [] (gen 3))`
8. `('a', '1') : ('b', '2') : ('c', '3') : foldr what (const []) [] (gen 4)`
9. `('a', '1') : ('b', '2') : ('c', '3') : []`

La expresión `misteriosa "abc" (gen 1)` se evalúa a `[('a', '1'), ('b', '2'), ('c', '3')]`.

1. `misteriosa "abc" (gen 1)`
2. `misteriosa "abc" (1 : gen 2)`
3. `misteriosa "abc" (1 : 2 : gen 3)`
4. `misteriosa "abc" (1 : 2 : 3 : gen 4)`
5. `misteriosa "abc" (1 : 2 : 3 : 4 : gen 5)`
6. `misteriosa "abc" (1 : 2 : 3 : 4 : 5 : gen 6)`

Se detiene la ejecucion pues Gen cae en recursion infinita.