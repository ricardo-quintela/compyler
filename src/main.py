import sys

from lexer import Token
from sr_parser import Production
from tokens import TOKENS, IGNORED_TOKENS
from productions import PRODUCTIONS, Program

def main(args):

    filepath = args[1]

    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()

    text_tokens = Token.lex(text, TOKENS, IGNORED_TOKENS)
    is_valid = Production.parse(text_tokens, PRODUCTIONS, Program)

    print(text_tokens)
    print(is_valid)


if __name__ == "__main__":
    main(sys.argv)