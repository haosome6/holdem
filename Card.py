class Card:
    """A card.

    === Private Attributes ===
    number:
        The number of the card, "A" is the biggest, and "2" is the smallest.
    suit:
        The suit of the card.
    """
    _number: str
    _suit: str

    def __init__(self, number: int, suit: str) -> None:
        """Initialize the card with number <number> and suit <suit>.
        """

    def __lt__(self, other: Card) -> bool:
        """Compare this card with another card <other> by number, "A" is the
        biggest.
        """

    def get_number(self) -> str:
        """Return the number of the card.
        """
        return self._number

    def get_suit(self) -> str:
        """Return the suit of the card.
        """
        return self._suit
