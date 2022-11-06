from dataclasses import dataclass, field
from types import NoneType
from typing import Any
from pathlib import Path
import importlib.resources
import json


@dataclass
class Attributes:
    key: str | None = None
    value: str | None = None

    #TODO: verify type of value

    def __post_init__(self) -> None:
        pass

    def from_dict(self, data:dict) -> None:
        if 'key' in data:
            self.key = data['key']
        if 'value' in data:
            self.value = data['value']


@dataclass
class Informations:
    author: str | None = None
    source: str | None = None
    year: int | None = None
    pagination: str | None = None

    def __setattr__(self, __name: str, __value: Any) -> None:
        match __name:
            case "author":
                if not isinstance(__value, (str, NoneType)):
                    raise TypeError(f'The type of "{__name}" must be a str or NoneType')
            case "source":
                if not isinstance(__value, (str, NoneType)):
                    raise TypeError(f'The type of "{__name}" must be a str or NoneType')
            case "year":
                if not isinstance(__value, (int, NoneType)):
                    raise TypeError(f'The type of "{__name}" must be a int or NoneType')
            case "pagination":
                if not isinstance(__value, (str, NoneType)):
                    raise TypeError(f'The type of "{__name}" must be a str or NoneType')
            case _:
                raise AttributeError(
                    f'Attribute "{__name}" doesn\'t exist in Informations object'
                )

        super(Informations, self).__setattr__(__name, __value)
    
    def from_dict(self, data:dict) -> None:
        if 'author' in data:
            self.author = data['author']
        if 'source' in data:
            self.source = data['source']
        if 'year' in data:
            self.year = data['year']
        if 'pagination' in data:
            self.pagination = data['pagination']


@dataclass
class Content:
    text: str | None = None
    informations: Informations = field(default_factory=Informations)

    def __setattr__(self, __name: str, __value: Any) -> None:
        match __name:
            case "text":
                if not isinstance(__value, (str, NoneType)):
                    raise TypeError(f'The type of "{__name}" must be a str or NoneType')
            case "informations":
                if not isinstance(__value, (Informations)):
                    raise TypeError(f'The type of "{__name}" must be an Informations')
            case _:
                raise AttributeError(
                    f'Attribute "{__name}" doesn\'t exist in Content object'
                )

        super(Content, self).__setattr__(__name, __value)
    
    def from_dict(self, data:dict) -> None:
        if 'text' in data:
            self.text = data['text']
        if 'informations' in data:
            self.informations.from_dict(data['informations'])


@dataclass(frozen=True)
class Schema:
    path: Path = field(default_factory=Path)
    data: dict = field(init=False, default_factory=dict)

    def __post_init__(self) -> None:
        if self.path == Path():
            # Impossible to write on attributes if frozen is True
            object.__setattr__(
                self,
                "path",
                importlib.resources.path("src.livrel.schema", "document.json"),
            )

        if not isinstance(self.path, Path):
            raise TypeError(f'The type of "path" must be a Path')

        if not self.path.exists() or not self.path.is_file():
            raise FileNotFoundError(
                f'File "{self.path}" doesn\'t exists or is not a file'
            )

        with self.path.open(mode="r", encoding="utf8") as infile:
            object.__setattr__(self, "data", json.loads(infile.read()))


@dataclass
class Section:
    type: str | None = None
    content: Content = field(default_factory=Content)
    attributes: list[Attributes] | None = field(default_factory=list)

    #TODO: verify type of value