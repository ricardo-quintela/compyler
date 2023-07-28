# pylint: skip-file
from compyler import LALRParser

lalr_parser = LALRParser()

lalr_parser.add_production(
    "Program",
    {
        ("Parent", "EOF"): (0,),
        ("Parent", "Children", "EOF"): (0,1)
    }
)

lalr_parser.add_production(
    "Parent",
    {
        ("WIN", "ID", "Body"): (1,2)
    }
)

lalr_parser.add_production(
    "Relation",
    {
        ("ID", "POINTER", "ID"): (0,2)
    }
)

lalr_parser.add_production(
    "Child",
    {
        ("Widget", "Relation", "Body"): (0,1,2)
    }
)

lalr_parser.add_production(
    "Body",
    {
        ("LBRACE", "Layout", "RBRACE"): (1,)
    }
)

lalr_parser.add_production(
    "Children",
    {
        ("Child",): (0,),
        ("Children", "Children"): (0,1)
    }
)

lalr_parser.add_production(
    "Layout",
    {
        ("Property",): (0,),
        ("Layout", "Layout"): (0,1),
    }
)

lalr_parser.add_production(
    "Widget",
    {
        ("BUTTON",): (0,)
    }
)

lalr_parser.add_production(
    "Property",
    {
        ("ID", "STRING", "SEMICOLON"): (0,1),
        ("ID", "Tuple", "SEMICOLON"): (0,1)
    }
)

lalr_parser.add_production(
    "Tuple",
    {
        ("LPAR", "INT", "COMMA", "INT", "RPAR"): (1,3)
    }
)
