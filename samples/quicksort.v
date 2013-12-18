# quicksort.v -- quicksort example

# . a: head of the pair a
. (a, as) = a

# ~ a: tail of the pair a
~ (a, as) = as

# ++ (a, b): concatenate lists a and b
++ (a, ()) = a
++ ((), b) = b
++ (a, b) = (. a, ++ (~ a, b))

# map ((f, v), a): for every item in a, collect f (a, v)
map ((f, p), ()) = ()
map ((f, p), (a, as)) = (f (a, p), map ((f, p), as))

# filter (a, f): only keep a[i] where f[i] is true
filter ((), a) = ()
filter (a, ()) = ()
filter ((a, as), (1, ts)) = (a, filter (as, ts))
filter ((a, as), (0, ts)) = filter (as, ts)

# lt (p, as): return the elements of as which are smaller than p
lt (p, as) = filter (as, map ((<, p), as))

# gt (p, a): return the elements of a which are greater than p
gt (p, as) = filter (as, map ((>, p), as))

# quicksort a: sorts the a list using quicksort
qs () = ()
qs (a, as) = ++ (qs lt (a, as), ++ ((a), qs gt (a, as)))

main (argc, argv) = qs (5, (2, (3, (9, (8, (7, (1, (4, (6, (10, (11, (13, (12, (14, (0)))))))))))))))