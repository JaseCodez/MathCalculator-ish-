# Abstract Syntax Tree
from __future__ import annotations
from typing import Union


class Expr:

    def solve(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError


class Constant(Expr):

    constant: Union[float, int]

    def __init__(self, constant: Union[float, int]):
        self.constant = constant

    def solve(self):
        return self.constant

    def __str__(self):
        return str(self.constant)


class Exponent(Expr):
    coefficient: int
    exponent: int

    def __init__(self, coefficient: Union[float, int], exponent: Union[float, int]):
        self.coefficient = coefficient
        self.exponent = exponent

    def solve(self):
        return self

    def __str__(self):
        return f'{self.coefficient}x^{self.exponent}'


class Operand(Expr):
    a: Expr
    b: Expr

    def __init__(self, a: Expr, b: Expr):
        self.a = a
        self.b = b

    def solve(self) -> Expr:
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError


class AddOp(Operand):

    def __int__(self, a: Expr, b: Expr):
        Operand.__init__(self, a, b)

    def solve(self) -> Expr:
        """
        >>> str(AddOp(Constant(1), Constant(2)).solve())
        '3'
        >>> str(AddOp(Constant(1), Exponent(2, 1)).solve())
        '(1 + 2x^1)'
        >>> str(AddOp(Exponent(2, 1), Exponent(2, 1)).solve())
        '4x^1'
        """
        if isinstance(self.a, Constant) and isinstance(self.b, Constant):
            return Constant(self.a.constant + self.b.constant)

        elif isinstance(self.a, Exponent) and isinstance(self.b, Exponent):
            if self.a.exponent == self.b.exponent:
                num = self.a.coefficient + self.b.coefficient
                return Exponent(num, self.a.exponent)

        return AddOp(self.a, self.b)

    def __str__(self):
        return f'({str(self.a)} + {str(self.b)})'


class SubOp(Operand):

    def __int__(self, a: Expr, b: Expr):
        Operand.__init__(self, a, b)

    def solve(self):
        if isinstance(self.a, Constant) and isinstance(self.b, Constant):
            return Constant(self.a.constant - self.b.constant)

        elif isinstance(self.a, Exponent) and isinstance(self.b, Exponent):
            if self.a.exponent == self.b.exponent:
                num = self.a.coefficient - self.b.coefficient
                return Exponent(num, self.a.exponent)

        return SubOp(self.a, self.b)


class MultOp(Operand):

    def __int__(self, a: Expr, b: Expr):
        Operand.__init__(self, a, b)

    def solve(self):
        if isinstance(self.a, Constant) and isinstance(self.b, Constant):
            return Constant(self.a.constant * self.b.constant)

        elif isinstance(self.a, Exponent) and isinstance(self.b, Exponent):
            num = self.a.coefficient * self.b.coefficient
            return Exponent(num, self.a.exponent + self.b.exponent)

        return MultOp(self.a, self.b)


class DivOp(Operand):

    def __int__(self, a: Expr, b: Expr):
        Operand.__init__(self, a, b)

    def solve(self):
        if isinstance(self.a, Constant) and isinstance(self.b, Constant):
            return Constant(self.a.constant / self.b.constant)
        elif isinstance(self.a, Exponent) and isinstance(self.b, Exponent):
            num = self.a.coefficient / self.b.coefficient
            return Exponent(num, self.a.exponent - self.b.exponent)

        return DivOp(self.a, self.b)


class Equation:
    lhs: Expr
    rhs: Expr

    def __init__(self, lhs: Expr, rhs: Expr):
        self.lhs = lhs
        self.rhs = rhs

    def solve(self) -> Equation:
        """
        >>> str(Equation(AddOp(Constant(1), Constant(2)), Exponent(1, 1)).solve())
        '3 = 1x^1'
        """
        return Equation(self.lhs.solve(), self.rhs.solve())

    def __str__(self):
        return f'{str(self.lhs)} = {str(self.rhs)}'

