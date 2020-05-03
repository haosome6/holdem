from card import Card
from player import Player


class HandsComparator:
    """To compare multiple hands strength.

    === Private Attributes ===
    _ranking:
        mapping from the name of hands to an int, the stronger the hand is, the
        bigger is the number.
    """
    _ranking: map(str, int)

    def __init__(self) -> None:
        """Initialize _ranking.
        """

    def compare_hands(self, all_players: PlayersLinkedList) -> list[Player]:
        """Compare hands strength of Players in all_players that are still
        playing, return the winning players.
        """
