import pytest

from livrel import document


def test_informations_empty():
    info = document.Informations()

    assert info.author is None
    assert info.source is None
    assert info.year is None
    assert info.pagination is None


def test_informations_init():
    info = document.Informations("test", "test", 1, "test")
    assert info.author == "test"
    assert info.source == "test"
    assert info.year == 1
    assert info.pagination == "test"


def test_informations_init_kw():
    info = document.Informations(
        author="test", source="test", year=1, pagination="test"
    )
    assert info.author == "test"
    assert info.source == "test"
    assert info.year == 1
    assert info.pagination == "test"


def test_informations_wrong_kw():
    with pytest.raises(TypeError):
        document.Informations(var_1="test")


def test_informations_wrong_variable():
    with pytest.raises(AttributeError):
        info = document.Informations()
        info.var_1 = "test"


def test_informations_type_attribute():
    info = document.Informations()
    info.author = "test"
    info.source = "test"
    info.year = 1
    info.pagination = "test"

    assert info.author == "test"
    assert info.source == "test"
    assert info.year == 1
    assert info.pagination == "test"
    assert isinstance(info.author, str)
    assert isinstance(info.source, str)
    assert isinstance(info.year, int)
    assert isinstance(info.pagination, str)


def test_informations_wrong_type():
    with pytest.raises(TypeError):
        document.Informations(author=[])

    with pytest.raises(TypeError):
        document.Informations(source=1)

    with pytest.raises(TypeError):
        document.Informations(year="test")

    with pytest.raises(TypeError):
        document.Informations(pagination=())
