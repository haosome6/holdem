from typing import List, Optional
from Player import Player
from Card import Card


class PlayerNode:
    """A player node in a player linked list

    === Attributes ===
    _item:
        The player in that position, or an integer if the node is empty.
    _hands:
        A list of Cards that held by the player.
    _betting:
        An integer which represent the amount of betting of the player.
    _in_game:
        A boolean which indicate whether the player is involved in the game or
        not.
    next:
        The next node in the player linked list, or None if there are no more nodes.
    """
    _item: Optional[Player, int]
    _hands: list[Card]
    _betting: int
    _in_game: bool
    next: Optional[PlayerNode]

    def __init__(self, player: Optional[Player, int]) -> None:
        """Initialize an PlayerNode which is empty."""
        pass

    def set_hands(self, hands: list[Card]) -> None:
        """Set the current hands of the PlayerNode by given a list of cards."""
        self._hands = hands

    def get_hands(self) -> list[Card]:
        """Get the hands of the PlayerNode."""
        return self._hands

    def set_betting(self, amount: int) -> None:
        """Set the betting of the PlayerNode by a given amount."""
        self._betting = amount

    def get_betting(self) -> int:
        """Get the amount of betting of the PlayerNode."""
        return self._betting

    def set_item(self, player: Optional[Player, int]) -> None:
        """Set the item of the PlayerNode."""
        self._item = player

    def get_item(self) -> Optional[Player, int]:
        """Get the item of the PlayerNode."""
        return self._item

    def set_in_game(self, in_game: bool) -> None:
        """Set the _in_game variable of the PlayerNode by a given bool"""
        self._in_game = in_game

    def get_in_game(self) -> bool:
        """Get the in_game variable of the PlayerNode."""
        return self._in_game