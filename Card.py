from __future__ import annotations

compare_map = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    '10': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}


class Card:
    """A card.

    === Private Attributes ===
    _number:
        The number of the card, "A" is the biggest, and "2" is the smallest.
    _suit:
        The suit of the card.

    === Representation Invariants ===
    - _suit must be one of "s", "h", "d", and "c"(represents spade, heart,
      diamond, and club respectively)
    """
    _number: str
    _suit: str

    def __init__(self, number: str, suit: str) -> None:
        """Initialize the card with number <number> and suit <suit>.
        """
        self._number = number
        self._suit = suit

    def __eq__(self, other: Card) -> bool:
        """Return True iff this Card is equal to <other>.

        Two cards are equal if they have the same number.
        """
        return compare_map[self._number] == compare_map[other._number]

    def __ne__(self, other: Card) -> bool:
        """Return True iff this Card is not equal to <other>.
        """
        return not self.__eq__(other)

    def __lt__(self, other: Card) -> bool:
        """Return True iff this Card is less than <other>.
        """
        return compare_map[self._number] < compare_map[other._number]

    def __le__(self, other: Card) -> bool:
        """Return True iff this Card is less than or equal to <other>.
        """
        return compare_map[self._number] <= compare_map[other._number]

    def __gt__(self, other: Card) -> bool:
        """Return True iff this Card is greater than <other>.
        """
        return not self.__le__(other)

    def __ge__(self, other: Card) -> bool:
        """Return True iff this Card is greater than or equal to <other>.
        """
        return not self.__lt__(other)

    def get_number(self) -> str:
        """Return the number of the card.
        """
        return self._number

    def get_suit(self) -> str:
        """Return the suit of the card.
        """
        return self._suit
