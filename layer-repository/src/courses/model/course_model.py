from dataclasses import dataclass, field

@dataclass
class Courses:
    name: str
    description: str
    id: int = field(default=None)