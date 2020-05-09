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


def _number_checker(cards: List[Card]) -> Dict[str, int]:
    """Return a dictionary mapping from the number to the corresponding number
    of cards in <cards>.
    """
    numbers = {}
    for card in cards:
        if card.number not in numbers:
            numbers[card.number] = 0
        else:
            numbers[card.number] += 1
    return numbers


def _most_frequent_number(numbers: Dict[str, int]) -> Tuple[str, int]:
    """Return a tuple which records the number and number of occurrence of the
    most frequent number in a given map of number and number of occurrence."""
    max_card = (None, 0)
    for number, occurrence in numbers.items():
        if occurrence > max_card[1]:
            max_card = (number, occurrence)
    return max_card


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
                return self._four_of_a_kind(cards)
        suited_cards = []
        for card in cards:
            if card.suit == suit:
                suited_cards.append(card)

        # if suited cards have flush, then it's a straight flush
        if self._straight(suited_cards)[0] == 'straight':
            return 'straight flush', self._straight(suited_cards)[1]
        else:
            return self._four_of_a_kind(cards)

    def _four_of_a_kind(self, cards: List[Card]) -> Tuple[str, List[Card]]:
        """Return "four of a kind" and five cards make four of a kind in Tuple
        iff <cards> makes a four of a kind, otherwise return the result of
        running _full_house with <cards>.
        """
        numbers = _number_checker(cards)
        # the tuple max_card records the number and the number of occurrence of
        # the card with the highest occurrence time
        max_card = _most_frequent_number(numbers)
        if max_card[1] < 4:
            return self._full_house(cards)
        else:
            res = []
            # a list which records the cards that do not form the four of a kind
            temple_cards = []
            for card in cards:
                if card.number == max_card[0]:
                    res.append(card)
                else:
                    temple_cards.append(card)
            res.append(temple_cards.sort()[-1])
            return 'four of a kind', res

    def _full_house(self, cards: List[Card]) -> Tuple[str, List[Card]]:
        """Return "full house" and five cards make full house in Tuple iff
        <cards> makes a full house, otherwise return the result of running
        _flush with <cards>.
        """
        numbers = _number_checker(cards)
        max_card = _most_frequent_number(numbers)
        if max_card[1] < 3:
            return self._flush(cards)
        else:
            del numbers[max_card[0]]
            second_max_card = _most_frequent_number(numbers)
            if second_max_card[1] < 2:
                return self._flush(cards)
            else:
                res = []
                for card in cards:
                    if card.number == max_card:
                        res.append(card)
                for card in cards:
                    if card.number == second_max_card:
                        res.append(card)
        return 'full house', res

    def _flush(self, cards: List[Card]) -> Tuple[str, List[Card]]:
        """Return "flush" and five cards make flush in Tuple iff <cards> makes a
        flush, otherwise return the result of running _straight with <cards>.
        """
        suits = _suit_checker(cards)
        suit = ''

        # if there are more than 5 cards have same suit, extract them
        for s, number in suits.items():
            if number > 4:
                suit = s
            else:
                return self._straight(cards)
        suited_cards = []
        for card in cards:
            if card.suit == suit:
                suited_cards.append(card)
        suited_cards.sort()
        return 'flush', suited_cards

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
