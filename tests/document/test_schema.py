from pathlib import Path
from dataclasses import FrozenInstanceError
import importlib.resources
import pytest

from livrel import document


def test_schema_init():
    sch = document.Schema()
    assert isinstance(sch.path, Path)
    assert isinstance(sch.data, dict)


def test_schema_init_data():
    with pytest.raises(TypeError):
        document.Schema(data={})


def test_schema_file_exists():
    sch = document.Schema()
    assert sch.path.exists()


def test_schema_custom_exists_ko():
    with pytest.raises(FileNotFoundError):
        document.Schema(path=Path("test"))


def test_schema_attributes_frozen():
    with pytest.raises(FrozenInstanceError):
        document.Schema().path = "test"

    with pytest.raises(FrozenInstanceError):
        document.Schema().data = "test"


def test_schema_custom_ok():
    path = Path() / "tests" / "test_schema_1.json"
    sch = document.Schema(path=path)
    assert sch.data["data"] == "test"


def test_schema_custom_wrong_type():
    with pytest.raises(TypeError):
        document.Schema(path="path")
