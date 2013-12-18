# fibonacci.v -- calculating the fibonacci sequence

# . a: returns the head of the pair a
#      later this will be moved to the standard library
. (a, as) = a

# fib n: calculates the nth fibonacci number
fib 0 = 1
fib 1 = 1
fib n = + (fib - (n, 1), fib - (n, 2))

main (argc, argv) = fib . argv