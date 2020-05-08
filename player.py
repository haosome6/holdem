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
    """
    _username: str
    _password: str
    _total_chips: int


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

    def cash_out(self) -> None:
