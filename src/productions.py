# pylint: skip-file
from sr_parser import Production, production, EOF, Expression
from tokens import *

@production
class Program(Production):
    expression = Expression(
        ["Parent", "EOF"],
        ["Parent", "Children", "EOF"]
    )
    root: bool = True

@production
class Parent(Production):
    expression = Expression(
        ["WIN", "ID", "Body"]
    )

@production
class Relation(Production):
    expression = Expression(
        ["ID", "POINTER", "ID"]
    )

@production
class Child(Production):
    expression = Expression(
        ["Widget", "Relation", "Body"]
    )

@production
class Body(Production):
    expression = Expression(
        ["LBRACE", "Layout", "RBRACE"]
    )

@production
class Children(Production):
    expression = Expression(
        ["Child"],
        ["Children", "Children"]
    )

@production
class Layout(Production):
    expression = Expression(
        ["Property"],
        ["Layout", "Property"],
        ["Layout", "Layout"],
    )

@production
class Widget(Production):
    expression = Expression(
        ["BUTTON"]
    )

@production
class Property(Production):
    expression = Expression(
        ["ID", "STRING", "SEMICOLON"],
        ["ID", "Tuple", "SEMICOLON"]
    )

@production
class Tuple(Production):
    expression = Expression(
        ["LPAR", "INT", "COMMA", "INT", "RPAR"]
    )


PRODUCTIONS = Production.__subclasses__()
