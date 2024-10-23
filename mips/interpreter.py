class Interpreter:
    def visit(self, node):
        if node[0] == 'AREPA':
            left_value = int(self.visit(node[1]))  
            right_value = int(self.visit(node[2]))  
            return left_value + right_value
        elif node[0] == 'EMPANADA':
            left_value = int(self.visit(node[1]))  
            right_value = int(self.visit(node[2]))  
            return left_value - right_value
        elif node[0] == 'BUÑUELO':
            left_value = int(self.visit(node[1]))  
            right_value = int(self.visit(node[2]))  
            return left_value * right_value
        elif node[0] == 'NATILLA':
            left_value = int(self.visit(node[1])) 
            right_value = int(self.visit(node[2]))  
            return left_value / right_value
        elif node[0] == 'NUMBER':
            return int(node[1])  
        else:
            raise ValueError(f"Operador desconocido: {node[0]}")