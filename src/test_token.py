# pylint: skip-file
import pytest
from compyler import Token

@pytest.fixture
def int_token():
    return Token("INT", 123)


def test_tostring_token(int_token):
    assert str(int_token) == "INT"

def test_eq_token(int_token):
    assert int_token == "INT"

def test_hash_token(int_token):
    assert hash(int_token) == hash("INT")
