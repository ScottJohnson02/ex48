
# Exercise 48: test_lexicon.py
# NOTE: this should be added to the tests directory inside a newly created project
from ex48 import lexicon


def test_directions():
    assert lexicon
    assert lexicon.scan("north") == [('direction', 'north')]
    result = lexicon.scan("north south east")
    assert result == [
        ('direction', 'north'),
        ('direction', 'south'),
        ('direction', 'east')]


def test_verbs():
    assert lexicon.scan("go") == [('verb', 'go')]
    result = lexicon.scan("go kill eat")
    assert result == [
        ('verb', 'go'),
        ('verb', 'kill'),
        ('verb', 'eat')]


def test_stops():
    assert lexicon.scan("the") == [('stop', 'the')]
    result = lexicon.scan("the in of")
    assert result == [
        ('stop', 'the'),
        ('stop', 'in'),
        ('stop', 'of')]


def test_nouns():
    assert lexicon.scan("bear") == [('noun', 'bear')]
    result = lexicon.scan("bear princess")
    assert result == [
        ('noun', 'bear'),
        ('noun', 'princess')]


def test_numbers():
    assert lexicon.scan("1234") == [('number', 1234)]
    result = lexicon.scan("3 91234")
    assert result == [
        ('number', 3),
        ('number', 91234)]


def test_errors():
    assert lexicon.scan("ASDF") == [('error', 'ASDF')]
    result = lexicon.scan("bear IAS princess")
    assert result == [
        ('noun', 'bear'),
        ('error', 'IAS'),
        ('noun', 'princess')]


def test_swears():
    assert lexicon.scan("fuck") == [('swear', 'fuck')]
    result = lexicon.scan("fucking kill bear")
    assert result == [
        ('swear', 'fucking'),
        ('verb', 'kill'),
        ('noun', 'bear')]


def test_case():
    assert lexicon.scan("FUCK") == [('swear', 'FUCK')]
    result = lexicon.scan("fucking KILL bear")
    assert result == [
        ('swear', 'fucking'),
        ('verb', 'KILL'),
        ('noun', 'bear')]
