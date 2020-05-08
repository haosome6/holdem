from __future__ import annotations
from typing import Tuple, Dict, List
from card import Card


def _suit_checker(cards: List[Card]) -> Dict[str, int]:
    """Return a dictionary mapping from the suit to the corresponding number
    of cards in <cards>.
    """
    suits = {'s': 0, 'h': 0, 'c': 0, 'd': 0}
    for card in cards:
        suits[card.suit] += 1
    return suits


class HandsChecker:
    """To check the strength of hands.
    """

    def _straight_flush(self, cards: List[Card]) -> Tuple[str, List[Card]]:
        """Return "straight flush" and five cards make straight flush in Tuple
        iff <cards> makes a straight flush, otherwise return the result of
        running _full_house with <cards>.
        """
        suits = _suit_checker(cards)
        suit = ''

        # if there are more than 5 cards have same suit, extract them
        for s, number in suits.items():
            if number > 4:
                suit = s
            else:
                return self._full_house(cards)
        suited_cards = []
        for card in cards:
            if card.suit == suit:
                suited_cards.append(card)

        # if suited cards have flush, then it's a straight flush
        if self._straight(suited_cards)[0] == 'straight':
            return 'straight flush', self._straight(suited_cards)[1]
        else:
            return self._full_house(cards)

    def _full_house(self, cards: List[Card]) -> Tuple[str, List[Card]]:
        """Return "full house" and five cards make full house in Tuple iff
        <cards> makes a full house, otherwise return the result of running
        _flush with <cards>.
        """

    def _flush(self, cards: List[Card]) -> Tuple[str, List[Card]]:
        """Return "flush" and five cards make flush in Tuple iff <cards> makes a
        flush, otherwise return the result of running _straight with <cards>.
        """

    def _straight(self, cards: List[Card]) -> Tuple[str, List[Card]]:
        """Return "straight" and five cards make straight in Tuple iff <cards>
        makes a straight, otherwise return the result of running
        _three_of_a_kind with <cards>.
        """

    def _three_of_a_kind(self, cards: List[Card]) -> Tuple[str, List[Card]]:
        """Return "three of a kind" and five cards make it in Tuple iff <cards>
        makes a three of kind, otherwise return the result of running _two_pair
        with <cards>.
        """

    def _two_pair(self, cards: List[Card]) -> Tuple[str, List[Card]]:
        """Return "two pair" and five cards make it in Tuple iff <cards> makes a
        two pair, otherwise return the result of running _one_pair with <cards>.
        """

    def _one_pair(self, cards: List[Card]) -> Tuple[str, List[Card]]:
        """Return "one pair" and five cards make it in Tuple iff <cards> makes a
        one pair, otherwise return the result of running _high_card with <cards>.
        """

    def _high_card(self, cards: List[Card]) -> Tuple[str, List[Card]]:
        """Return "high card" and five biggest cards in <cards> by descending
        order."""

    def _check_hands(self, cards: List[Card]) -> Tuple[str, List[Card]]:
        """Return the strongest hand <cards> can make, and five cards make it.
        """

    def get_hands_type(self, cards: List[Card]) -> str:
        """Return the name of the strongest hand that <cards> can make.
        """

    def get_hands_cards(self, cards: List[Card]) -> List[Card]:
        """Return the five cards that make strongest hand.
        """
