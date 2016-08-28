f 0 = 1
f 1 = 1
f 2 = 2
f nn =
  if nn `mod` 2 == 0
    then f n + f (n + 1) + n
    else f (n - 1) + f n + 1
  where n = nn `div` 2

l = map f [1..]
le = map f [0,2..]
lo = map f [1,3..]
