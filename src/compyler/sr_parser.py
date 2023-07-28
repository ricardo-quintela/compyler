"""Contains a class ready to register productions
and one to store expressions
"""
from typing import Tuple, List, Union, Dict, Iterator

from .lexer import Token
from .parsing_ast import ASTNode

class Production:
    """Stores the combinations of tokens that compose a production\n
    A production must also include the indices of which tokens or other
    productions will be used as children on the AST.\n\n

    This means that if the production is:
        `Vardecl: ID EQ INT PLUS INT SEMICOLON`
    
    And the indices are (2,4)\n
    
    The result in the AST would be:
    \n
    ```
    Vardecl
    |   INT
    |   INT
    ```
    
    Examples:
        ```
        >>> production = Production(
        ...     {
        ...         ("TOKEN1", "TOKEN2", "TOKEN3"): (1, 2),
        ...         ("TOKEN1", "TOKEN4", "TOKEN3"): (1, 2)
        ...     }
        ... )
        ```
    """
    def __init__(self, name: str, rules: Dict[Tuple[str], Tuple[int]]) -> None:
        self.name = name
        self.rules = rules

    def __str__(self) -> str:
        return self.name

    def __contains__(self, __value: Tuple[str]) -> bool:
        return __value in self.rules

    def __iter__(self) -> Iterator[Dict]:
        return iter(self.rules)

    def __eq__(self, __value: object) -> bool:
        return self.name == str(__value)

    def __len__(self):
        return len(self.rules)

    def get_indices(self, rule: Tuple[str]) -> Union[Tuple[int], None]:
        """Returns the indices of a given rule

        Args:
            rule (Tuple[str]): the rule to access on the map via hashing

        Returns:
            Tuple[int] | None: the indices of the given rule or None if the rule does not exist
        """
        return self.rules[rule] if rule in self.rules else None

    def add_rule(self, new_rule: Dict[Tuple[str], Tuple[int]]):
        """Adds a new rule to the rule dictionary

        Args:
            new_rule (Dict[Tuple[str], Tuple[int]]): the rule to add to the map
        """
        self.rules.update(new_rule)



class LALRParser:
    """Composed by a list of productions.\n
    Uses LALR parsing on a token buffer to build an
    Abstract Syntax Tree.
    """

    def __init__(self) -> None:
        self.productions = list()

    def __len__(self):
        return len(self.productions)

    def __getitem__(self, __index):
        return self.productions[__index]


    def add_production(self, name: str, rules: Dict[Tuple[str], Tuple[int]]):
        """Adds a production to the production list

        Args:
            name (str): the name of the production
            rules (Dict[Tuple[str], Tuple[int]]): the rules of the production
        """
        self.productions.append(Production(name, rules))

    def try_reduce(self, stack: List[Union[Token, ASTNode]]) -> bool:
        """Attempts to reduce the stack to a production in the list

        Args:
            stack (List[Token | ASTNode]): A list of tokens or AST Nodes
        """
        if not stack:
            return False

        # check each production
        for production in self.productions:

            # check each rule
            for rule in production:

                # stack smaller than rule -> cannot be reduced
                if len(stack) < len(rule):
                    continue

                for i, string in enumerate(rule):
                    # top of stack doesnt follow rule -> cannot be reduced
                    if stack[i] != string:
                        break

                # top of stack follows rule -> reduce
                else:
                    # create AST Node
                    node = ASTNode(str(production))
                    for index in production.get_indices(rule):
                        node.add_children(stack[index])

                    for _ in range(len(rule)):
                        stack.pop(0)
                    stack.insert(0, node)

                    return True
        return False

    def parse(self, token_buffer: List[Token]) -> Union[ASTNode, None]:
        """Parses the given token buffer and returns the Abstract Syntax Tree

        Args:
            token_buffer (List[Token]): a list of tokens returned by a lexer

        Returns:
            ASTNode | None: The AST or None if the buffer couldn't be parsed
        """

        inverted_buffer = token_buffer[::-1]

        stack = ["EOF"]

        i = -1
        while i < len(inverted_buffer):

            if self.try_reduce(stack):
                continue

            i += 1

            if i < len(inverted_buffer):
                stack.insert(0, inverted_buffer[i])

        if str(stack[0]) == str(self.productions[0]):
            return stack[0]

        return None
