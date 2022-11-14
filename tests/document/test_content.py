import pytest

from livrel import document


def test_content_empty():
    con = document.Content()
    assert con.text is None
    assert isinstance(con.informations, document.Informations)


def test_content_init():
    con = document.Content("test", document.Informations())
    assert con.text == "test"
    assert con.informations == document.Informations()


def test_content_init_kw():
    con = document.Content(text="test", informations=document.Informations())
    assert con.text == "test"
    assert con.informations == document.Informations()


def test_content_wrong_kw():
    with pytest.raises(TypeError):
        document.Content(var_1="test")


def test_content_wrong_variable():
    with pytest.raises(AttributeError):
        con = document.Content()
        con.var_1 = "test"


def test_content_type_attribute():
    con = document.Content()
    con.text = "test"
    con.informations = document.Informations()
    assert con.text == "test"
    assert isinstance(con.text, str)
    assert con.informations.author is None
    assert isinstance(con.informations, document.Informations)


def test_content_wrong_type():
    with pytest.raises(TypeError):
        document.Content(text=[])
    with pytest.raises(TypeError):
        document.Content(informations=[])


def test_content_from_dict_empty():
    con = document.Content()
    con.from_dict({})
    assert con.text is None
    assert con.informations == document.Informations()


def test_content_from_dict_type_parameters():
    con = document.Content()
    with pytest.raises(TypeError):
        con.from_dict("test")


def test_content_from_dict_data():
    con = document.Content()
    con.from_dict({"text": "test", "informations": {"author": "test"}})
    assert con.text == "test"
    assert con.informations.author == "test"


def test_content_from_dict_wrong_key():
    con = document.Content()
    con.from_dict({"text": "test", "test": "test"})
    assert con.text == "test"
    assert con.informations == document.Informations()

    con = document.Content()
    con.from_dict({"test": "test_k", "informations": {"year": 1}})
    assert con.informations.year == 1


def test_content_from_dict_wrong_type_key():
    con = document.Content()
    with pytest.raises(TypeError):
        con.from_dict({"informations": {"year": "test"}})
