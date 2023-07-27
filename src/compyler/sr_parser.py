"""Contains a class ready to register productions
and one to store expressions
"""
from dataclasses import dataclass
from typing import List, Union, Tuple

from .lexer import Token, EOF
from .parsing_ast import AST, Node

production = dataclass(frozen=True, repr=False)

class Expression:
    """Stores the combinations of tokens that compose a production

    Examples:
        ```
        >>> expression = Expression(
        ...     ["TOKEN1"],
        ...     ["TOKEN1", "TOKEN2"],
        ...     ["TOKEN1", "TOKEN3"]
        ... )
        ```
    """

    def __init__(self, *expression: List[str]) -> None:
        """Constructor of the class Expression\n
        One can pass multiple combinations of `str`
        """
        self.expression = expression

    def __contains__(self, other):
        return other in self.expression

    def __iter__(self):
        return iter(self.expression)

    def __repr__(self) -> str:
        return str(self.expression)


@production
class Production:
    """Composed of expressions\n

    One can call `Production.parse` to run the shift-reduce
    parser on a list of tokens gathered by a lexer\n
    The tokens can either be a registered `Token` or `str`

    Can be used to register other productions

    Examples:
        ```
        @production
        class Tuple(Production):
            expression = Expression(
                ["LPAR", "INT", "COMMA", "INT", "RPAR"]
            )
        ```
    """
    expression: Expression
    children: Tuple[int]

    def __repr__(self) -> str:
        return self.__class__.__name__


    @classmethod
    def try_reduce(cls, stack: List[Union[Token, str]]) -> bool:
        """Checks if a given stack contains items that
        can be reduced to the expression

        Args:
            stack (List[Token | str]): the stack of tokens

        Returns:
            bool: True if it can be reduced, False otherwise
        """
        for expression in cls.expression:

            for token, string in zip(stack[:len(expression)], expression):
                if str(token) != string:
                    break
            else:

                return len(expression)
        return -1

    @staticmethod
    def parse(tokens: List[Union[Token, str]], productions: list, root) -> bool:
        """Parses a list of tokens according to the
        given grammar of productions\n
        If the final token is not equal to the given root of the
        Abstract Syntax Tree returns False

        Args:
            tokens (List[Token | str]): a list of tokens
            productions (list): the registered productions
            root (Token): the root of the AST

        Returns:
            bool: True if the given tokens can be parsed, False otherwise
        """

        stack = [EOF()]

        for token in tokens:
            stack.insert(0, token)

            print("Current Stack ", stack)

            i = 0
            while i < len(productions):

                reduce_range = productions[i].try_reduce(stack)
                if reduce_range != -1:

                    # reduce the top of the stack
                    for _ in range(reduce_range):
                        stack.pop(0)
                    stack.insert(0, productions[i].__name__)
                    i = 0
                    continue
                i += 1

        return stack[0] == root.__name__
