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

    def pow(self, args):
        def op(a, b):
            return a ** b
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

    def left_shift(self, args):
        def op(a, b):
            return a << b
        return self.arithmetic(op, args)

    def right_shift(self, args):
        def op(a, b):
            return a >> b
        return self.arithmetic(op, args)

    def lt(self, args):
        def op(a, b):
            return int (a < b)
        return self.arithmetic(op, args)

    def lte(self, args):
        def op(a, b):
            return int (a <= b)
        return self.arithmetic(op, args)

    def gt(self, args):
        def op(a, b):
            return int (a > b)
        return self.arithmetic(op, args)

    def gte(self, args):
        def op(a, b):
            return int (a >= b)
        return self.arithmetic(op, args)

    def eq(self, args):
        def op(a, b):
            return int (a == b)
        return self.arithmetic(op, args)

    def neq(self, args):
        def op(a, b):
            return int (a != b)
        return self.arithmetic(op, args)

    def boolean_not(self, args):
        def op(a, b):
            return int (not a)
        return self.arithmetic(op, args)

    def boolean_and(self, args):
        def op(a, b):
            return int (a and b)
        return self.arithmetic(op, args)

    def boolean_or(self, args):
        def op(a, b):
            return int (a or b)
        return self.arithmetic(op, args)

    def __init__(self):

        self.functions = {
            '+': self.add,
            '-': self.sub,
            '*': self.mul,
            '**': self.pow,
            '/': self.div,
            '^': self.bitwise_xor,
            '&': self.bitwise_and,
            '|': self.bitwise_or,
            '<<': self.left_shift,
            '>>': self.right_shift,
            '<': self.lt,
            '<=': self.lte,
            '>': self.gt,
            '>=': self.gte,
            '==': self.eq,
            '!=': self.neq,
            '!': self.boolean_not,
            '&&': self.boolean_and,
            '||': self.boolean_or
        }