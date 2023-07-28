# pylint: skip-file
import pytest

from compyler import Token, Lexer
from compyler import ASTNode
from compyler import LALRParser, Production


#* TEST TOKEN ----------------------------------------------------------------

@pytest.fixture
def int_token():
    return Token("INT", 123)


def test_tostring_token(int_token):
    assert str(int_token) == "INT"

def test_eq_token(int_token):
    assert int_token == "INT"

def test_hash_token(int_token):
    assert hash(int_token) == hash("INT")

#* TEST LEX ----------------------------------------------------------------

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

#* TEST AST Node ----------------------------------------------------------------

@pytest.fixture
def ast_node():
    node = ASTNode("VarDecl")

    # var = 1 + 2;
    node.add_children(
        Token("ID", "var"),
        Token("ASSIGN", "="),
        Token("INT", 1),
        Token("PLUS", "+"),
        Token("INT", 2),
        Token("SEMICOLON", ";"),
    )
    return node

def test_tostring_astnode(ast_node):
    assert str(ast_node) == "VarDecl"

def test_eq_astnode(ast_node):
    assert ast_node == "VarDecl"

def test_len_astnode(ast_node):
    assert len(ast_node) == 6

def test_add_children(ast_node):
    ast_node.add_children(
        Token("TEST", "test")
    )
    assert ast_node.children[-1] == "TEST"

def test_access_astnode(ast_node):
    assert ast_node[0] == "ID"

#* TEST PRODUCTION ----------------------------------------------------------------

@pytest.fixture
def vardecl_production():
    # VarDecl: ID EQ INT PLUS INT SEMICOLON {$0 = AST($2, $4)}
    production = Production(
        name="VarDecl",
        rules={
            ("ID", "ASSIGN", "INT", "PLUS", "INT", "SEMICOLON"): (2,4)
        }
    )
    return production


def test_tostring_str(vardecl_production):
    assert str(vardecl_production) == "VarDecl"

def test_eq_str(vardecl_production):
    assert vardecl_production == "VarDecl"

def test_contains_str(vardecl_production):
    assert ("ID", "ASSIGN", "INT", "PLUS", "INT", "SEMICOLON") in vardecl_production

def test_iter_production(vardecl_production):
    iterator = iter(vardecl_production)
    first_rule = next(iterator)

    assert first_rule == ("ID", "ASSIGN", "INT", "PLUS", "INT", "SEMICOLON")

def test_len_vardecl(vardecl_production):
    assert len(vardecl_production) == 1

def test_get_indices(vardecl_production):
    assert vardecl_production.get_indices(("ID", "ASSIGN", "INT", "PLUS", "INT", "SEMICOLON")) == (2,4)

def test_add_rule(vardecl_production):
    vardecl_production.add_rule(
        {
            ("TEST",):(0)
        }
    )
    assert ("TEST",) in vardecl_production

#* TEST LALR PARSER ----------------------------------------------------------------

@pytest.fixture
def lalr_parser():
    lalr_parser = LALRParser()
    lalr_parser.add_production(
        name="VarDecl",
        rules={
            ("ID", "ASSIGN", "INT", "PLUS", "INT", "SEMICOLON"): (2,4)
        }
    )

    return lalr_parser


def test_len_lalrparser(lalr_parser):
    assert len(lalr_parser) == 1

def test_add_production(lalr_parser):
    lalr_parser.add_production(
        "TEST",
        {
            ("TEST",): (0)
        }
    )

    assert lalr_parser.productions[-1] == "TEST"

def test_get_production(lalr_parser):
    assert lalr_parser[0] == "VarDecl"


def test_try_reduce(lalr_parser):
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

def test_parse(lalr_parser):

    token_buffer = [
        Token("ID", "var"),
        Token("ASSIGN", "="),
        Token("INT", 1),
        Token("PLUS", "+"),
        Token("INT", 2),
        Token("SEMICOLON", ";")
    ]

    assert lalr_parser.parse(token_buffer) == "VarDecl"

def test_unable_to_parse(lalr_parser):

    token_buffer = [
        Token("ID", "var"),
        Token("ASSIGN", "="),
        Token("INT", 1),
        Token("PLUS", "+"),
        Token("INT", 2),
    ]

    assert lalr_parser.parse(token_buffer) is None
