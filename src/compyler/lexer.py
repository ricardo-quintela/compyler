"""Contains a class ready to register tokens
"""
import re
from dataclasses import dataclass
from typing import Any, Callable, Union, Tuple

# registers a class as a token
token = dataclass(frozen=True, repr=False)

@token
class Token:
    """Registers a token

    The token is composed of:
    - its name
    - the position on the text
    - its value
    - the regex that it obeys to
    - a function to convert the text to it's value

    The name is automaticly registered by the class name\n
    One must call Token.scan to scan the text for tokens

    Examples:
        ```
        @token
        class INT(Token):
            regex: str = r"[1-9][0-9]*"
            func: Callable = int
        ```
    """
    pos: Tuple[int, int]
    value: Any

    regex: str
    func: Callable = str

    def __repr__(self) -> str:
        return self.__class__.__name__

    def __str__(self) -> str:
        return self.__class__.__name__


    @staticmethod
    def lex(text: str, tokens: Union[list, tuple], ignore: list = []) -> list:
        """Scans an entire string for the existence of tokens
        and joins them, ordered, on a list

        Args:
            text (str): the string to scan for tokens
            tokens (list | tuple): a list or tuple containing the tokens

        Returns:
            list: a list of the ordered tokens on the text or None if an error is found
        """

        legal_tokens = [_token for _token in tokens if _token not in ignore]

        token_map = dict(
            zip(
                [_token.__name__ for _token in legal_tokens],
                legal_tokens
            )
        )

        token_regex = "|".join(f"(?P<{name}>{value.regex})" for name, value in token_map.items())

        buffer = list()

        for match in re.finditer(token_regex, text):
            buffer.insert(
                0,
                token_map[match.lastgroup](
                    pos=(match.start(), match.end() - 1),
                    value=token_map[match.lastgroup].func(match.group())
                )
            )

        return buffer


@token
class EOF(Token):
    """Represents the end-of-file character
    """
    pos: tuple = (-1, -1)
    value: None = None
    regex: str = r"\0"
    function: Callable = lambda _: None
