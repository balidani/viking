#!/usr/bin/env python

__author__ = 'dada'

from VikingType import VikingType

class VikingStd:
    'The standard library for viking'


    def arithmetic(self, function, args):
        'Adds two numbers'

        # Unpacking the arguments
        pair_type, pair_data = args

        if pair_type != VikingType.PAIR:
            raise Exception('Arguments must be in a pair')

        # Unpacking pair values
        (head_type, head_data), (tail_type, tail_data) = pair_data

        if head_type != VikingType.NUMBER \
            or tail_type != VikingType.NUMBER:
            raise Exception('Arguments must be of number type')

        result = function(head_data, tail_data)

        # Pack results
        return (VikingType.NUMBER, result)

    def add(self, args):
        def op(a, b):
            return a + b
        return self.arithmetic(op, args)

    def sub(self, args):
        def op(a, b):
            return a - b
        return self.arithmetic(op, args)

    def mul(self, args):
        def op(a, b):
            return a * b
        return self.arithmetic(op, args)

    def div(self, args):
        def op(a, b):
            return a // b
        return self.arithmetic(op, args)

    def bitwise_xor(self, args):
        def op(a, b):
            return a ^ b
        return self.arithmetic(op, args)

    def bitwise_and(self, args):
        def op(a, b):
            return a & b
        return self.arithmetic(op, args)

    def bitwise_or(self, args):
        def op(a, b):
            return a | b
        return self.arithmetic(op, args)

    def lt(self, args):
        def op(a, b):
            return int (a < b)
        return self.arithmetic(op, args)

    def gt(self, args):
        def op(a, b):
            return int (a > b)
        return self.arithmetic(op, args)

    def nand(self, args):
        def op(a, b):
            return not (a and b)
        return self.arithmetic(op, args)

    def __init__(self):

        self.functions = {
            '+': self.add,
            '-': self.sub,
            '*': self.mul,
            '/': self.div,
            '^': self.bitwise_xor,
            '&': self.bitwise_and,
            '|': self.bitwise_or,
            '<': self.lt,
            '>': self.gt,
            '$': self.nand
        }