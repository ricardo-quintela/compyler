from dataclasses import dataclass
from typing import List, Union

from .lexer import Token

class Node:
    """Stores a value and children
    """

    def __init__(self, value=Union[Token, str]):
        self.value = value
        self.children: List[Token] = list()


    def add_children(self, *children):
        """Adds children to the end of the children's list
        """
        for child in children:
            self.children.append(child)


@dataclass
class AST:
    """An abstract syntax tree stores the tokens into a parenting relation
    """
    root: Node
