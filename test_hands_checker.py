from hands_checker import HandsChecker
from card import Card

hands_checker = HandsChecker()


def test_straight_flush() -> None:
    cA = Card('A', 's')
    cK = Card('K', 's')
    cQ = Card('Q', 's')
    cJ = Card('J', 's')
    cT = Card('10', 's')
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


def test_flush() -> None:
    cQ = Card('Q', 's')
    cJ = Card('J', 's')
    c9 = Card('9', 's')
    c5 = Card('5', 's')
    c3 = Card('3', 's')
    c2 = Card('2', 's')
    c6h = Card('6', 'h')

    # flush of Q
    cards_1 = [c2, c3, c6h, c9, cQ, cJ, c5]
    assert hands_checker.get_hands_type(cards_1) == 'flush'

    result_cards = hands_checker.get_hands_cards(cards_1)
    assert len(result_cards) == 5
    assert result_cards[0].number == 'Q'
    assert result_cards[-1].number == '3'


def test_full_house() -> None:
    c9s = Card('9', 's')
    c9h = Card('9', 'h')
    c9c = Card('9', 'c')
    cAd = Card('A', 'd')
    cAs = Card('A', 's')
    cAc = Card('A', 'c')

    # four of a kind of 9, with kicker A
    cards_1 = [cAd, c9h, cAs, c9s, c9c, cAc]
    assert hands_checker.get_hands_type(cards_1) == 'full house'
    assert len(hands_checker.get_hands_cards(cards_1)) == 5
    assert hands_checker.get_hands_cards(cards_1)[0].number == 'A'
    assert hands_checker.get_hands_cards(cards_1)[3].number == '9'
    assert hands_checker.get_hands_cards(cards_1)[-1].number == '9'


if __name__ == "__main__":
    import pytest

    pytest.main(['test_hands_checker.py'])
