-- Dieses Haskell-Programm ist nur zur Veranschaulichung. Es zeigt ein ähnliches Prinzip,
-- wie die zweite rekursive Funktion des Python-Primzahltests

isPrime :: Integer -> Bool
isPrime x =
    x >= 2 &&
    isPrime' x 2 ||
    negate x >= 2 &&
    isPrime' (negate x) 2

isPrime' :: Integer -> Integer -> Bool
isPrime' x y =
    y * y >= succ x ||
    x `mod` y /= 0 &&
    isPrime' x (succ y)