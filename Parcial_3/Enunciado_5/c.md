Orden de evaluación Normal:

1. `sospechosa arbolito (genA 1)`
2. `foldA whatTF (const Hoja) arbolito (genA 1)`
3. `foldA whatTF (const Hoja) (Rama 'a' (Rama 'b' Hoja (Rama 'c' Hoja Hoja) ) Hoja) (genA 1)`
4. `whatTF 'a' (foldA whatTF (const Hoja) (Rama 'b' Hoja (Rama 'c' Hoja Hoja ) ) ) (foldA whatTF (const Hoja) Hoja) (genA 1)`
5. `whatTF 'a' (foldA whatTF (const Hoja) (Rama 'b' Hoja (Rama 'c' Hoja Hoja) ) ) (foldA whatTF (const Hoja) Hoja) (Rama 1 (genA (1 + 1)) (genA (1 * 2)) )`
6. `Rama ('a', 1) ((foldA whatTF (const Hoja) (Rama 'b' Hoja (Rama 'c' Hoja Hoja) ) ) (genA (1 + 1)) ) ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)) )`
7. `Rama ('a', 1) (whatTF 'b' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)) (genA (1 + 1))) ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2))) `
8. `Rama y Rama ('a', 1) (whatTF 'b' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)) (Rama 2 (genA (2 + 1)) (genA (2 * 2)) ) ) ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))`
9. `Rama ('a', 1) (Rama ('b', 2) ((foldA whatTF (const Hoja) Hoja) (genA (2 + 1))) (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja) (genA (2 * 2))) ) ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))`
10. `Rama ('a', 1) (Rama ('b', 2) ((const Hoja) (genA (2 + 1))) (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja) (genA (2 * 2))) ) ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))`
11. `Rama ('a', 1) (Rama ('b', 2) Hoja (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja) (genA (2 * 2))) ) ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))`
12. `Rama ('a', 1) (Rama ('b', 2) Hoja (whatTF 'c' (foldA whatTF (const Hoja) Hoja)(foldA whatTF (const Hoja) Hoja) (genA (2 * 2))) ) ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))`
13. `Rama ('a', 1) (Rama ('b', 2) Hoja (whatTF 'c' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) Hoja) (Rama 4 (genA(4+1)) (genA(4*2)) ) ) ) ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))`
14. `Rama ('a', 1) (Rama ('b', 2) Hoja ( Rama ('c', 4) ((foldA whatTF (const Hoja) Hoja) (genA(4+1))) ((foldA whatTF (const Hoja) Hoja) (genA(4*2))) ) ) ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))`
15. `Rama ('a', 1) (Rama ('b', 2) Hoja ( Rama ('c', 4) ((const Hoja) (genA(4+1))) ((foldA whatTF (const Hoja) Hoja) (genA(4*2))) ) ) ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))`
16. `Rama ('a', 1) (Rama ('b', 2) Hoja ( Rama ('c', 4) Hoja ((foldA whatTF (const Hoja) Hoja) (genA(4*2))) ) ) ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2))) Evaluamos el primer foldA`
17. `Rama ('a', 1) (Rama ('b', 2) Hoja ( Rama ('c', 4) Hoja ((const Hoja) (genA(4*2)) ) ) ) ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))`
18. `Rama ('a', 1) (Rama ('b', 2) Hoja ( Rama ('c', 4) Hoja Hoja ) ) ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))`
19. `Rama ('a', 1) (Rama ('b', 2) Hoja ( Rama ('c', 4) Hoja Hoja ) ) ((const Hoja) (genA (1 * 2)))`
20. `Rama ('a', 1) (Rama ('b', 2) Hoja ( Rama ('c', 4) Hoja Hoja ) ) Hoja`

Resultado:
Rama ('a', 1) (Rama ('b', 2) Hoja (Rama ('c', 4) Hoja Hoja)) Hoja

Orden de evaluación Aplicativo:

1. `sospechosa arbolito (genA 1)`
2. `sospechosa arbolito Rama 1 (genA (2)) (genA (2))`
3. `sospechosa arbolito Rama 1 (Rama 2 (genA (3)) (genA (4))) (genA (2)) `
4. `sospechosa arbolito Rama 1 (Rama 2 (genA (3)) (genA (4))) (Rama 2 (genA (3)) (genA (4)))`
5. `sospechosa arbolito Rama 1 (Rama 2 (genA (3)) (genA (4)) ) (Rama 2 (genA (3)) (genA (4)))`
6. `sospechosa arbolito Rama 1 (Rama 2 (Rama 3 (genA (4)) (genA (6))) (genA (4)) ) (Rama 2 (genA (3)) (genA (4)))`
7. `sospechosa arbolito Rama 1 (Rama 2 (Rama 3 (genA (4)) (genA (6))) (Rama 3 (genA (4)) (genA (6)))) (Rama 2 (genA (3)) (genA (4)))`

Evaluación recursiva infinita por genA, se detiene la corrida.