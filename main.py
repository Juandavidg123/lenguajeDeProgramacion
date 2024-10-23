from mips.mips import MIPSCodeGenerator
from mips.lexer import tokenize
from mips.parser import Parser
from mips.interpreter import Interpreter

def main():
    code = input()  

    tokens_list = tokenize(code)
    print("Tokens:", tokens_list)

    parser_instance = Parser(tokens_list)
    ast = parser_instance.parse_operation()
    print("AST:", ast)

    interpreter_instance = Interpreter()
    result = interpreter_instance.visit(ast)
    print("Resultado de la interpretación:", result)

    codegen = MIPSCodeGenerator()
    codegen.generate(ast)
    mips_code = codegen.get_code()
    print("Código MIPS generado:")
    print(mips_code)

if __name__ == '__main__':
    main()
