import re

# Tokenizador
tokens = [
    (r'[ \t\n]+', None),  # Ignorar espacios
    (r'\d+', 'NUMBER'),   # Números
    (r'[a-zA-Z_]\w*', 'IDENTIFIER'),  # Identificadores
    (r'ASIGNA', 'ASIGNA'),     # Operador de asignación
    (r'AREPA', 'AREPA'),    # Suma en español
    (r'EMPANADA', 'EMPANADA'),  # Resta en español
    (r'BUÑUELO', 'BUÑUELO'),  # Multiplicación en español
    (r'NATILLA', 'NATILLA'),  # División en español
    (r'CON', 'CON'),      # Simbolo para operaciones en español
]

def tokenize(code):
    pos = 0
    tokens_list = []
    while pos < len(code):
        match = None
        for token_expr in tokens:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(code, pos)
            if match:
                text = match.group(0)
                if tag:
                    tokens_list.append((tag, text))
                break
        if not match:
            raise SyntaxError(f'Error de sintaxis en el carácter: {code[pos]}')
        else:
            pos = match.end(0)
    return tokens_list
