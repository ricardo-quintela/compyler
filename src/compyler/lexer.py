"""Contains a class ready to register tokens
"""
import re
from typing import List, Tuple, Callable


class Token:
    """Used to register a token
    A token contains a name and a regex that defines it

    Examples:
        ```
        >>> Token(name='INT', regex=r'[1-9][0-9]*')
        INT: '0|[1-9][0-9]*'
        ```
    """
    def __init__(self, name: str, regex: str) -> None:
        self.name: str = name
        self.regex: str = regex

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f"{self.name}: {self.regex}"


class Lexer:
    def __init__(self):
        self.tokens: List[Token] = list()

    def __len__(self):
        return len(self.tokens)

    def __contains__(self, _value) -> bool:
        for token in self.tokens:
            if token.name == _value:
                return True
        return False

    def __repr__(self) -> str:
        return f"Lexer with {len(self.tokens)} registered tokens"

    def add_token(self, name: str, regex: str):
        self.tokens.append(Token(name=name, regex=regex))

    def get_regex(self) -> str:
        return "|".join(f"(?P<{token.name}>{token.regex})" for token in self.tokens)

    def tokenize(self, text: str) -> List[Tuple[str]]:

        matches = re.finditer(self.get_regex(), text)

        tokenized_string = list()

        for match in matches:
            tokenized_string.append(
                (match.lastgroup, match.group())
            )

        return tokenized_string
