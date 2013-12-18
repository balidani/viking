
 ____________________________________________________________________________ 
|                                                                            |
|            viking - a purely functional programming language     __4___    |
|__________________________________________________________________\     \___|
                                                               <'\ /_ _ _/    
                "viking is not a rip-off of Erlang at all"      ((____!___/)  
                                        - no one ever            \0\0\0\0\/   
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Grammar
=======

    program = { fun };
    
    fun = { symbol, { whitespace }, pattern, { whitespace }, '=', 
        { whitespace }, exp, newline };
    exp = empty | pair | number | function call | symbol;

    function call = symbol, { whitespace }, expression

    pattern = expression;
    
    pair = '(', exp, ',', { whitespace }, exp, ')' | '(', exp, ')';
    empty = '()';

    number = { digit };
    digit = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9';

    symbol = ( all characters - digit - special ), 
        { all characters - special };
    special = '=' | '(' | ')' | ',' | '#' | whitespace;
    
    newline = '\n';
    whitespace = ' ' | '\t' | newline;
    all characters = ? all ASCII characters ?;

Syntax
======

The grammar specifies the syntax almost completely. There are a few reserved 
special characters that cannot be used in symbol names: '=', '(', ')', ',', 
'#' and whitespace. The hashmark is reserved for comments.

Any line where the first non-whitespace character is the hashmark is considered 
a comment, and is not interpreted as part of the program.

Program
=======

Each program consists of a list of functions. One special function is `main`. 
`main` is called by the interpreter, with the arguments supplied by the user. 

    main (argc, argv) = << some expression >>

Similarly to many programming languages, `argc` is the number of arguments 
and `argv` is the list of arguments.

Functions
=========

Every function takes a pattern as it's argument. If the pattern matches the 
arguments that the function received, it evaluates the expression in its body
and returns the result. The following example illustrates this:

    fib 0 = 1
    fib 1 = 1
    fib n = + (fib (- (n, 1)), fib (- (n, 2)))

For a given argument, every pattern is checked, until one is successfully 
matched. At that point the pattern matching terminates, and the function 
evaluates the expression in its body. If every pattern fails, the program 
will exit with an error message.

Functions are represented by a unique symbol. This symbol can also be used as
a function pointer. A good example of this is `map`, which calls a function on
each element of a list, and returns the results in a new list:

    map (f, ()) = ()
    map (f, (a, as)) = (f a, map (f, as))

Every function call in viking is in prefix order.

Expressions
===========

The goal of each expression is to emit a single value after it is processed. 
The result of an expression can be a number, a pair, the empty pair or a 
function (as a symbol).

Pattern matching
================

Pattern matching is a key part of viking. Patterns are matched recursively 
until the pattern matching is finished, or it fails at some point. If an 
unknown symbol is found in the pattern, it will be matched with whatever is in 
the suplied argument. At the end of the pattern matching process, we get a list 
of symbols and their values. These symbols are then replaced by their values 
inside the body of the function. If there is a conflict with the symbols, the 
pattern matching fails.

Some examples, where the left arrow represents the arguments that were passed, 
and the right arrow shows the results of pattern matching (these are not 
language elements)

    fun0 n <- 42
        n -> 42

    fun1 (a, b) <- (3, 4)
        a -> 3
        b -> 4

    fun2 (a, a) <- (3, 4)
        a --> Error

    fun3 ((a, as), f) <- ((1, (2, (3, ()))), map)
        a -> 1
        b -> (2, (3, ()))
        f -> map (Must exist in the current context)

Pairs
=====

Pairs are a structure to encapsulate two values. Using these, we can implement 
any complex data-structure we want.

There are two very useful functions to access the members of a pair. These are 
also called the head and tail functions.
    
    . (a, b) = a
    ~ (a, b) = b

Lists can be implemented with pairs

    [1, 2, 3] = 
        (1, (2, (3, ()))), or (1, (2, (3)))

Dictionaries can also be implemented with pairs

    {1: 1, 2: 4, 3: 9} =
        ((1, 1), ((2, 4), ((3, 9))))

Arithmetic
==========

There are a couple of built-in arithmetic functions in viking
    
    +    addition
    -    subtraction
    *    multiplication
    **   exponentiation
    /    integer division
    %    modulo
    ^    bitwise xor
    &    bitwise and
    |    bitwise or
    >>   right arithmetic shift
    <<   left arithmetic shift

Boolean arithmetic
==================

viking doesn't have boolean values, instead it uses 1 for true and 0 for false.

The following comparison operators are built-in:

    <   less than
    >   greater than
    <=  less or equal
    >=  greater or equal
    ==  equal
    !=  not equal

The following logic operators are supported:

    !   logical negation
    &&  logical and
    ||  logical or


Quicksort example
=================

Helper function to merge lists

    # ++ (a, b): concatenate lists a and b
    ++ ((), b) = b
    ++ (a, ()) = a
    ++ (a, b) = (. a, ++ (~ a, b))

Helper functions to filter elements

    # map (a, (f, v)): for every item in a, collect f (a, v)
    map ((), _) = ()
    map ((a, as), (f, v)) = (f (a, v), map (as, (f, v)))

    # filter (a, f): only keep a[i] where f[i] is true
    filter (a, ()) = ()
    filter ((), f) = ()
    filter ((a, as), (0, fs)) = filter (as, fs)
    filter ((a, as), (1, fs)) = (a, filter (as, fs))

    # lt (p, as): return the elements of as which are smaller than p
    lt (p, as) = filter (as, map (as, (<, p)))

    # gt (p, a): return the elements of a which are greater than p
    gt (p, as) = filter (as, map (as, (>, p)))

Quicksort implementation

    qs (a, ()) = (a)
    qs (a, as) = ++ (qs lt (a, as), ++ (a, qs gt (a, as)))

Standard library
================

The standard viking library consists of the most important core functions. 
These functions are visible from every viking program.    

    .      (a, b)    head of a pair
    ~      (a, b)    tail of a pair
    ++     (a, b)    merging lists
    map    (f, a)    call f for every element of a
    filter (f, a)    keep every element of a, for which f(a) is true