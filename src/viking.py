#!/usr/bin/env python

__author__ = 'dada'

"viking.py -- Viking interpreter"

import argparse
import sys
import time

from VikingInterpreter import VikingInterpreter
from VikingParser import VikingParser

def main():

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('args', nargs='*')

    args = vars(parser.parse_args())

    with open(args['source'], 'rb') as fp:
        source = fp.read()
        source = source.replace('\r', '')

    start_time = time.time()

    vp = VikingParser()
    functions = vp.parse_program(source)

    print "# Code parsed in %0.4f s" % (time.time() - start_time)

    start_time = time.time()

    vi = VikingInterpreter(functions)
    result = vi.interpret_program(sys.argv)

    print "# Code interpreted in %0.4f s" % (time.time() - start_time)

    print result

if __name__ == '__main__':
    main()

