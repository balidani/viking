#!/usr/bin/env python

__author__ = 'dada'

"viking.py -- Viking interpreter"

import argparse
import sys

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

    vp = VikingParser()
    functions = vp.parse_program(source)

    vi = VikingInterpreter(functions)
    result = vi.interpret_program(sys.argv)

    print result

if __name__ == '__main__':
    main()

