class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def consume(self, token_type):
        if self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            if token[0] == token_type:
                self.pos += 1
                return token
            else:
                raise SyntaxError(f'Se esperaba {token_type}, pero se encontró {token[0]}')
        else:
            raise SyntaxError('Se esperaban más tokens pero se llegó al final')

    def parse_operation(self):
        operation = self.consume('IDENTIFIER') 
        left = self.consume('NUMBER')  
        sintaxis = self.consume('IDENTIFIER')
        if sintaxis[1] != 'CON':
            raise SyntaxError('Se esperaba la palabra "CON"')
        right = self.consume('NUMBER')  

        return (operation[1], left, right) 