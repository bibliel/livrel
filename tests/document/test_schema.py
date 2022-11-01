from pathlib import Path
from dataclasses import FrozenInstanceError

import pytest

from livrel.document import Schema


def test_schema_obj_exists():
    sch = Schema()
    assert isinstance(sch, Schema)

def test_schema_instance_values():
    sch = Schema()
    assert isinstance(sch.path, Path)
    assert isinstance(sch.data, dict)

def test_schema_parameters_ko():
    with pytest.raises(TypeError):
        Schema(path='')
    with pytest.raises(TypeError):
        Schema(data={})
    
def test_schema_parameters_ko():
    sch = Schema()
    with pytest.raises(FrozenInstanceError):
        sch.path = 'test'
    with pytest.raises(FrozenInstanceError):
        sch.data = {}

def test_schema_file_exist():
    pass

# Schema(Path+schema, data)
# data.id = document
# check if path exists