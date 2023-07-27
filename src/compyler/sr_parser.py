"""Contains a class ready to register productions
and one to store expressions
"""
from typing import Tuple

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
        >>> expression = Production(
        ...     ("TOKEN1", "TOKEN2"),
        ...     (1, 2)
        ... )
        ```
    """

    def __init__(self, production: Tuple[str], indices: Tuple[int]) -> None:
        self.production = production
        self.indices = indices
