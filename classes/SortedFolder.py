from dataclasses import dataclass, asdict
import json


@dataclass
class SortedFolder:
    name: int
    associated_types: list[str]

    def __init__(self, name: str, associated_types: list[str]):
        self.name: str = name
        self.associated_types: list[str] = associated_types

    def jsonable(self):
        return self.__dict__
