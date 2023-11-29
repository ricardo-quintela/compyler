# pylint: skip-file
import pytest
from compyler import ASTNode, Token

@pytest.fixture
def ast_node():
    # var = 1 + 2;
    return ASTNode("VarDecl",
        [
            Token("ID", "var"),
            ASTNode("Expr",
                [
                    ASTNode("Add",
                        [
                            Token("INT", 1),
                            Token("INT", 2)
                        ]
                    )
                ]
            )
        ]
    )

def test_tostring_astnode(ast_node: ASTNode):
    assert str(ast_node) == "VarDecl"

def test_eq_astnode(ast_node: ASTNode):
    assert ast_node == "VarDecl"

def test_len_astnode(ast_node: ASTNode):
    assert len(ast_node) == 2

def test_add_children(ast_node: ASTNode):
    ast_node.add_children(
        Token("TEST", "test")
    )
    assert ast_node.children[-1] == "TEST"

def test_access_astnode(ast_node: ASTNode):
    assert ast_node[0] == "ID"

def test_ast_representation(ast_node: ASTNode):
    assert ast_node.representation() == "VarDecl\n| ID: var\n| Expr\n| | Add\n| | | INT: 1\n| | | INT: 2"
