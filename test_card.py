from card import Card


def test__ls_() -> None:
    c1 = Card('A', 's')
    c2 = Card('J', 's')
    c3 = Card('5', 's')
    c4 = Card('5', 'c')
    assert c1 > c2
    assert c2 > c3
    assert c3 == c4
    assert c3 >= c4
    assert c2 >= c4
    assert c4 < c2
    assert c4 <= c3


if __name__ == "__main__":
    import pytest

    pytest.main(['test_card.py'])
