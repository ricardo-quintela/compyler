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

    def __len__(self):
        return len(self.children)

    def __eq__(self, __value: object) -> bool:
        return self.name == str(__value)

    def __getitem__(self, __index):
        return self.children[__index]

    def add_children(self, *children: Union[Token, ASTNode]):
        """Adds children to the end of the children's list
        """
        for child in children:
            self.children.append(child)

    def __repr__(self):
        ast_string = f"{self.name}"
        for child in self.children:
            ast_string += f"\n..{str(child.__repr__())}"

        return ast_string
