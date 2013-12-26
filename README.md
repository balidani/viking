viking
======

viking is a purely functional programming language, not intended for serious use. This is only a hobby project for me. This sample implementation was done with python 2.7. It will probably be ported to both C and JavaScript later on, but first it has a *lot* to improve.

### Samples

The samples can be found in the [samples](samples/) directory. It is possible to run them with the following commands:

    $ python src/viking.py samples/fibonacci.v 6
    13
<!-- separator -->
    $ python src/viking.py samples/quicksort.v "(5, (3, (2, (7, (4, (1, (0, (6))))))))"
    (0, (1, (2, (3, (4, (5, (6, (7, ()))))))))

### Specification

For now, the [specification](specification.txt) will serve as the documentation for the language. Ideally, this will be changed later on for a proper documentation.

### TODO

The whole implementation has to be thrown away and remade. Possibly in C. The interpreter might have to be replaced by a compiler, which produces some form of byte-code. There could be a 'Viking Virtual Machine' to handle things.
