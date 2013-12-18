# fibonacci.v -- calculating the fibonacci sequence

# fib n: calculates the nth fibonacci number
fib 0 = 1
fib 1 = 1
fib n = + (fib - (n, 1), fib - (n, 2))

main (argc, argv) = fib 12