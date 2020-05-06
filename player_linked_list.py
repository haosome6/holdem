from player_node import PlayerNode
from typing import Optional, Any
from player import Player


class PlayersLinkedList:
    """A players linked list.

    === Attributes ===
    _first:
        the first PlayerNode
    button:
        the button of the current round
    curr:
        the current PlayerNode that is acting
    """
    _first: Optional[PlayerNode]
    button: Optional[PlayerNode]
    curr: Optional[PlayerNode]

    def __init__(self, number: int) -> None:
        """Initialize a PlayersLinkedList by a given limited number of
        players. """
        pass

    def __getitem__(self, index: int) -> Any:
        pass

    def next_player(self) -> None:
        """"Set the next player of current player as current player."""
        pass

    def add_player(self, index: int, player: Player) -> bool:
        """Return true if the player is added successfully in the
        PlayersLinkedList, otherwise return false."""
        pass

    def delete_player(self, player: Player) -> None:
        """Delete the given player from the PlayersLinkedList."""
        pass
