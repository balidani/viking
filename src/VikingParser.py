#!/usr/bin/env python

__author__ = 'dada'

from VikingType import VikingType

def enum(**enums):
    return type('Enum', (), enums)

class VikingParser:
    'Handles the parsing of viking code'

    def __init__(self):

        self.functions = {}
        self.digits = map(str, range(10))
        self.special = "=(),#"
        self.newline = "\n"
        self.whitespace = " \t\n"

    def tokenize(self, line):
        'Find the next token from a line of the source'

        # Count the parentheses for balance
        paren_count = 0

        current_token = ''
        for char in line:
            if char in self.whitespace:
                if current_token != '':
                    if paren_count == 0:
                        yield current_token
                        current_token = ''
                    else:
                        current_token += char
                continue

            if char == '(':
                paren_count += 1
            elif char == ')':
                paren_count -= 1

                if paren_count < 0:
                    raise Exception('Unbalanced parentheses')

            current_token += char

        if current_token != '':
            yield current_token

    def try_parsing(self, token, *functions):
        'Tries to parse an item using a list of parser functions'

        for fun in functions:
            try:
                return fun(token)
            except Exception:
                pass

        raise Exception('Unrecognised expression \'%s\'' % token)

    def parse_expression(self, token):
        'Parse an expression'

        result = self.try_parsing(
            token,
            self.parse_empty,
            self.parse_pair,
            self.parse_number,
            self.parse_symbol,
            self.parse_function_call)

        return result


    def parse_empty(self, token):
        'Parse the `empty` type'

        if token != '()':
            raise Exception('Syntax error: expected ()')

        return (VikingType.EMPTY, ())

    def parse_pair(self, token):
        'Parse a pair'

        from string import strip

        # Check parentheses
        if not token.startswith('('):
            raise Exception('Pair must start with left parenthesis')

        if not token.endswith(')'):
            raise Exception('Pair must end with right parenthesis')

        # Remove parentheses
        token = token[1:-1]

        # Find comma index
        paren_count = 0
        comma_index = 0
        for char in token:
            if char == '(':
                paren_count += 1
            elif char == ')':
                paren_count -= 1
                if paren_count < 0:
                    raise Exception('Unbalanced parentheses')
            elif char == ',':
                if paren_count == 0:
                    break
            comma_index += 1

        # Check if comma index exists
        if comma_index < len(token):
            head = token[:comma_index]
            tail = token[comma_index + 1:]
        else:
            head = token
            tail = '()'

        pair = tuple(map(self.parse_expression, map(strip, [head, tail])))

        return (VikingType.PAIR, pair)

    def parse_number(self, token):

        # Each character has to be a digit
        for char in token:
            if char not in self.digits:
                raise Exception('Invalid number syntax')

        return (VikingType.NUMBER, int(token))

    def parse_symbol(self, token):

        # Disallow numbers at the beginning
        if token[0] in self.digits:
            raise Exception('Symbol may not start with a number')

        # Disallow special characters and whitespace
        for char in self.special + self.whitespace:
            if char in token:
                raise Exception('Illegal character in symbol name')

        return (VikingType.SYMBOL, token)

    def parse_function_call(self, token):

        # Split at the first space
        space = token.index(' ')

        symbol = self.parse_symbol(token[:space])
        pair = self.parse_expression(token[space + 1:])

        return (VikingType.FUNCTION_CALL, (symbol, pair))

    def parse_program(self, source):
        'Parse the entire source code of the program'

        # Process lines individually
        for line in source.split(self.newline):

            tokens = self.tokenize(line)

            try:
                # Parse symbol name
                token = tokens.next()

                # Ignore comments
                if token.startswith('#'):
                    continue

                symbol = self.parse_symbol(token)

                # Parse pattern
                token = tokens.next()

                pattern = self.parse_expression(token)

                # Parse equals sign
                try:
                    token = tokens.next()

                    if token != '=':
                        raise Exception('Expected \'=\'')

                except StopIteration:
                    raise Exception('Function with no body expression')

                # Parse body expression
                token = ''
                while True:
                    try:
                        token += tokens.next() + ' '
                    except StopIteration:
                        break

                token = token.strip()
                expression = self.parse_expression(token)

                if symbol not in self.functions:
                    self.functions[symbol] = []

                self.functions[symbol].append((symbol, pattern, expression))

            except StopIteration:
                continue

        return self.functions