from PlayerNode import PlayerNode
from typing import Optional, Any
from Player import Player


class PlayersLinkedList:
    """A players linked list.

    === Attributes ===
    _first: the first PlayerNode
    curr: the current PlayerNode
    """
    _first: Optional[PlayerNode]
    curr: Optional[PlayerNode]

    def __init__(self, number: int) -> None:
        """Initialize a PlayersLinkedList by a given limited number of
        players. """
        pass

    def __getitem__(self, index: int) -> Any:
        pass

    def next_player(self) -> Optional[Player]:
        """"return the next player in the PlayersLinkedList, or return None
        if it does not have a next player."""
        pass

    def add_player(self, index: int, player: Player) -> bool:
        """return true if the player is added successfully in the
        PlayersLinkedList, otherwise return false."""
        pass

    def delete_player(self, player: Player) -> None:
        """delete the given player from the PlayersLinkedList."""
        pass
