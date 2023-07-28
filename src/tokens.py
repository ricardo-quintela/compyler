# pylint: skip-file
from compyler import Lexer

tk_lexer = Lexer()

tk_lexer.add_token("WIN", r"win")

tk_lexer.add_token("BUTTON", r"button")

tk_lexer.add_token("INT", r"0|[1-9][0-9]*")

tk_lexer.add_token("STRING", r"\"(.|[ \t])*\"")

tk_lexer.add_token("ID", r"[a-zA-Z_$][a-zA-Z0-9_$]*")

tk_lexer.add_token("POINTER", r"->")

tk_lexer.add_token("COMMA", r",")

tk_lexer.add_token("LPAR", r"\(")

tk_lexer.add_token("RPAR", r"\)")

tk_lexer.add_token("SEMICOLON", r";")

tk_lexer.add_token("LBRACE", r"{")

tk_lexer.add_token("RBRACE", r"}")

tk_lexer.add_token("COMMENT", r"#[^\n]*(\n|$)")

tk_lexer.add_token("NEWLINE", r"\n")
