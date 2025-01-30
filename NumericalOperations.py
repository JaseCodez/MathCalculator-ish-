import re


class Expr:
    def evaluate(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError


class Constant(Expr):
    n: int

    def __init__(self, n: int):
        self.n = n

    def evaluate(self):
        return self.n

    def __str__(self):
        return str(self.n)


class AddOp(Expr):
    a: Expr
    b: Expr

    def __init__(self, a: Expr, b: Expr):
        self.a = a
        self.b = b

    def evaluate(self):
        return self.a.evaluate() + self.b.evaluate()

    def __str__(self):
        return f'({self.a} + {self.b})'


class SubOp(Expr):
    a: Expr
    b: Expr

    def __init__(self, a: Expr, b: Expr):
        self.a = a
        self.b = b

    def evaluate(self):
        return self.a.evaluate() - self.b.evaluate()

    def __str__(self):
        return f'({self.a} - {self.b})'


class MultOp(Expr):
    a: Expr
    b: Expr

    def __init__(self, a: Expr, b: Expr):
        self.a = a
        self.b = b

    def evaluate(self):
        return self.a.evaluate() * self.b.evaluate()

    def __str__(self):
        return f'({self.a} * {self.b})'


class DivOp(Expr):
    a: Expr
    b: Expr

    def __init__(self, a: Expr, b: Expr):
        self.a = a
        self.b = b

    def evaluate(self):
        return self.a.evaluate() // self.b.evaluate()

    def __str__(self):
        return f'({self.a} / {self.b})'


class Token:
    type: str

    def __init__(self, type: str):
        self.type = type


# Parser
class LexicalAnalysis:
    s: str

    def __init__(self, s: str):
        self.s = s

    def generate_tokens(self) -> list[Token]:
        lst = []
        for ch in self.s:
            if ch in '+=/*':
                lst.append(Token('OP'))
            elif ch.isdigit():
                lst.append(Token('NUM'))
        return lst


class SyntacticAnalysis:
    pass


class Parse:
    s: str

    def __init__(self, s: str):
        self.s = s

    def parse(self) -> Expr:
        LexicalAnalysis(self.s)


if __name__ == '__main__':
    print(AddOp(MultOp(Constant(2), Constant(3)), Constant(5)).evaluate())
