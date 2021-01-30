from enum import Enum
from dataclasses import dataclass

# Tokenizer's Token DataClass
class TokenType(Enum): 
    NUMBER = 0
    LPAREN = 1
    RPAREN = 2
    PLUS = 3
    MINUS = 4
    MULTIPLY = 5
    DIVIDE = 6
    EXPONENT = 7

@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self): 
        return self.type.name + (f":{self.value}" if self.value != None else "")


# Tokenizer 
WHITESPACE = ' \n\t'
DIGITS = '0123456789'

class Tokenizer:
    def __init__(self, text): 
        # Iteration of text
        self.text = iter(text)
        self.advance()

    # Advance to next character if avail
    def advance(self): 
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None
     
    def generate_tokens(self): 
        while self.current_char != None:
            # Ignore whitespaces
            if self.current_char in WHITESPACE:
                self.advance()
            # Tokenize valid operands/operators
            elif self.current_char == '.' or self.current_char in DIGITS:
                # Handle numbers (many digits/decimal pts)
                yield self.generate_number()
            elif self.current_char == '+': 
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-': 
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*': 
                yield self.generate_asterisk()
            elif self.current_char == '/': 
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '(': 
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')': 
                self.advance()
                yield Token(TokenType.RPAREN)
            # Except all other characters
            else:
                print(self.current_char + ' is fucked up')
                raise Exception(f"Illegal character '{self.current_char}'")

    # Generates numbers from each character (digit/decimal)
    def generate_number(self): 
        # TO TEST: try ".0.2", does it work with 2 decimals, starting with dec?
        decimal_count = 0
        number_str = ''

        # While still digits/decimals
        while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS): 
            # No more than 1 decimal in number 
            if self.current_char == '.': 
                decimal_count += 1
                if decimal_count > 1:
                    break

            # Adds digits/decimals to number_str
            number_str += self.current_char
            self.advance()

        # Formats numbers starting with . appropriately (.12 -> 0.12)
        if number_str.startswith('.'):
            number_str = '0' + number_str

        # Formats numbers ending with . appropriately (12. -> 12)
        if number_str.endswith('.'):
            number_str += '0'

        return Token(TokenType.NUMBER, float(number_str))

    # Generates either MULTIPLY or EXPONENT Token
    def generate_asterisk(self): 
        asterisk_count = 1
        self.advance()

        # Loop when still *
        while self.current_char != None and (self.current_char == '*'):
            asterisk_count += 1
            # Cannot have more than 2 * in a row, invalid expression 
            if asterisk_count > 2:
                break

            self.advance()

        # Return respective Tokens
        if asterisk_count == 1:
            return Token(TokenType.MULTIPLY)

        return Token(TokenType.EXPONENT)
