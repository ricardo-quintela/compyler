# compyler
Tools to make a compiler in python

# Requirements
[Python 3](https://www.python.org/)

# Lexer

## Registering tokens

The `Token` class from the `lexer` module can be used to register tokens.  
The `@token` decorator must be used or a call to `dataclass(frozen=True, repr=False)` can be made in replacement. This will register the token as a dataclass.
The registered token must be inherit from the `Token` class.

```python
from compyler import Token, token

@token
class INT(Token):
    regex: str = r"[1-9][0-9]*"
    func: Callable = int
```

To run the lexer on a string, first, a list of tokens must be created in order of importance.  
This means that the tokens with the highest priority must be placed first.  

The order of importance grants that a token will not be confused with another at the time of scanning.

```python
@token
class STRING(Token):
    regex: str = r"\"(.|[ \t])*\""

@token
class ID(Token):
    regex: str = r"[a-zA-Z_$][a-zA-Z0-9_$]*"

TOKENS = [INT, STRING, ID]
```

*In this case, the ID token is a subset of the STRING token, so it would disrupt the scanning*.

## Scanning a string

To scan a string, the `Token.lex` method can be invoked.

```python
>>> string = '1234 "spam" eggs'
>>> Token.lex(text=string, tokens=TOKENS)
[INT, STRING, ID]
```

A list of tokens to be ignored can be given and those will be skipped at the time of scanning.

```python
>>> Token.lex(text=string, tokens=TOKENS, ignore=[INT])
[STRING, ID]
```

# Shift Reduce Parser

**wip**
