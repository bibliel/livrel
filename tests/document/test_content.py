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
