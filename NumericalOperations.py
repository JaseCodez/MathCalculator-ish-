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


if __name__ == '__main__':
    print(AddOp(MultOp(Constant(2), Constant(3)), Constant(5)).evaluate())
