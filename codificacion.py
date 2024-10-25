from mips.mips import MIPSCodeGenerator
from mips.lexer import tokenize
from mips.parser import Parser
from mips.interpreter import Interpreter


def codifcarCodigo(contenido):
    if contenido:
        pipeline = contenido.split('\n')
        codigoEjecutado = []
        errores = []
        try:
            for code in pipeline:
                lineaEjecutada = []
                tokens_list = tokenize(code)

                parser_instance = Parser(tokens_list)
                ast = parser_instance.parse_operation()

                interpreter_instance = Interpreter()
                result = interpreter_instance.visit(ast)

                codegen = MIPSCodeGenerator()
                codegen.generate(ast)
                mips_code = codegen.get_code()

                lineaEjecutada.append(tokens_list)
                lineaEjecutada.append(ast)
                lineaEjecutada.append(result)
                lineaEjecutada.append(mips_code)
                
                codigoEjecutado.append(lineaEjecutada)
            
        except Exception as e:
            errores.append(e)
        
        return codigoEjecutado, errores
        
    return [], ["No se generaron resultados."]