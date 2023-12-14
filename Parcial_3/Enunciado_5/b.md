data Arbol a = Hoja | Rama a (Arbol a) (Arbol a)

foldA :: (a -> b -> b -> b) -> b -> Arbol a -> b
foldA f b Hoja = b
foldA f b (Rama value left right) = f value (foldA f b left) (foldA f b right)
