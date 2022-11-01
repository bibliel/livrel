import pytest

from livrel import document


def test_content_exists():
    content = document.Content()
    assert isinstance(content, document.Content)

def test_content_empty():
    content = document.Content()
    assert content.text is None
    assert isinstance(content.informations, document.Informations)
    assert content.informations.author is None
    assert content.informations.source is None
    assert content.informations.year is None
    assert content.informations.pagination is None

def test_content_init():
    content = document.Content('test', document.Informations(author='Gauthier'))
    assert content.text == 'test'
    assert content.informations.author == 'Gauthier'

def test_content_attributes_ko():
    content = document.Content()
    with pytest.raises(AttributeError):
        content.test

def test_content_wrong_informations_type():
    with pytest.raises(TypeError):
        document.Content(informations='test')

def test_content_from_dict_text_ok():
    content = document.Content()
    data = {'text':'test'}
    content.from_dict(data)
    assert content.text == 'test'
    assert content.informations == document.Informations()

def test_content_from_dict_informations_ok():
    content = document.Content()
    data = {'informations':{'author':'Gauthier'}}
    content.from_dict(data)
    assert content.text is None
    assert content.informations.author == 'Gauthier'
    assert content.informations.source is None

def test_content_from_dict_informations_ko():
    content = document.Content()
    data = {'informations':''}
    with pytest.raises(TypeError):
        content.from_dict(data)
    assert content.text is None