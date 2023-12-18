# pylint: skip-file
import pytest
from compyler import LALRParser, Token

@pytest.fixture
def lalr_parser():
    lalr_pars = LALRParser()
    lalr_pars.add_production(
        name="VarDecl",
        rules={
            ("ID", "ASSIGN", "INT", "PLUS", "INT", "SEMICOLON"): (2,4)
        }
    )

    return lalr_pars


def test_len_lalrparser(lalr_parser: LALRParser):
    assert len(lalr_parser) == 1

def test_add_production(lalr_parser: LALRParser):
    lalr_parser.add_production(
        "TEST",
        {
            ("TEST",): (0)
        }
    )

    assert lalr_parser.productions[-1] == "TEST"

def test_get_production(lalr_parser: LALRParser):
    assert lalr_parser[0] == "VarDecl"


def test_try_reduce(lalr_parser: LALRParser):
    stack = [
        Token("ID", "var"),
        Token("ASSIGN", "="),
        Token("INT", 1),
        Token("PLUS", "+"),
        Token("INT", 2),
        Token("SEMICOLON", ";")
    ]

    lalr_parser.try_reduce(stack)

    assert stack[0] == "VarDecl"

def test_parse(lalr_parser: LALRParser):

    token_buffer = [
        Token("ID", "var"),
        Token("ASSIGN", "="),
        Token("INT", 1),
        Token("PLUS", "+"),
        Token("INT", 2),
        Token("SEMICOLON", ";")
    ]

    assert lalr_parser.parse(token_buffer) == "VarDecl"

def test_unable_to_parse(lalr_parser: LALRParser):

    token_buffer = [
        Token("ID", "var"),
        Token("ASSIGN", "="),
        Token("INT", 1),
        Token("PLUS", "+"),
        Token("INT", 2),
    ]

    assert lalr_parser.parse(token_buffer) == "ID"


def test_production__repr__():

    lalr_parser = LALRParser()
    lalr_parser.add_production(
        name="VarDecl",
        rules={
            ("ID", "ASSIGN", "INT", "PLUS", "INT", "SEMICOLON"): (2,4)
        }
    )

    assert lalr_parser[0].__repr__() == "VarDecl:  ID ASSIGN INT PLUS INT SEMICOLON -> $2 $4"


def test_production__repr___multiple_rules():

    lalr_parser = LALRParser()
    lalr_parser.add_production(
        name="VarDecl",
        rules={
            ("ID", "ASSIGN", "INT", "PLUS", "INT", "SEMICOLON"): (2,4),
            ("ID", "ASSIGN", "FLOAT", "PLUS", "FLOAT"): (2,4),
        }
    )

    assert lalr_parser[0].__repr__() == "VarDecl:  ID ASSIGN INT PLUS INT SEMICOLON -> $2 $4\n        | ID ASSIGN FLOAT PLUS FLOAT -> $2 $4"
