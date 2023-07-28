from __future__ import annotations
from typing import List, Union
from .lexer import Token

class ASTNode:
    """Stores a value and children
    """

    def __init__(self, name=Union[Token, str]):
        self.name = name
        self.children: List[Union[Token, ASTNode]] = list()

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.name}: ({','.join(str(child) for child in self.children)})"

    def __eq__(self, __value: object) -> bool:
        return self.name == str(__value)

    def add_children(self, *children: Union[Token, ASTNode]):
        """Adds children to the end of the children's list
        """
        for child in children:
            self.children.append(child)
