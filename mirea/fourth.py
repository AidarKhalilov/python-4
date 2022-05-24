class Num():
    def __init__(self, value):
        self.value = value

    def printSelf(self, visitor):
        return str(self.value)

    def calculateSelf(self, calculator):
        return self.value

    def stackSelf(self, stacker):
        stacker.operations_list.append("PUSH " + str(self.value))


class Operation():
    def __init__(self, left_arg, right_arg):
        self.left_arg = left_arg
        self.right_arg = right_arg
        self.operation_sign = ":)"
        self.operation_name = "kek"

    def printSelf(self, visitor):
        result_string = "("
        result_string += visitor.visit(self.left_arg)
        result_string += (" " + self.operation_sign + " ")
        result_string += visitor.visit(self.right_arg)
        result_string += ")"
        return result_string

    def stackSelf(self, stacker):
        stacker.visit(self.left_arg)
        stacker.visit(self.right_arg)
        stacker.operations_list.append(self.operation_name)


class Add(Operation):
    def __init__(self, left_arg, right_arg):
        super().__init__(left_arg, right_arg)
        self.operation_sign = "+"
        self.operation_name = "ADD"

    def calculateSelf(self, calculator):
        return self.left_arg.calculateSelf(calculator) + self.right_arg.calculateSelf(calculator)


class Mul(Operation):
    def __init__(self, left_arg, right_arg):
        super().__init__(left_arg, right_arg)
        self.operation_sign = "*"
        self.operation_name = "MUL"

    def calculateSelf(self, calculator):
        return self.left_arg.calculateSelf(calculator) * self.right_arg.calculateSelf(calculator)


class Sub(Operation):
    def __init__(self, left_arg, right_arg):
        super().__init__(left_arg, right_arg)
        self.operation_sign = "-"
        self.operation_name = "SUB"

    def calculateSelf(self, calculator):
        return self.left_arg.calculateSelf(calculator) - self.right_arg.calculateSelf(calculator)


class Div(Operation):
    def __init__(self, left_arg, right_arg):
        super().__init__(left_arg, right_arg)
        self.operation_sign = "/"
        self.operation_name = "DIV"

    def calculateSelf(self, calculator):
        return self.left_arg.calculateSelf(calculator) // self.right_arg.calculateSelf(calculator)


class PrintVisitor:
    def visit(self, tree):
        return tree.printSelf(self)


class CalcVisitor:
    def visit(self, tree):
        return tree.calculateSelf(self)


class StackVisitor:
    def __init__(self):
        self.operations_list = []

    def visit(self, tree):
        tree.stackSelf(self)

    def get_code(self):
        result = "\n".join(self.operations_list)
        self.operations_list = []
        return result


ast = Add(Num(7), Mul(Num(3), Num(2)))
pv = PrintVisitor()
cv = CalcVisitor()
sv = StackVisitor()
print(pv.visit(ast))
print(cv.visit(ast))
sv.visit(ast)
print(sv.get_code())