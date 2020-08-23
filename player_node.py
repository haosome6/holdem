from __future__ import annotations

from typing import Optional

from card import Card
from player import Player


class PlayerNode:
    """A player node in a player linked list

    === Attributes ===
    player:
        The player in that position.
    in_game:
        A boolean which indicate whether the player is in the current game or
        not.
    _hands:
        Two Cards the player is holding.
    _betting_amount:
        The player's betting amount for the current street.
    _playing_chips:
        The player's chips left on the table.
    next:
        The next node in the player linked list, or None if there are no more
        nodes.

    === Representation Invariant ===
    _playing_chips is always greater than or equal to zero.
    """
    player: Optional[Player]
    in_game: bool
    _hands: list[Card]
    _betting_amount: int
    _playing_chips: int
    next: Optional[PlayerNode]

    def set_player(self, player: Player, chips_bring_in: int) -> None:
        """Add a player on the node.
        """
        self.player = player
        self.in_game = False
        self._hands = []
        self._betting_amount = 0
        self._playing_chips = chips_bring_in

    def set_hands(self, hands: list[Card]) -> None:
        """Set the current hands of the PlayerNode by given a list of cards.
        """
        self._hands = hands

    def get_hands(self) -> list[Card]:
        """Get the hands of the PlayerNode.
        """
        return self._hands

    def fold_hands(self) -> list[Card]:
        """The Player folds hands.
        """
        cards = []
        cards, self._hands = self._hands, cards
        return cards

    def add_to_betting_amount(self, amount: int) -> None:
        """Add player's betting.
        """
        self._betting_amount += amount
        self._playing_chips -= amount

    def get_betting_amount(self) -> int:
        """Get the amount of betting of the PlayerNode.
        """
        return self._betting_amount

    def add_to_playing_chips(self, amount: int) -> None:
        """Add chips to player's _playing_chips.
        """
        self._playing_chips += amount
