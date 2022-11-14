import pytest

from livrel import document


def test_attributes_exists():
    att = document.Attributes()
    assert hasattr(att, "key")
    assert hasattr(att, "value")


def test_attributes_empty():
    att = document.Attributes()
    assert att.key is None
    assert att.value is None


def test_attributes_variable_kw():
    att = document.Attributes(key="test", value="test")
    assert att.key == "test"
    assert att.value == "test"


def test_attributes_variables():
    att = document.Attributes("test", "test")
    assert att.key == "test"
    assert att.value == "test"


def test_attributes_type():
    att = document.Attributes()
    with pytest.raises(TypeError):
        att.key = []
    with pytest.raises(TypeError):
        att.value = 12


def test_attributes_wrong_attribute():
    att = document.Attributes()
    with pytest.raises(AttributeError):
        att.test = "test"


def test_attributes_from_dict_empty():
    att = document.Attributes()
    att.from_dict({})
    assert att.key is None
    assert att.value is None


def test_attributes_from_dict_type_parameters():
    att = document.Attributes()
    with pytest.raises(TypeError):
        att.from_dict("test")


def test_attributes_from_dict_data():
    att = document.Attributes()
    att.from_dict({"key": "test_k", "value": "test_v"})
    assert att.key == "test_k"
    assert att.value == "test_v"


def test_attributes_from_dict_wrong_key():
    att = document.Attributes()
    att.from_dict({"key": "test_k", "test": "test_v"})
    assert att.key == "test_k"
    assert att.value is None

    att = document.Attributes()
    att.from_dict({"test": "test_k", "value": "test_v"})
    assert att.key is None
    assert att.value == "test_v"
