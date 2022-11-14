import pytest

from livrel import document


def test_section_exists():
    sec = document.Section()
    assert hasattr(sec, "type")
    assert hasattr(sec, "content")
    assert hasattr(sec, "attributes")


def test_section_empty():
    sec = document.Section()
    assert sec.type is None
    assert sec.content == document.Content()
    assert sec.attributes == []


def test_section_variable_kw():
    sec = document.Section(type="dialog", content=document.Content(text="test"))
    assert sec.type == "dialog"
    assert sec.content.text == "test"


def test_section_variables():
    sec = document.Section(
        "dialog", document.Content(text="test"), [document.Attributes(key="test")]
    )
    assert sec.type == "dialog"
    assert sec.content.text == "test"
    assert sec.attributes[0].key == "test"


def test_section_type():
    sec = document.Section()
    with pytest.raises(TypeError):
        sec.type = []
    with pytest.raises(TypeError):
        sec.content = 12
    with pytest.raises(TypeError):
        sec.attributes = "test"


def test_section_type_var_exclude():
    sec = document.Section()
    with pytest.raises(KeyError):
        sec.type = "test"


def test_section_type_attributes_list():
    sec = document.Section()
    with pytest.raises(TypeError):
        sec.attributes = ["test"]


def test_section_wrong_attribute():
    sec = document.Section()
    with pytest.raises(AttributeError):
        sec.test = "test"


def test_section_from_dict_empty():
    sec = document.Section()
    sec.from_dict({})
    assert sec.type is None
    assert sec.content == document.Content()
    assert sec.attributes == []


def test_section_from_dict_type_parameters():
    sec = document.Section()
    with pytest.raises(TypeError):
        sec.from_dict("test")


def test_section_from_dict_data():
    sec = document.Section()
    sec.from_dict({"type": "poem", "content": {}, "attributes": []})
    assert sec.type == "poem"
    assert sec.content == document.Content()
    assert sec.attributes == []


def test_section_from_dict_data_attributes_ok():
    sec = document.Section()
    sec.from_dict(
        {
            "type": "poem",
            "content": {},
            "attributes": [{"key": "test", "value": "test_v"}],
        }
    )
    assert sec.type == "poem"
    assert sec.content == document.Content()
    assert sec.attributes[0].key == "test"
    assert sec.attributes[0].value == "test_v"


def test_section_from_dict_data_attributes_ko():
    sec = document.Section()
    with pytest.raises(TypeError):
        sec.from_dict({"type": "poem", "attributes": "test"})


def test_section_from_dict_data_attributes_list_ko():
    sec = document.Section()
    with pytest.raises(TypeError):
        sec.from_dict({"type": "poem", "content": {}, "attributes": ["test"]})


def test_section_from_dict_data_attributes_list_type_ko():
    sec = document.Section()
    with pytest.raises(TypeError):
        sec.from_dict({"type": "poem", "attributes": [{"key": 1, "value": "test_v"}]})


# Test a full Section
def test_section_full_ok():
    data = {
        "type": "poem",
        "content": {"text": "Ceci est un test", "informations": {"author": "Marc"}},
        "attributes": [{"key": "lang", "value": "la"}],
    }
    sec = document.Section()
    sec.from_dict(data=data)
    assert sec.type == "poem"
    assert sec.content.text == "Ceci est un test"
    assert sec.content.informations.author == "Marc"
    assert sec.attributes[0].key == "lang"
    assert sec.attributes[0].value == "la"


def test_section_limited_ok():
    data = {"type": "narrative", "content": {"text": "Hello World!"}}
    sec = document.Section()
    sec.from_dict(data=data)
    assert sec.type == "narrative"
    assert sec.content.text == "Hello World!"
    assert sec.content.informations.source is None
    assert len(sec.attributes) == 0


def test_section_limited_empty_ok():
    data = {
        "type": "dialog",
        "content": {"text": "Ceci est un test", "informations": {}},
        "attributes": [],
    }
    sec = document.Section()
    sec.from_dict(data=data)
    assert sec.type == "dialog"
    assert sec.content.text == "Ceci est un test"
    assert sec.content.informations.source is None
    assert len(sec.attributes) == 0


def test_section_limited_ok():
    data = {"type": "narrative", "content": {"text": "Hello World!"}}
    sec = document.Section()
    sec.from_dict(data=data)
    assert sec.type == "narrative"
    assert sec.content.text == "Hello World!"
    assert sec.content.informations.source is None
    assert len(sec.attributes) == 0


def test_section_limited_type_attr_ko():
    data = {
        "type": "test",
        "content": {"text": "Ceci est un test", "informations": {"author": "Marc"}},
        "attributes": [{"key": "lang", "value": "la"}],
    }
    sec = document.Section()
    with pytest.raises(KeyError):
        sec.from_dict(data=data)
