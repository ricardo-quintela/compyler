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

**wip**
