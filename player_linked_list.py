from player_node import PlayerNode
from typing import Optional, Any
from player import Player


class PlayersLinkedList:
    """A players linked list. The last PlayerNode is linked to the first
    PlayerNode.

    === Attributes ===
    _first:
        The first PlayerNode, represents the first seat on the table.
    button:
        The button position of the current round
    acting_player:
        The PlayerNode is acting

    === Representation Invariant ===
    The player attribute of button and acting_player is not None.
    """
    _first: PlayerNode
    button: PlayerNode
    acting_player: PlayerNode

    def __init__(self, number: int) -> None:
        """Initialize a PlayersLinkedList by <number> players.

        Precondition: <number> is no less than 2.
        """
        self._first = PlayerNode()
        pre_node = self._first
        while number != 1:
            pre_node.next = PlayerNode()
            pre_node = pre_node.next
            number -= 1
        pre_node.next = self._first

    def __getitem__(self, index: int) -> PlayerNode:
        """Return the PlayerNode at position <index> in this list.

        Precondition: <index> is less than number of nodes in this list.
        """
        curr = self._first
        curr_index = 0
        while curr_index < index:
            curr = curr.next
            curr_index += 1
        return curr

    def get_next_player(self, curr: PlayerNode) -> PlayerNode:
        """"Get next PlayerNode with player after <curr>.
        """
        while curr.next.player is None:
            curr = curr.next
        return curr.next

    def get_small_blind(self) -> PlayerNode:
        """Return the PlayerNode with small blind of current round.
        """
        curr = self.button
        return self.get_next_player(curr)

    def add_player(self, index: int, player: Player) -> bool:
        """Return true if the player is added successfully in the
        PlayersLinkedList, otherwise return false.
        """
        pass

    def delete_player(self, player: Player) -> None:
        """Delete the given player from the PlayersLinkedList.
        """
        pass
