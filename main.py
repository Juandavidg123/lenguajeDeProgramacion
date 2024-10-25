from mips.mips import MIPSCodeGenerator
from mips.lexer import tokenize
from mips.parser import Parser
from mips.interpreter import Interpreter


def main():
    def leer_archivo_txt(ruta_archivo):
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                return contenido
        except FileNotFoundError:
            print(f"El archivo {ruta_archivo} no se encontró.")
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")

    ruta = './comando.txt'
    contenido = leer_archivo_txt(ruta)
    if contenido:
        pipeline = contenido.split('\n')
        print(f"Código a interpretar: {pipeline}")
        for code in pipeline:

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
