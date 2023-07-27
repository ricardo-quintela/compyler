# pylint: skip-file
import pytest
from compyler import Token, Lexer

@pytest.fixture
def int_token():
    return Token("INT", "0|[1-9][0-9]*")

def test_tostring(int_token):
    assert str(int_token) == "INT"

def test_hash(int_token):
    assert hash(int_token) == hash("INT")


@pytest.fixture
def lexer():
    return Lexer()

def test_add_token(lexer):
    lexer.add_token("INT", "0|[1-9][0-9]*")

    assert "INT" in lexer

def test_regex(lexer):
    lexer.add_token("INT", "0|[1-9][0-9]*")

    assert lexer.get_regex() == "(?P<INT>0|[1-9][0-9]*)"

def test_lex(lexer):
    lexer.add_token("INT", "0|[1-9][0-9]*")

    text = "123 abc 456"

    assert lexer.tokenize(text) == [("INT", "123"), ("INT", "456")]
