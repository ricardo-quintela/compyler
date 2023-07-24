# pylint: skip-file

from typing import Callable
from compyler import Token, token

@token
class INT(Token):
    regex: str = r"0|[1-9][0-9]*"
    func: Callable = int

def test_lex():

    TOKENS = [INT]

    assert Token.lex("123 abc 456", TOKENS) == [INT(value=456, pos=(8, 10)), INT(value=123, pos=(0,2))]
