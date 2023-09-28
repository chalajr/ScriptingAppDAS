from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    email: str
    id: int = field(default=None)

