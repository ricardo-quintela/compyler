# pylint: skip-file
import pytest
from compyler import Lexer, Token

@pytest.fixture
def lexer():
    l = Lexer()
    l.add_token("INT", "0|[1-9][0-9]*")
    return l

def test_len_lexer(lexer):

    assert len(lexer) == 1

def test_add_token(lexer):

    assert "INT" in lexer

def test_regex(lexer):

    assert lexer.get_regex() == "(?P<INT>0|[1-9][0-9]*)"

def test_lex(lexer):

    text = "123 abc 456"

    assert lexer.tokenize(text) == [Token("INT", "123"), Token("INT", "456")]

def test_filter(lexer):
    tokenized_string = [Token("INT", "123"), Token("INT", "456")]

    lexer.filter(("INT",), tokenized_string)

    assert len(tokenized_string) == 0