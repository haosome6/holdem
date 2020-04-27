from typing import List
from PlayersLinkedList import PlayersLinkedList
from Player import Player
from Card import Card


class Table:
    """A table for playing hold'em by a given number of players.

    === Attributes ===
    _cards: a list of cards left.
    _boards: a list of cards that have been dealt.
    _players: a PlayersLinkedList which represents the players in the table.
    _pot: the current pot of money in this table.
    _small_blind: the amount of small blind.
    _big_blind: the amount of big blind.
    """
    _cards: list[Card]
    _boards: list[Card]
    _players: list[Player]
    _pot: int
    _small_blind: int
    _big_blind: int

    def __init__(self, small_blind: int, big_blind: int, num_players: int) -> None:
        """Initialize a table by a given small_blind, big_blind and the number
        of players."""
        pass

    def add_player(self) -> None:
        """An abstract method which dealing with adding a player to the
        table. """
        raise NotImplementedError

    def dealt_to_players(self) -> None:
        pass

    def dealt_to_boards(self, number: int) -> None:
        pass

    def pre_flop(self) -> None:
        pass

    def flop(self) -> None:
        pass

    def turn(self) -> None:
        pass

    def river(self) -> None:
        pass

    def compare(self) -> list[Player]:
        """compare the cards for each players in game and return a list of
        players who win this game."""
        pass

    def shuffle(self) -> None:
        """shuffle the cards in this table."""
        pass
