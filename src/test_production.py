# pylint: skip-file
import pytest
from compyler import Production

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


def test_tostring_str(vardecl_production: Production):
    assert str(vardecl_production) == "VarDecl"

def test_eq_str(vardecl_production: Production):
    assert vardecl_production == "VarDecl"

def test_contains_str(vardecl_production: Production):
    assert ("ID", "ASSIGN", "INT", "PLUS", "INT", "SEMICOLON") in vardecl_production

def test_iter_production(vardecl_production: Production):
    iterator = iter(vardecl_production)
    first_rule = next(iterator)

    assert first_rule == ("ID", "ASSIGN", "INT", "PLUS", "INT", "SEMICOLON")

def test_len_vardecl(vardecl_production: Production):
    assert len(vardecl_production) == 1

def test_get_indices(vardecl_production: Production):
    assert vardecl_production.get_indices(("ID", "ASSIGN", "INT", "PLUS", "INT", "SEMICOLON")) == (2,4)

def test_add_rule(vardecl_production: Production):
    vardecl_production.add_rule(
        {
            ("TEST",):(0)
        }
    )
    assert ("TEST",) in vardecl_production
