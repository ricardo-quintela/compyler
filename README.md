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
'[INT: 123, STRING: "spam", ID: eggs]'
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
'ProductionName:  Token1 EOF -> $0
                | Token1 Token2 EOF -> $0 $1'
```

**WIP**


Stores the combinations of tokens that compose a production
A production must also include the indices of which tokens or other
productions will be used as children on the AST.

This means that if the production is:
    `Vardecl: ID EQ INT PLUS INT SEMICOLON`

And the indices are (2,4)

The result in the AST would be:

```python
Vardecl
|   INT
|   INT
```
    


