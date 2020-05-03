from __future__ import annotations


class Player:
    """A player of the game.

    ===Attributes===
    username:
        The username of the player.
    password:
        The password of the player.
    total_chips:
        The total chips of the player that is not playing.
    playing_chips:
        The chips that a player is playing on the table.
    """
    _username: str
    _password: str
    _total_chips: int
    _playing_chips: int

    def __init__(self, username: str, password: str, total_chips: int) -> None:
        """Initialize the player with username <username>, password <password>
        and total_chips <total_chips>.
        """

    def log_in(self, password: str) -> bool:
        """Return True iff <password> matches this Player's password.
        """

    def get_username(self) -> str:
        """Return the username of this Player.
        """

    def fold(self) -> None:
        """The Player folds hands.
        """

    def bet(self, min: int) -> bool:
        """The Player bet certain amount of chips, and it should be greater than
         or equal to the minimum amount <min>.
         """

    def win(self, amount: int) -> None:
        """The Player wins <amount> chips, and added chips to _playing_chips.
        """
