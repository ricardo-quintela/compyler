# compyler
Tools to make a compiler in python

# Requirements
[Python 3](https://www.python.org/)

# Lexer

## Registering tokens

A `Lexer` object can be used to register tokens.

```python
>>> from compyler import Lexer
>>> lexer = Lexer()
>>> lexer.add_token(name='INT', regex=r'0|[1-9][0-9]*')
```

The tokens are registered in order of importance.

```python
>>> from compyler import Lexer
>>> lexer = Lexer()
>>> lexer.add_token('ID', r'[a-zA-Z_$][a-zA-Z0-9_$]*')
>>> lexer.add_token('STRING', r'\"(.|[ \t])*\"')
```

In the exemple above, two tokens are registered. Despite `ID` being a subset of `STRING`
the lexer's greedy search makes so that the biggest match is found first, thus, `STRING: "spam"`
is caught before than `ID: eggs`.

## Scanning a string

To scan a string, the `Lexer.tokenize` method can be invoked.

```python
>>> from compyler import Lexer
>>> lexer = Lexer()
>>> lexer.add_token(name='INT', regex=r'0|[1-9][0-9]*')
>>> lexer.add_token('ID', r'[a-zA-Z_$][a-zA-Z0-9_$]*')
>>> lexer.add_token('STRING', r'\"(.|[ \t])*\"')
>>> lexer.tokenize('123 "spam" eggs')
[INT: 123, STRING: "spam", ID: eggs]
```

## Filtering

A tokenized string can also be filtered to remove unwanted tokens:

```python
>>> from compyler import Lexer
>>> lexer = Lexer()
>>> lexer.add_token(name='INT', regex=r'0|[1-9][0-9]*')
>>> lexer.add_token('ID', r'[a-zA-Z_$][a-zA-Z0-9_$]*')
>>> lexer.add_token('STRING', r'\"(.|[ \t])*\"')
>>> lexer.add_token("COMMENT", r"#[^\n]*\n*$")
>>> buffer = lexer.tokenize('123 "spam" eggs')
>>> lexer.filter({"COMMENT"}, buffer)
```

# Shift Reduce Parser

## Registering productions

Productions can be created and registered using the `LALRParser` class:

```python
>>> from compyler import LALRParser
>>> lalr_parser = LALRParser()
>>> lalr_parser.add_production(
...     "ProductionName",
...     {
...         ("Token1", "EOF"): (0,),
...         ("Token1", "Token2", "EOF"): (0,1)
...     }
... )
```

A production **must** also include the indices of which tokens or other
productions will be used as children on the AST.

This means that if the production is:

`Vardecl: ID EQ INT PLUS INT SEMICOLON`

And the indices are `(2,4)`

The result in the AST would be:

```python
Vardecl
|   INT
|   INT
```

On the example above:

```python
>>> from compyler import LALRParser
>>> lalr_parser = LALRParser()
>>> lalr_parser.add_production(
...     "ProductionName",
...     {
...         ("Token1", "EOF"): (0,),
...         ("Token1", "Token2", "EOF"): (0,1)
...     }
... )
>>> lalr_parser[0]
ProductionName:  Token1 EOF -> $0
                | Token1 Token2 EOF -> $0 $1
```

## Parsing a tokenized string

After registering the productions on the parser a tokenized string can be parsed:

```python
>>> from compyler import Lexer, LALRParser
>>> lexer = Lexer()
>>> lexer.add_token("ID", r"[a-zA-Z_$][a-zA-Z0-9_$]*")
>>> lexer.add_token("ASSIGN", r"[ \t]*=[ \t]")
>>> lexer.add_token("INT", r"0|[1-9][0-9]*")
>>> lexer.add_token("SEMICOLON", r"[ \t]*;")
>>> lalr_parser = LALRParser()
>>> lalr_parser.add_production(
... "VarDecl", {
...     ("ID", "ASSIGN", "INT", "SEMICOLON"): (0,2)
... }
... )
>>> buffer = lexer.tokenize("var = 1;")
>>> lalr_parser.parse(buffer)
VarDecl
```

The result of the parsing process will either be a `ASTNone` on **success** object or `None` in case the parsing **fails**.

## Accessing a AST node's children

After the parsing is complete and a `ASTNode` object is generated one can access it's children by indexing the object.

On the example above:

```python
>>> parsed_ast = lalr_parser.parse(buffer)
>>> parsed_ast[0]
ID: var
```
