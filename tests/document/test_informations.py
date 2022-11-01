import pytest

from livrel import document


def test_informations_exists():
    info = document.Informations()
    assert isinstance(info, document.Informations)

def test_informations_empty():
    info = document.Informations()
    assert info.author is None
    assert info.source is None
    assert info.year is None
    assert info.pagination is None

def test_informations_init():
    info = document.Informations('Test','test',2022,'test')
    assert info.author == 'Test'
    assert info.source == 'test'
    assert info.year == 2022
    assert info.pagination == 'test'

def test_informations_wrong_type():
    info = document.Informations(year='2022')
    assert info.author is None
    assert info.source is None
    assert info.year == '2022'
    assert info.pagination is None

def test_infomations_from_dict_author_ok():
    info = document.Informations()
    data = {'author':'Gauthier'}
    info.from_dict(data)
    assert info.author == 'Gauthier'

def test_infomations_from_dict_source_ok():
    info = document.Informations()
    data = {'source':'test'}
    info.from_dict(data)
    assert info.source == 'test'

def test_infomations_from_dict_year_ok():
    info = document.Informations()
    data = {'year':2022}
    info.from_dict(data)
    assert info.year == 2022

def test_infomations_from_dict_pagination_ok():
    info = document.Informations()
    data = {'pagination':'test'}
    info.from_dict(data)
    assert info.pagination == 'test'

def test_infomations_from_dict_unknown_ok():
    info = document.Informations()
    data = {'test':'test'}
    info.from_dict(data)
    assert info.author is None
    assert info.source is None
    assert info.year is None
    assert info.pagination is None

def test_infomations_from_dict_type_ko():
    info = document.Informations()
    data = ''
    with pytest.raises(TypeError):
        info.from_dict(data)

def test_informations_attributes_ko():
    info = document.Informations()
    with pytest.raises(AttributeError):
        info.test