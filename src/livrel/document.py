from dataclasses import dataclass, field
from pathlib import Path
import importlib.resources


@dataclass
class Informations:
    
    author: str = None
    source: str = None
    year: str = None
    pagination: str = None

    def from_dict(self, data: dict) -> None:

        if not isinstance(data, dict):
            raise TypeError(f'data needs to be a dict not {type(data)}')

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
    text: str = None
    informations: Informations = field(default_factory=Informations)

    def __post_init__(self):
        if not isinstance(self.informations, Informations):
            raise TypeError(f'informations needs to be an Informations object not {type(self.informations)}')
    
    def from_dict(self, data):

        if not isinstance(data, dict):
            raise TypeError(f'data needs to be a dict not {type(data)}')
        
        if 'text' in data:
            self.text = data['text']
        
        if 'informations' in data:
            self.informations.from_dict(data['informations'])


@dataclass(frozen=True)
class Schema:
    path: Path = field(init=False, default_factory=Path)
    data: dict = field(init=False, default_factory=dict)

    def __post_init__(self):
        # Impossible to write on path if frozen is True
        object.__setattr__(self, 'path', importlib.resources.path('src.livrel.schema', 'document.json'))
        print(self.path, self.path.is_file())

        with self.path.open(encoding='utf8', mode='r') as infile:
            print(infile.read())