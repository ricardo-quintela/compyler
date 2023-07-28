import sys

from tokens import tk_lexer
from productions import lalr_parser

def main(args):

    filepath = args[1]

    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()

    buffer = tk_lexer.tokenize(text)
    tk_lexer.filter({"NEWLINE", "COMMENT"}, buffer)
    parsed_ast = lalr_parser.parse(buffer)

    print()
    print(buffer)
    print(parsed_ast)

if __name__ == "__main__":
    main(sys.argv)
