# pylint: skip-file
from typing import Callable
from compyler import token, Token

@token
class WIN(Token):
    regex: str = r"win"

@token
class BUTTON(Token):
    regex: str = r"button"

@token
class INT(Token):
    regex: str = r"[1-9][0-9]*"
    func: Callable = int

@token
class STRING(Token):
    regex: str = r"\"(.|[ \t])*\""

@token
class ID(Token):
    regex: str = r"[a-zA-Z_$][a-zA-Z0-9_$]*"

@token
class POINTER(Token):
    regex: str = r"->"

@token
class COMMA(Token):
    regex: str = r","

@token
class LPAR(Token):
    regex: str = r"\("

@token
class RPAR(Token):
    regex: str = r"\)"

@token
class SEMICOLON(Token):
    regex: str = r";"

@token
class LBRACE(Token):
    regex: str = r"{"

@token
class RBRACE(Token):
    regex: str = r"}"

@token
class STR_ERROR(Token):
    regex: str = r"\"(.|[ \t])*[\n\0]"



@token
class COMMENT(Token):
    regex: str = r"#[^\n]*(\n|$)"

@token
class NEWLINE(Token):
    regex: str = r"\n"




TOKENS = Token.__subclasses__()
IGNORED_TOKENS = [COMMENT, NEWLINE]
