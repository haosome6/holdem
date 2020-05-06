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

    === Public Attributes ===
    number:
        The number of the card, "A" is the biggest, and "2" is the smallest.
    suit:
        The suit of the card.

    === Representation Invariants ===
    - _suit must be one of "s", "h", "d", and "c"(represents spade, heart,
      diamond, and club respectively)
    """
    number: str
    suit: str

    def __init__(self, number: str, suit: str) -> None:
        """Initialize the card with number <number> and suit <suit>.
        """
        self.number = number
        self.suit = suit

    def __eq__(self, other: Card) -> bool:
        """Return True iff this Card is equal to <other>.

        Two cards are equal if they have the same number.
        """
        return compare_map[self.number] == compare_map[other.number]

    def __ne__(self, other: Card) -> bool:
        """Return True iff this Card is not equal to <other>.
        """
        return not self.__eq__(other)

    def __lt__(self, other: Card) -> bool:
        """Return True iff this Card is less than <other>.
        """
        return compare_map[self.number] < compare_map[other.number]

    def __le__(self, other: Card) -> bool:
        """Return True iff this Card is less than or equal to <other>.
        """
        return compare_map[self.number] <= compare_map[other.number]

    def __gt__(self, other: Card) -> bool:
        """Return True iff this Card is greater than <other>.
        """
        return not self.__le__(other)

    def __ge__(self, other: Card) -> bool:
        """Return True iff this Card is greater than or equal to <other>.
        """
        return not self.__lt__(other)
