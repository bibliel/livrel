import pytest

from livrel import document


def test_informations_exists():
    info = document.Informations()

    assert hasattr(info, "author")
    assert hasattr(info, "source")
    assert hasattr(info, "year")
    assert hasattr(info, "pagination")


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


def test_informations_from_dict_empty():
    info = document.Informations()
    info.from_dict({})
    assert info.author is None
    assert info.source is None
    assert info.year is None
    assert info.pagination is None


def test_informations_from_dict_type_parameters():
    info = document.Informations()
    with pytest.raises(TypeError):
        info.from_dict("test")


def test_informations_from_dict_data():
    info = document.Informations()
    info.from_dict(
        {"author": "test_a", "source": "test_s", "year": 1, "pagination": "test_p"}
    )
    assert info.author == "test_a"
    assert info.source == "test_s"
    assert info.year == 1
    assert info.pagination == "test_p"


def test_informations_from_dict_wrong_key():
    info = document.Informations()
    info.from_dict({"author": "test_a", "test": "test_v"})
    assert info.author == "test_a"
    assert info.source is None
    assert info.year is None
    assert info.pagination is None

    info = document.Informations()
    info.from_dict({"test": "test_k", "year": 1})
    assert info.author is None
    assert info.source is None
    assert info.year == 1
    assert info.pagination is None


def test_informations_from_dict_wrong_type_key():
    info = document.Informations()
    with pytest.raises(TypeError):
        info.from_dict({"year": "test"})
