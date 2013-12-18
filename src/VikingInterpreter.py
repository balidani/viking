#!/usr/bin/env python

__author__ = 'dada'

from VikingParser import VikingParser
from VikingStd import VikingStd
from VikingType import VikingType

class VikingInterpreter:
    'Handles the interpretation of viking code'

    def __init__(self, functions):
        self.functions = functions

    def match_pattern(self, pattern, args):
        'Match a pattern with the arguments'

        result = {}

        # Extract data
        pattern_type, pattern_data = pattern
        arg_type, arg_data = args

        if pattern_type != arg_type and pattern_type != VikingType.SYMBOL:
            return None

        # Check types
        if pattern_type == VikingType.EMPTY:
            if arg_type != VikingType.EMPTY:
                return None
        elif pattern_type == VikingType.PAIR:
            # Match pattern recursively

            pattern_head, pattern_tail = pattern_data
            arg_head, arg_tail = arg_data

            head_match = self.match_pattern(pattern_head, arg_head)
            tail_match = self.match_pattern(pattern_tail, arg_tail)

            if head_match is None:
                return None

            if tail_match is None:
                return None

            # Resolve symbols
            for symbol, value in head_match.iteritems():
                if symbol in tail_match:
                    if tail_match[symbol] != head_match[symbol]:
                        return None

            result.update(head_match)
            result.update(tail_match)

        elif pattern_type == VikingType.NUMBER:
            if arg_type != VikingType.NUMBER:
                return None
            if pattern_data != arg_data:
                return None
        elif pattern_type == VikingType.SYMBOL:
            result[pattern_data] = args

        return result

    def interpret_expression(self, expression, symbols):
        'Interpret an expression with a given symbol dictionary'

        exp_type, exp_data = expression

        if exp_type == VikingType.EMPTY:
            return (VikingType.EMPTY, ())
        elif exp_type == VikingType.PAIR:
            head, tail = exp_data
            head_value = self.interpret_expression(head, symbols)
            tail_value = self.interpret_expression(tail, symbols)

            return (VikingType.PAIR, (head_value, tail_value))
        elif exp_type == VikingType.NUMBER:
            return (VikingType.NUMBER, exp_data)
        elif exp_type == VikingType.SYMBOL:

            # Return function pointer
            if exp_data in self.std.functions:
                return expression

            if expression in self.functions:
                return expression

            if exp_data not in symbols:
                raise Exception('Unknown symbol \'%s\'' % exp_data)

            if exp_data == symbols[exp_data]:
                raise Exception('Symbol resolves to itself')

            return self.interpret_expression(symbols[exp_data], symbols)
        elif exp_type == VikingType.FUNCTION_CALL:
            # Unpacking function parameters
            function, args = exp_data
            function_type, function_name = function

            # Evaluate arguments
            interpreted_args = self.interpret_expression(args, symbols)

            # Check for symbols
            if function_name in symbols:
                function = symbols[function_name]
                function_type, function_name = function

            if function not in self.functions:
                if function_name not in self.std.functions:
                    raise Exception('Unknown function called \'%s\'' % function_name)
                else:
                    std_function = self.std.functions[function_name]
                    return std_function(interpreted_args)

            return self.interpret_function(self.functions[function], interpreted_args)

    def interpret_function(self, function, args):
        'Interpret a single function'

        # Match the pattern
        match, expression = None, None
        for part_candidate in function:
            symbol, pattern, expression = part_candidate

            match_candidate = self.match_pattern(pattern, args)
            if match_candidate is not None:
                match = match_candidate
                break

        if match is None:
            print args
            raise Exception('No matching pattern found for function \'%s\'' % function[0][0][1])

        # Use the match to interpret the expression
        return self.interpret_expression(expression, match)

    def pretty_print(self, expression):
        'Convert an expression to a more readable format'

        exp_type, exp_value = expression

        if exp_type == VikingType.EMPTY:
            return ()
        elif exp_type == VikingType.PAIR:
            head, tail = exp_value

            pretty_head = self.pretty_print(head)
            pretty_tail = self.pretty_print(tail)

            return (pretty_head, pretty_tail)
        else:
            return exp_value

    def parse_args(self, args):

        def parse_arg_list(args):
            if args == []:
                return (VikingType.EMPTY, ())

            arg_exp = self.interpret_expression(args[0], {})
            return (VikingType.PAIR, (arg_exp, parse_arg_list(args[1:])))

        parsed_args = []
        vp = VikingParser()

        for arg in args:
            parsed_args.append(vp.parse_expression(arg))

        if len(parsed_args) == 0:
            return ((VikingType.NUMBER, 0), (VikingType.EMPTY, ()))

        return ((VikingType.NUMBER, len(parsed_args)), parse_arg_list(parsed_args))

    def interpret_program(self, args):
        'Interpret all of the program starting from the main function'

        # Check the existence of main
        if (VikingType.SYMBOL, 'main') not in self.functions:
            raise Exception('Main function not found')

        # Load standard viking library
        self.std = VikingStd()

        # Parse arguments
        (argc, argv) = self.parse_args(args[2:])

        main = self.functions[(VikingType.SYMBOL, 'main')]
        args = (VikingType.PAIR, (argc, argv))

        result = self.interpret_function(main, args)

        # Convert a result to a more readable 'canonical' form
        return self.pretty_print(result)