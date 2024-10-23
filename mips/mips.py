class MIPSCodeGenerator:
    def __init__(self):
        self.instructions = []
        self.register_counter = 0
        self.variables = {}

    def new_register(self):
        reg = f"$t{self.register_counter}"
        self.register_counter = (self.register_counter + 1) % 10
        return reg

    def generate(self, node):
        if node[0] == 'NUMBER':
            reg = self.new_register()
            self.instructions.append(f"li {reg}, {node[1]}")
            return reg

        if node[0] == 'ASIGNA':
            var_name = node[1][1]
            reg = self.generate(node[2])
            self.variables[var_name] = reg
            return reg

        operator = node[0]
        reg1 = self.generate(node[1])
        reg2 = self.generate(node[2])
        result_reg = self.new_register()

        if operator == 'AREPA':
            self.instructions.append(f"add {result_reg}, {reg1}, {reg2}")
        elif operator == 'EMPANADA':
            self.instructions.append(f"sub {result_reg}, {reg1}, {reg2}")
        elif operator == 'BUÑUELO':
            self.instructions.append(f"mul {result_reg}, {reg1}, {reg2}")
        elif operator == 'NATILLA':
            self.instructions.append(f"div {reg1}, {reg2}")
            self.instructions.append(f"mflo {result_reg}")  

        return result_reg
    
    def get_code(self):
        code = ".text\n"
        for instr in self.instructions:
            code += instr + "\n"
        return code