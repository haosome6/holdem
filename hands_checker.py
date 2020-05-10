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


def _most_frequent_numbers(numbers: Dict[str, int]) -> List[Tuple[str, int]]:
    """Return a list of tuples which records the number and number of occurrence
    of the most frequent number in a given map of number and number of
    occurrence."""
    max_card = (None, 0)
    res = []
    for number, occurrence in numbers.items():
        if occurrence > max_card[1]:
            max_card = (number, occurrence)
            res = [max_card]
        elif occurrence == max_card[1]:
            res.append((number, occurrence))
    # sort the list by the number of the most frequent cards.
    res.sort(key=lambda item: item[0])
    return res


class HandsChecker:
    """To check the strength of hands.
    """

    def _straight_flush(self, cards: List[Card]) -> Tuple[str, List[Card]]:
        """Return "straight flush" and five cards make straight flush in Tuple
        iff <cards> makes a straight flush, otherwise return the result of
        running _full_house with <cards>.
        """
        suits_occurrence = _suit_checker(cards)
        suit = ''

        # if there are more than 4 cards have same suit, extract them
        max_occurrence = max(suits_occurrence.values())
        if max_occurrence < 5:
            return self._four_of_a_kind(cards)
        else:
            for s, occurrence in suits_occurrence.items():
                if occurrence >= 5:
                    suit = s
        suited_cards = []
        cards.sort(reverse=True)
        i = 0
        while len(suited_cards) <= 5 and i < len(cards):
            if cards[i].suit == suit:
                suited_cards.append(cards[i])
            i += 1

        # suited cards is either straight flush, or flush;
        # more than 4 suited cards can't make four of a kind, nor full house
        if self._straight(suited_cards)[0] == 'straight':
            return 'straight flush', self._straight(suited_cards)[1]
        else:
            return 'flush', suited_cards

    def _four_of_a_kind(self, cards: List[Card]) -> Tuple[str, List[Card]]:
        """Return "four of a kind" and five cards make four of a kind in Tuple
        iff <cards> makes a four of a kind, otherwise return the result of
        running _full_house with <cards>.
        """
        numbers = _number_checker(cards)
        # the tuple max_card records the number and the number of occurrence of
        # the card with the highest occurrence time
        max_card = _most_frequent_numbers(numbers)[0]
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
        max_card = _most_frequent_numbers(numbers)[0]
        if max_card[1] < 3:
            return self._straight(cards)
        else:
            del numbers[max_card[0]]
            second_max_card = _most_frequent_numbers(numbers)[0]
            if second_max_card[1] < 2:
                return self._straight(cards)
            else:
                res = []
                for card in cards:
                    if card.number == max_card:
                        res.append(card)
                for card in cards:
                    if card.number == second_max_card and len(res) < 5:
                        res.append(card)
        return 'full house', res

    # no need for flush checker, which is done in _straight_flush

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
        numbers = _number_checker(cards)
        # the tuple max_card records the number and the number of occurrence of
        # the card with the highest occurrence time
        max_card = _most_frequent_numbers(numbers)[0]
        if max_card[1] < 3:
            return self._two_pair(cards)
        else:
            res = []
            # a list which records the cards that do not form the four of a kind
            temple_cards = []
            for card in cards:
                if card.number == max_card[0]:
                    res.append(card)
                else:
                    temple_cards.append(card)
            temple_cards.sort()
            res.append(temple_cards[-1])
            res.append(temple_cards[-2])
            return 'four of a kind', res

    def _two_pair(self, cards: List[Card]) -> Tuple[str, List[Card]]:
        """Return "two pair" and five cards make it in Tuple iff <cards> makes a
        two pair, otherwise return the result of running _one_pair with <cards>.
        """
        numbers = _number_checker(cards)
        max_cards = _most_frequent_numbers(numbers)
        if len(max_cards) < 2:
            return self._one_pair(cards)
        else:
            max_number1 = max_cards[0][0]
            max_number2 = max_cards[1][0]
        res1 = []
        res2 = []
        temple_cards = []
        for card in cards:
            if card.number == max_number1:
                res1.append(card)
            if card.number == max_number2:
                res2.append(card)
            else:
                temple_cards.append(card)
        temple_cards.sort()
        return 'two pair', res1 + res2 + [temple_cards[-1]]

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
