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

    def get_player_by_index(self, index: int) -> PlayerNode:
        """"Get <index>-th PlayerNode with player after button.
        """
        curr = self.button
        while index > 0:
            if curr.next.player is not None:
                index -= 1
            curr = curr.next
        return curr

    def add_player(self, index: int, player: Player, chips_bring_in: int) \
            -> bool:
        """Return true if and only if the player is added successfully in the
        PlayersLinkedList.
        """
        if self[index].is_empty():
            self[index].add_player(player, chips_bring_in)
            # set the first player on the table as button
            if self.button is None:
                self.button = self[index]
            return True
        return False

    def remove_player(self, username: str) -> bool:
        """Return true if and only if remove player with name <username> from
        this list successfully.
        """
        curr = self.button

        while curr.next != self.button:
            if not curr.next.is_empty() and \
                    curr.next.player.username == username:
                curr.next.remove_player()
                return True
            curr = curr.next

        if self.button.player.username == username:
            self.button.remove_player()
            self.button = self.button.get_next_player()
            return True
        else:
            return False
