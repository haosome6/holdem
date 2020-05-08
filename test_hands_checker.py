from hands_checker import HandsChecker
from card import Card

hands_checker = HandsChecker()


def test_straight_flush() -> None:
    cA = Card('A', 's')
    cK = Card('K', 's')
    cQ = Card('Q', 's')
    cJ = Card('J', 's')
    cT = Card('T', 's')
    c5 = Card('5', 's')
    c3h = Card('3', 'h')

    # straight flush from A to T
    cards_1 = [cT, cQ, cJ, cA, c5, cK, c3h]
    assert hands_checker.get_hands_type(cards_1) == 'straight flush'
    assert hands_checker.get_hands_cards(cards_1)[0].number == 'A'
    assert hands_checker.get_hands_cards(cards_1)[3].number == 'J'

    # straight flush from 5 to A
    c5h = Card('5', 'h')
    c4h = Card('4', 'h')
    c3h = Card('3', 'h')
    c2h = Card('2', 'h')
    cAh = Card('A', 'h')
    cards_2 = [cT, cJ, cAh, c2h, c5h, c4h, c3h]
    assert hands_checker.get_hands_type(cards_2) == 'straight flush'
    assert hands_checker.get_hands_cards(cards_2)[0].number == '5'
    assert hands_checker.get_hands_cards(cards_2)[4].number == 'A'
    assert hands_checker.get_hands_cards(cards_2)[2].number == '3'


def test_four_of_a_kind() -> None:
    c9s = Card('9', 's')
    c9h = Card('9', 'h')
    c9c = Card('9', 'c')
    c9d = Card('9', 'd')
    cAd = Card('A', 'd')
    c5s = Card('5', 's')

    # four of a kind of 9, with kicker A
    cards_1 = [cAd, c9s, c9h, c9c, c9d, c5s]
    assert hands_checker.get_hands_type(cards_1) == 'four of a kind'
    assert hands_checker.get_hands_cards(cards_1)[0].number == '9'
    assert hands_checker.get_hands_cards(cards_1)[4].number == 'A'


if __name__ == "__main__":
    import pytest

    pytest.main(['test_hands_checker.py'])
