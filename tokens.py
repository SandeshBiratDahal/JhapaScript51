from dataclasses import dataclass

@dataclass
class TokenType:
    OPERATOR: str = "OPERATOR"
    KEYWORD: str = "KEYWORD"
    IDENTIFIER: str = "IDENTIFIER"
    INTEGER: str = "INTEGER"
    STRING: str = "STRING"


class Token:
    def __init__(self, type: str, value: str) -> None:
        self.type = type
        self.value = value